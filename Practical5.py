
import socket
import paramiko
from datetime import datetime

HOST, PORT = "127.0.0.1", 2222

if not __import__("os").path.exists("host.key"):
    paramiko.RSAKey.generate(2048).write_private_key_file("host.key")

host_key = paramiko.RSAKey(filename="host.key")

class Honeypot(paramiko.ServerInterface):
    def check_auth_password(self, username, password):
        print(f"[LOGIN ATTEMPT] user='{username}' pass='{password}'")
        return paramiko.AUTH_SUCCESSFUL

    def get_allowed_auths(self, username):
        return "password"

    def check_channel_request(self, kind, chanid):
        return paramiko.OPEN_SUCCEEDED if kind == "session" else paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_channel_shell_request(self, channel):
        return True

    def check_channel_pty_request(self, *args):
        return True

    def check_channel_exec_request(self, channel, command):
        print(f"[COMMAND] {command.decode(errors='replace')}")
        return True


server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(5)

print(f"[HONEYPOT RUNNING] Listening on port {PORT}")

while True:
    client, address = server.accept()
    print(f"[+] Connection from {address}")

    transport = paramiko.Transport(client)
    transport.add_server_key(host_key)

    try:
        transport.start_server(server=Honeypot())
        channel = transport.accept(20)

        if channel:
            channel.send(b"Welcome to SSH server!\n$ ")

            while not channel.closed:
                data = channel.recv(1024)
                if not data:
                    break

                for command in data.decode(errors="replace").splitlines():
                    if command.strip():
                        print(f"[COMMAND] {address} -> {command}")
                        channel.send(b"$ ")

    except Exception as e:
        print("[DISCONNECTED]", address, e)

    finally:
        transport.close()
        client.close()
