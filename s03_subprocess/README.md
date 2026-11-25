# Sesión 3: subprocess.run y ping

`ping_one(ip)` corre el comando `ping` del sistema desde Python
con `subprocess.run` y devuelve `True` si el host responde.

## Validación de platform.system()

- Linux / macOS: usa `ping -c 1 <ip>`
- Windows: usa `ping -n 1 <ip>`
- Otro sistema: lanza `RuntimeError`, no adivina el comando.

## Resultado

`returncode == 0` significa que el ping respondió.

$ python3 ping_one.py
192.168.56.101 True
192.168.56.102 True  [200~EOF
