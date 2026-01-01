def analyze(port):
    if port == 22:
        return "MEDIUM (SSH exposed)"
    elif port == 445:
        return "HIGH (SMB exposed)"
    elif port in [80, 443]:
        return "LOW (Web service)"
    else:
        return "UNKNOWN"
