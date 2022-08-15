import os, platform

def ping_ip(ip):
    current_os = platform.system().lower()
    if current_os == "windows":
        parameter = "-n"
    else:
        parameter = "-c"
    exit_code = os.system(f"ping {parameter} 1 -w2 {ip} > /dev/null 2>&1")
    #print(exit_code)
    return exit_code == 0

    

if __name__ == "__main__":
    ip = "10.253.229.14"
    if ping_ip(ip):
        print("Ping Success at : ", ip)
    else:
        print("Ping failed at : ", ip)
