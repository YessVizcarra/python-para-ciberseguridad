import subprocess
import platform


def ping_one(ip):
    system = platform.system()
    if system in ("Linux", "Darwin"):
        command = ["ping", "-c", "1", ip]
    elif system == "Windows":
        command = ["ping", "-n", "1", ip]
    else:
        raise RuntimeError(f"Sistema no soportado: {system}")
    result = subprocess.run(command, capture_output=True, timeout=5)
    return result.returncode == 0


if __name__ == "__main__":
    for ip in ["192.168.56.101", "192.168.56.102"]:
        print(ip, ping_one(ip))
