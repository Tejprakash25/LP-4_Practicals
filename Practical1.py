from email import message_from_string
import re

print("===== EMAIL HEADER ANALYZER =====")
print("Paste the email header below:")
print("Enter END on a new line to finish:\n")

lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

msg = message_from_string("\n".join(lines))

print("\n===== ANALYSIS REPORT =====")
for field in ["From", "To", "Subject", "Date", "Reply-To", "Message-ID"]:
    if msg[field]:
        print(f"{field}: {msg[field]}")

print("\n===== EMAIL ROUTING DETAILS =====")
for i, received in enumerate(msg.get_all("Received", []), 1):
    received = " ".join(received.split())
    print(f"{i}. {received}")

print("\n===== IP ADDRESS ANALYSIS =====")
for received in msg.get_all("Received", []):
    ip = re.search(r"\((\d{1,3}(?:\.\d{1,3}){3})\)", received)
    if ip:
        print("IP Address:", ip.group(1))

print("\nAnalysis completed.")
print("Note: Header information alone cannot prove a crime.")
