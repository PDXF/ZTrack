import json
import requests
import os

# Colors
Wh = '\033[1;90m'   # Gray
Gr = '\033[0;35m'   # Magenta

# Utility function to clear the console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def track_ip():
    ip = input(f"{Wh}\nEnter IP target: {Gr}")
    response = requests.get(f"http://ipwho.is/{ip}")
    ip_data = response.json()

    print(f"{Wh}\nIP Target: {Gr}{ip}")
    print(f"{Wh}Country: {Gr}{ip_data['country']}")
    print(f"{Wh}City: {Gr}{ip_data['city']}")
    print(f"{Wh}Maps: {Gr}https://www.google.com/maps/@{ip_data['latitude']},{ip_data['longitude']},8z")

def show_ip():
    response = requests.get('https://api.ipify.org/')
    print(f"\n{Wh}Your IP Address: {Gr}{response.text}")

# Main function to present options
def main():
    clear()
    options = {
        1: track_ip,
        2: show_ip,
        0: exit
    }

    while True:
        print(f"\n{Wh}1: Track IP Address\n{Wh}2: Retrieve Your IP\n{Wh}0: Exit")
        choice = int(input(f"{Wh}Select an option: {Gr}"))
        if choice in options:
            options[choice]()
        else:
            print(f"{Wh}Invalid option. Please try again.")

if __name__ == "__main__":
    main()
