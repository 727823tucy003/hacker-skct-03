# student_name: Dakkshina M
# roll_number: 03
# project_name: ARP Spoofing Tool
# date: 2026-03-29

import datetime, subprocess, os

print(f"[03] setup_lab.py started at {datetime.datetime.now()}")
print(f"[03] Roll No: 03")

subprocess.run(["pip", "install", "scapy", "--break-system-packages"],
               check=True)

os.makedirs("logs", exist_ok=True)
print(f"[03] Logs directory ready.")

os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
print(f"[03] IP forwarding enabled.")
print(f"[03] Setup complete at {datetime.datetime.now()}")
