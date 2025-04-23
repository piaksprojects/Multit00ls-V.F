import pystyle
from pystyle import *
import requests

menu =""" 
 █     █░▓█████  ▄▄▄▄     ██░ ██  ▒█████   ▒█████   ▀██ ▄█▀      ██ ███▄    █    █████ ▒█████  
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▒▓██░ ██ ▒██▒  ██▒▒██▒  ██▒  ██▄█▒     ▒▓██ ██ ▀█   █  ▓██    ▒██▒  ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██░▒██▀▀██ ▒██░  ██▒▒██░  ██▒ ▓███▄░     ░▒██▓██  ▀█ ██▒ ▒████  ▒██░  ██▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀   ░▓█ ░██ ▒██   ██░▒██   ██░ ▓██ █▄      ░██▓██▒  ▐▌██▒ ░▓█▒   ▒██   ██░
░░██▒██▓ ░▒████▒░▓█  ▀█▓ ░▓█▒░██▓░ ████▓▒░░ ████▓▒░ ▒██▒ █▄     ░██▒██░   ▓██░▒░▒█░   ░ ████▓▒░
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒  ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ▒▒ ▓▒     ░▓ ░ ▒░   ▒ ▒ ░ ▒ ░   ░ ▒░▒░▒░ 
  ▒ ░ ░   ░ ░  ░▒░▒   ░   ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ░▒ ▒░      ▒ ░ ░░   ░ ▒░░ ░       ░ ▒ ▒░ 
  ░   ░     ░    ░    ░   ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░░ ░       ▒    ░   ░ ░   ░ ░   ░ ░ ░ ▒  
    ░       ░  ░ ░        ░  ░  ░    ░ ░      ░ ░   ░  ░         ░          ░ ░           ░ ░  """


print(Colorate.Horizontal(Colors.yellow_to_red, menu))
link = input(Colorate.Horizontal(Colors.yellow_to_red, "What is your webhook link? >> "))
r = requests.get(link)

# Corrected string concatenation
print("Webhook Name: " + r.json()["name"])
print("Webhook ID: " + r.json()["id"])
print("Guild ID of Webhook: " + r.json()["guild_id"])
print("Channel ID of Webhook: " + r.json()["channel_id"])

if r.json()['avatar'] is None:
    print('Avatar: None')
else:
    avatar = f'https://cdn.discordapp.com/avatars/{r.json()["id"]}/{r.json()["avatar"]}'
    print(f'Avatar: {avatar}')
    print(f'Token of Webhook: {r.json()["token"]}')
    input("Press return to have the main menu")