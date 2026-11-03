import subprocess
import sys

print("===== COMPUTER FORENSIC RECOVERY TOOL =====")

image = input("Enter disk image path: ")
output = input("Enter recovery folder path: ")

print("\n===== PARTITION ANALYSIS =====")
subprocess.run(["mmls", image])

print("\n===== DELETED FILE RECOVERY =====")
subprocess.run(["tsk_recover", "-d", image, output])

print("\n===== DELETED PARTITION RECOVERY =====")
subprocess.run(["testdisk", image])

print("\nForensic analysis completed.")
