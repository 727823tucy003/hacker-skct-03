# student_name: Dakkshina M
# roll_number: 03
# project_name: ARP Spoofing Tool
# date: 2026-03-29

import datetime, subprocess, sys

print(f"[03] run_tool.py started at {datetime.datetime.now()}")
print(f"[03] Roll No: 03")

target_ip  = "10.16.113.196"   # <-- change to your Metasploitable2 IP
gateway_ip = "10.16.113.196"     # <-- change to your gateway IP

print(f"[03] Running ARP spoof: target={target_ip} gateway={gateway_ip}")
print(f"[03] Tool will run for 30 seconds...")

try:
    result = subprocess.run(
        ["sudo", "python3", "tool_main.py", target_ip, gateway_ip],
        timeout=30
    )
except subprocess.TimeoutExpired:
    print(f"[03] 30 second run complete at {datetime.datetime.now()}")

print(f"[03] run_tool.py finished at {datetime.datetime.now()}")
