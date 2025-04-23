import ctypes
import colorama
import requests
import random
import os
from colorama import *
import pystyle
from pystyle import *

def useragent():
     file_path = 'data/useragents.txt'
     
     try:
         with open(file_path, 'r') as file:
             useragents = file.readlines() 
             if useragents:
                 useragents = [agent.strip() for agent in useragents]
                 return random.choice(useragents)
             else:
                 return ''
     except FileNotFoundError:
         print("")
         return ''
     except Exception as e:
         print(f"Une erreur s'est produite lors de la lecture du fichier de user-agents : {e}")
         return ''
 
     print(useragent())

def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

def cls():
    os.system("cls")

cls()
url = 'https://discord.com/api/v9/hypesquad/online'

house = int(input(Colorate.Horizontal(Colors.yellow_to_red, """
  ██░ ██ ▓██   ██▓ ██▓███   ▓█████ ██▀███    ██████   █████   █    ██  ▄▄▄     ▓█████▄ 
▒▓██░ ██  ▒██  ██▒▓██░  ██  ▓█   ▀▓██ ▒ ██▒▒██    ▒ ▒██▓  ██▒ ██  ▓██▒▒████▄   ▒██▀ ██▌
░▒██▀▀██   ▒██ ██░▓██░ ██▓▒ ▒███  ▓██ ░▄█ ▒░ ▓██▄   ▒██▒  ██░▓██  ▒██░▒██  ▀█▄ ░██   █▌
 ░▓█ ░██   ░ ▐██▓░▒██▄█▓▒ ▒ ▒▓█  ▄▒██▀▀█▄    ▒   ██▒░██  █▀ ░▓▓█  ░██░░██▄▄▄▄██░▓█▄   ▌
 ░▓█▒░██▓  ░ ██▒▓░▒██▒ ░  ░▒░▒████░██▓ ▒██▒▒██████▒▒░▒███▒█▄ ▒▒█████▓ ▒▓█   ▓██░▒████▓ 
  ▒ ░░▒░▒   ██▒▒▒ ▒▓▒░ ░  ░░░░ ▒░ ░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒ ░▒▒   ▓▒█ ▒▒▓  ▒ 
  ▒ ░▒░ ░ ▓██ ░▒░ ░▒ ░     ░ ░ ░    ░▒ ░ ▒ ░ ░▒  ░ ░ ░ ▒░  ░ ░░▒░ ░ ░ ░ ░   ▒▒  ░ ▒  ▒ 
  ░  ░░ ░ ▒ ▒ ░░  ░░           ░    ░░   ░ ░  ░  ░     ░   ░  ░░░ ░ ░   ░   ▒   ░ ░  ░ 
  ░  ░  ░ ░ ░              ░   ░     ░           ░      ░       ░           ░     ░    

[1] BRAVERY
[2] BRILLIANCE
[3] BALANCE
[4] RANDOM
[5] LEAVE ALL HYPESQUADS

    Your choice >> """)))

tokens = []
token = []

with open('tokens.txt','r') as f:
        for line in f:
            tokens.append(line)

        for element in tokens:
            token.append(element.strip())

        length = len(token)

for x in range(length):
        header = {
            "authority": "discord.com",
            "method": "POST",
            "path": "/api/v9/users/@me",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{token[x]}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": useragent(),
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }
        if house == 1 or 2 or 3:
            payload = {
                'house_id':house
            }

            r = requests.post(url, headers=header, json=payload)
            if r.status_code == 200 or 204:
                print(f"{Fore.GREEN}    Done!")
            else:
                print(r)

        if house == 5:
            payload1 = {
                'house_id':'None'
            }

            t = requests.delete(url, headers=header, json=payload1)

        if house == 4:
            num = random.randint(1,3)

            payload2 = {
                'house_id':num
            }

            r = requests.post(url, headers=header, json=payload2)
            if r.status_code == 200 or 204:
                print(f"{Fore.GREEN}    Done!")
            else:
                print(r)
        else:
             print("Invalid Choice !")