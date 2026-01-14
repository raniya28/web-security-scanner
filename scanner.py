import requests

def scan_xss(url):
    payload = "<script>alert(1)</script>"
    response = requests.get(url, params={"q": payload})

    # Check if user input is reflected (escaped or not)
    if "&lt;script&gt;" in response.text or payload in response.text:
        print("[!] Potential XSS Vulnerability Detected (Reflected Input)")
    else:
        print("[+] No XSS detected")

def scan_sqli(url):
    payload = "' OR '1'='1"
    response = requests.get(url, params={"q": payload})

    if "error" in response.text.lower():
        print("[!] SQL Injection Vulnerability Detected")
    else:
        print("[+] No SQL Injection detected")

def main():
    target_url = "http://127.0.0.1:5000/"
    print("Starting Web Security Scan...\n")
    scan_xss(target_url)
    scan_sqli(target_url)

if __name__ == "__main__":
    main()
