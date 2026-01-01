def generate_report(ip, results):
    print("\n=== Network Recon Report ===")
    print(f"Target: {ip}\n")

    for item in results:
        print(f"Port {item['port']} OPEN")
        print(f"  Banner: {item['banner']}")
        print(f"  Risk: {item['risk']}\n")
