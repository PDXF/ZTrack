import requests
import csv
import os
import logging

# Set up logging
logging.basicConfig(filename='token_checker.log', level=logging.ERROR)

# Watermark
watermark = """
██████████████████████████████████████████
██  Discord Token Tester by PDX (Zrk)  ██
██████████████████████████████████████████
"""

# ASCII Art Title
ascii_art = """
▒███████▒▄▄▄█████▓▄▄▄█████▓
▒ ▒ ▒ ▄▀░▓  ██▒ ▓▒▓  ██▒ ▓▒
░ ▒ ▄▀▒░ ▒ ▓██░ ▒░▒ ▓██░ ▒░
  ▄▀▒   ░░ ▓██▓ ░ ░ ▓██▓ ░ 
▒███████▒  ▒██▒ ░   ▒██▒ ░ 
░▒▒ ▓░▒░▒  ▒ ░░     ▒ ░░   
░░▒ ▒ ░ ▒    ░        ░    
░ ░ ░ ░ ░  ░        ░      
  ░ ░                       ░
░                           ░
"""

# File to store tokens
TOKEN_FILE = "saved_tokens.txt"

def is_token_active(token):
    url = "https://discord.com/api/v9/users/@me"
    headers = {
        "Authorization": token
    }
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()  # Return user data if the token is valid
    elif response.status_code == 401:
        return None  # Token is invalid
    elif response.status_code == 429:
        return "Rate limit exceeded. Please wait and try again later."
    else:
        logging.error(f"Error {response.status_code}: {response.text}")
        return f"Error: {response.status_code} - {response.text}"

def validate_token_format(token):
    token = token.strip()  # Remove any leading or trailing whitespace
    # Check if the token has the right structure and length
    if len(token) < 59 or not all(c.isprintable() for c in token):  # Example of validating characters
        return False
    return True

def save_token(token):
    with open(TOKEN_FILE, "a") as file:
        file.write(f"{token}\n")

def view_saved_tokens():
    try:
        with open(TOKEN_FILE, "r") as file:
            tokens = file.readlines()
            if not tokens:
                return "No saved tokens found."
            else:
                return "\n".join([f"- {line.strip()}" for line in tokens])
    except FileNotFoundError:
        return "No saved tokens found."

def clear_saved_tokens():
    if os.path.exists(TOKEN_FILE):
        os.remove(TOKEN_FILE)
        return "All saved tokens have been cleared."
    else:
        return "No tokens to clear."

def export_tokens_to_csv():
    if not os.path.exists(TOKEN_FILE):
        return "No tokens to export."

    with open(TOKEN_FILE, "r") as infile, open("saved_tokens.csv", "w", newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Token"])  # CSV Header
        for line in infile:
            writer.writerow([line.strip()])
    return "Tokens exported to saved_tokens.csv successfully!"

def display_user_data(user_data):
    username = user_data.get('username', 'N/A')
    discriminator = user_data.get('discriminator', 'N/A')
    user_id = user_data.get('id', 'N/A')
    email = user_data.get('email', 'Not Available')
    avatar_url = user_data.get('avatar', None)

    if avatar_url:
        avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_url}.png"
        
    return f"""
--- Token is valid ---
Username: {username}#{discriminator}
User ID: {user_id}
Email: {email}
Avatar URL: {avatar_url if avatar_url else 'No avatar set'}
"""

def list_user_guilds(token):
    url = "https://discord.com/api/v9/users/@me/guilds"
    headers = {
        "Authorization": token
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        guilds = response.json()
        if guilds:
            return "\n".join([f"Guild ID: {guild['id']}, Name: {guild['name']}" for guild in guilds])
        else:
            return "User is not a member of any guilds."
    else:
        return f"Error: {response.status_code} - {response.text}"

def get_user_status(token):
    user_data = is_token_active(token)
    if isinstance(user_data, dict):
        return f"Status: {user_data.get('status', 'Unknown')}"
    return user_data  # Return the error message if any

def change_nickname(token, guild_id, nickname):
    url = f"https://discord.com/api/v9/guilds/{guild_id}/members/@me/nick"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    payload = {"nick": nickname}
    
    response = requests.patch(url, headers=headers, json=payload)
    
    if response.status_code == 204:
        return "Nickname changed successfully."
    else:
        return f"Error changing nickname: {response.status_code} - {response.text}"

def logout_token(token):
    url = "https://discord.com/api/v9/auth/logout"
    headers = {
        "Authorization": token
    }
    
    response = requests.post(url, headers=headers)
    
    if response.status_code == 204:
        return "Token logged out successfully."
    else:
        return f"Error logging out token: {response.status_code} - {response.text}"

def main():
    print(watermark)  # Print the watermark
    print(ascii_art)
    
    while True:
        print("\n--- Discord Token Tester ---")
        print("1. Check Token")
        print("2. View Saved Tokens")
        print("3. Clear Saved Tokens")
        print("4. Export Tokens to CSV")
        print("5. List User Guilds")
        print("6. Get User Status")
        print("7. Change Nickname")
        print("8. Logout Token")
        print("9. Exit")
        print("-------------------------")
        
        choice = input("Select an option (1-9): ").strip()
        output_message = ""

        if choice == "1":  # Check Token
            token = input("Enter Discord Token: ").strip()
            if not validate_token_format(token):
                output_message = "Invalid token length."
                print("\n--- Output ---")
                print(output_message)
                input("\nPress Enter to close and go back to the menu...")
                continue

            user_data = is_token_active(token)

            if isinstance(user_data, dict):
                output_message = display_user_data(user_data)
                save_option = input("Save this token? (yes/no): ").strip().lower()
                if save_option == 'yes':
                    save_token(token)
            else:
                output_message = f"Token is invalid. {user_data}"
                
        elif choice == "2":  # View Saved Tokens
            output_message = view_saved_tokens()
                
        elif choice == "3":  # Clear Saved Tokens
            output_message = clear_saved_tokens()
        
        elif choice == "4":  # Export Tokens to CSV
            output_message = export_tokens_to_csv()

        elif choice == "5":  # List User Guilds
            token = input("Enter Discord Token: ").strip()
            output_message = list_user_guilds(token)
        
        elif choice == "6":  # Get User Status
            token = input("Enter Discord Token: ").strip()
            output_message = get_user_status(token)

        elif choice == "7":  # Change Nickname
            token = input("Enter Discord Token: ").strip()
            guild_id = input("Enter Guild ID: ").strip()
            nickname = input("Enter New Nickname: ").strip()
            output_message = change_nickname(token, guild_id, nickname)

        elif choice == "8":  # Logout Token
            token = input("Enter Discord Token: ").strip()
            output_message = logout_token(token)

        elif choice == "9":  # Exit
            print("Exiting the program...")
            break
        
        else:
            output_message = "Invalid choice. Please select a valid option."
        
        print("\n--- Output ---")
        print(output_message)
        input("\nPress Enter to close and go back to the menu...")

if __name__ == "__main__":
    main()
