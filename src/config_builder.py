import json
import os
try:
    from colorama import Fore, Style, init
except ModuleNotFoundError:
    os.system("import colorama")

init(autoreset=True)

def build_config():
    print(f"""{Fore.MAGENTA}
 ▄▄▄· ▄· ▄▌▄▄▄   ▄▄▄· ▄▄·     ▄▄▄▄· ▄• ▄▌▪  ▄▄▌  ·▄▄▄▄  ▄▄▄ .▄▄▄  
▐█ ▄█▐█▪██▌▀▄ █·▐█ ▄█▐█ ▌▪    ▐█ ▀█▪█▪██▌██ ██•  ██▪ ██ ▀▄.▀·▀▄ █·
 ██▀·▐█▌▐█▪▐▀▀▄  ██▀·██ ▄▄    ▐█▀▀█▄█▌▐█▌▐█·██▪  ▐█· ▐█▌▐▀▀▪▄▐▀▀▄ 
▐█▪·• ▐█▀·.▐█•█▌▐█▪·•▐███▌    ██▄▪▐█▐█▄█▌▐█▌▐█▌▐▌██. ██ ▐█▄▄▌▐█•█▌
.▀     ▀ • .▀  ▀.▀   ·▀▀▀     ·▀▀▀▀  ▀▀▀ ▀▀▀.▀▀▀ ▀▀▀▀▀•  ▀▀▀ .▀  ▀
""")
    print(Fore.CYAN + "Welcome to the Discord RPC Config Builder!" + Style.RESET_ALL)
    print(Fore.CYAN + "Please provide the following information." + Style.RESET_ALL)

    config = {
        "token": input(Fore.BLUE + "Enter bot's token: " + Fore.GREEN),
        "client_id": input(Fore.BLUE + "Enter bot's ID: " + Fore.GREEN),
        "user_id": input(Fore.BLUE + "Enter your ID: " + Fore.GREEN),
        "details": input(Fore.BLUE + "Enter details: " + Fore.GREEN),
        "state": input(Fore.BLUE + "Enter state: " + Fore.GREEN),
        "large_image": input(Fore.BLUE + "Enter large image name: " + Fore.GREEN),
        "large_text": input(Fore.BLUE + "Enter large image text: " + Fore.GREEN),
        "buttons": []
    }

    # Add buttons dynamically
    button_count = int(input(Fore.BLUE + "Enter the number of buttons: " + Fore.GREEN))
    for i in range(button_count):
        label = input(Fore.BLUE + f"Enter label for button {i + 1}: " + Fore.GREEN)
        url = input(Fore.BLUE + f"Enter URL for button {i + 1}: " + Fore.GREEN)
        config["buttons"].append({"label": label, "url": url})

    return config

def save_config(config):
    with open("config.json", "w") as config_file:
        json.dump(config, config_file, indent=4)

if __name__ == "__main__":
    config_data = build_config()
    save_config(config_data)

    print(Fore.BLUE + "\nConfiguration saved to 'config.json'." + Style.RESET_ALL)
