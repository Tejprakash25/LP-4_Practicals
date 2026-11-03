from datetime import datetime, timedelta

# Sample system log entries for practical
logs = [
    "2026-10-23 10:00:00 LOGIN_FAILED user1",
    "2026-10-23 10:01:00 LOGIN_FAILED user1",
    "2026-10-23 10:02:00 LOGIN_SUCCESS user2",
    "2026-10-23 10:03:00 LOGIN_FAILED user1",
    "2026-10-23 10:04:00 LOGIN_FAILED user1",
    "2026-10-23 10:05:00 LOGIN_FAILED user1",
]

# Save logs to a file
with open("system_logs.txt", "w") as file:
    for log in logs:
        file.write(log + "\n")

print("Log Capturing and Event Correlation")
print("-----------------------------------")

failed_events = {}

# Read and analyze logs
with open("system_logs.txt", "r") as file:
    for line in file:
        print("Log:", line.strip())
        parts = line.strip().split()
        event_time = datetime.strptime(
            parts[0] + " " + parts[1],
            "%Y-%m-%d %H:%M:%S",
        )
        event_type = parts[2]
        username = parts[3]

        if event_type == "LOGIN_FAILED":
            if username not in failed_events:
                failed_events[username] = []
            failed_events[username].append(event_time)

print("\nEvent Correlation Results")
print("-------------------------")

for username, times in failed_events.items():
    for start in times:
        count = sum(
            1
            for event_time in times
            if start <= event_time <= start + timedelta(minutes=5)
        )
        if count >= 5:
            print("Possible suspicious activity detected!")
            print("User:", username)
            print("Failed login attempts:", count)
            print("Time window: 5 minutes")
            break
    else:
        continue
    break
else:
    print("No suspicious activity detected.")
