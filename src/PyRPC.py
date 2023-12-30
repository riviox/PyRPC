import time
import json
import os
import ctypes

try:
    import requests
    from colorama import Fore, Style, init
    from pypresence import Presence
except ModuleNotFoundError:
    os.system("import pypresence requests colorama")

init(autoreset=True)

CONFIG_FILE = "config.json"

def load_config():
    with open(CONFIG_FILE, "r") as config_file:
        return json.load(config_file)

def connect_to_discord_rpc(client_id):
    rpc = Presence(client_id)
    rpc.connect()
    return rpc

UPDATE_INTERVAL = 15

def update_discord_rpc(rpc, config):
    user_info = get_user_info(config["user_id"])
    if user_info:
        print_info(f"Logged in as {Fore.GREEN}{user_info.get('tag', '')}{Style.RESET_ALL}")

    while True:
        try:
            user_id = config["user_id"]
            user_info = get_user_info(user_id)

            if user_info:
                avatar_url = get_avatar_url(user_info)
                if avatar_url:
                    config["large_image"] = avatar_url

                buttons = config["buttons"]
                rpc.update(
                    details=user_info.get("tag", ""),
                    state=config["state"],
                    large_image=config["large_image"],
                    large_text=config.get("large_text", ""),
                    start=int(time.time()),
                    buttons=buttons
                )

        except requests.exceptions.RequestException as e:
            print_error(f"{Fore.RED}HTTP request error: {e}{Style.RESET_ALL}")
            print_debug(f"Details: {config}")

        except Exception as e:
            print_error(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
            print_debug(f"Details: {config}")

        time.sleep(UPDATE_INTERVAL)

def get_user_info(user_id):
    api_url = f"https://discordlookup.mesavirep.xyz/v1/user/{user_id}"
    response = requests.get(api_url)
    return response.json()

def get_avatar_url(user_info):
    return user_info.get("avatar", {}).get("link", None)

def print_error(message):
    print(f"{Fore.RED}[Error]{Style.RESET_ALL} {message}")

def print_info(message):
    print(f"{Fore.CYAN}[Info]{Style.RESET_ALL} {message}")

def print_debug(message):
    print(f"{Fore.MAGENTA}[Debug]{Style.RESET_ALL} {message}")

def print_ascii():
    ascii_art = f"""
{Fore.MAGENTA} ▄▄▄· ▄· ▄▌▄▄▄   ▄▄▄· ▄▄· 
{Fore.MAGENTA}▐█ ▄█▐█▪██▌▀▄ █·▐█ ▄█▐█ ▌▪
{Fore.MAGENTA} ██▀·▐█▌▐█▪▐▀▀▄  ██▀·██ ▄▄
{Fore.MAGENTA}▐█▪·• ▐█▀·.▐█•█▌▐█▪·•▐███▌
{Fore.MAGENTA}.▀     ▀ • .▀  ▀.▀   ·▀▀▀ 
{Fore.GREEN} Made by {Fore.YELLOW}_riviox_{Style.RESET_ALL}
"""
    print(ascii_art)

try:
    print_ascii()
    print_info(f"Loading config from '{CONFIG_FILE}'")
    config = load_config()

    rpc = connect_to_discord_rpc(config["client_id"])
    print_info(f"{Fore.GREEN}Discord RPC is active{Style.RESET_ALL}")

    update_discord_rpc(rpc, config)

except KeyboardInterrupt:
    print_info(f"{Fore.YELLOW}Closing Discord RPC{Style.RESET_ALL}")
    rpc.close()
except Exception as e:
    print_error(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
    print_debug(f"Details: {config}")
    rpc.close()
