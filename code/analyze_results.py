# student_name: Dakkshina M
# roll_number: 03
# project_name: ARP Spoofing Tool
# date: 2026-03-29

import datetime, os

print(f"[03] analyze_results.py started at {datetime.datetime.now()}")

log_file = "logs/run_output.txt"

if not os.path.exists(log_file):
    print("[03] ERROR: log file not found. Run run_tool.py first.")
    exit(1)

with open(log_file, "r") as f:
    lines = f.readlines()

packets_sent = sum(1 for l in lines if "Sent" in l or "packet" in l.lower())
errors = sum(1 for l in lines if "error" in l.lower() or "exception" in l.lower())

print("\n========== ANALYSIS REPORT ==========")
print(f"Roll No     : 03")
print(f"Timestamp   : {datetime.datetime.now()}")
print(f"Total lines : {len(lines)}")
print(f"Packets sent: {packets_sent}")
print(f"Errors found: {errors}")
print("======================================\n")

os.makedirs("logs", exist_ok=True)
with open("logs/analysis_report.txt", "w") as f:
    f.write(f"Roll No: 03\nTimestamp: {datetime.datetime.now()}\n")
    f.write(f"Packets sent: {packets_sent}\nErrors: {errors}\n")

print("[03] Analysis complete. Saved to logs/analysis_report.txt")
