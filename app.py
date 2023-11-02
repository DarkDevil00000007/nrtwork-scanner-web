from flask import Flask, request, render_template
import nmap

app = Flask(__name)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    ip_addr = request.form["ip_addr"]
    scan_type = request.form["scan_type"]

    scanner = nmap.PortScanner()

    if scan_type == '1':
        # Perform SYN ACK Scan
        scanner.scan(ip_addr, '1-1624', '-v -sS')
    elif scan_type == '2':
        # Perform UDP Scan
        scanner.scan(ip_addr, '1-1624', '-v -sU')
    elif scan_type == '3':
        # Perform Comprehensive Scan
        scanner.scan(ip_addr, '1-1624', '-v -sS -sV -sC -A -O')

    return f"Scan result for {ip_addr} (Type {scan_type}):\n{scanner.all_hosts()}\n{scanner[ip_addr]}"

if __name__ == "__main":
    app.run()
