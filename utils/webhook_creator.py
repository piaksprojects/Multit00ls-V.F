import colorama
from colorama import Fore
import random
import requests
import threading

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

print(f'''
{Fore.YELLOW}
 █     █░▓█████  ▄▄▄▄     ██░ ██  ▒█████   ▒█████   ▀██ ▄█▀     ▄████▄  ██▀███  ▓█████ ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▒▓██░ ██ ▒██▒  ██▒▒██▒  ██▒  ██▄█▒     ▒██▀ ▀█ ▓██ ▒ ██▒▓█   ▀▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██░▒██▀▀██ ▒██░  ██▒▒██░  ██▒ ▓███▄░     ▒▓█    ▄▓██ ░▄█ ▒▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀   ░▓█ ░██ ▒██   ██░▒██   ██░ ▓██ █▄     ▒▓▓▄ ▄██▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░░██▒██▓ ░▒████▒░▓█  ▀█▓ ░▓█▒░██▓░ ████▓▒░░ ████▓▒░ ▒██▒ █▄    ▒ ▓███▀ ░██▓ ▒██▒░▒████ ▓█   ▓██  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒  ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ▒▒ ▓▒    ░ ░▒ ▒  ░ ▒▓ ░▒▓░░░ ▒░  ▒▒   ▓▒█  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
  ▒ ░ ░   ░ ░  ░▒░▒   ░   ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ░▒ ▒░      ░  ▒    ░▒ ░ ▒░ ░ ░    ░   ▒▒     ░      ░ ▒ ▒░   ░▒ ░ ▒░
  ░   ░     ░    ░    ░   ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░░ ░     ░          ░   ░    ░    ░   ▒    ░ ░    ░ ░ ░ ▒     ░   ░ 
    ░       ░  ░ ░        ░  ░  ░    ░ ░      ░ ░   ░  ░       ░ ░        ░        ░        ░               ░ ░     ░     



        ''')

chanid = input(f'''{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}] {Fore.WHITE}What is the channel id you want to make the webhooks in? >> ''')
tukan4 = input(f'''{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}] {Fore.WHITE}What is the token to use? >> ''')
print("Starting Now...")

def spammer():

            url = f'https://discord.com/api/v9/channels/{chanid}/webhooks'

            global randstr

            def randstr(lenn):
                alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
                text = ''
                for i in range(0, lenn):
                    text += alpha[random.randint(0, len(alpha) - 1)]
                return text


            header = {
                "authority": "discord.com",
                "method": "POST",
                "path": f"/api/v9/channels/{chanid}/webhooks",
                "scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "Authorization": f'{tukan4}',
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




            url2 = "data:image/jpeg;base64,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"

            ids = []
            for x in range(1):

                r = requests.post(url,headers=header,json={'name':'Nuked By Piak'})

                try:
                    ids.append(r.json()['id'])
                except Exception as e:
                    print('')

                length = len(ids)
                for i in range(length):
                    header2 = {
                        "authority": "discord.com",
                        "method": "POST",
                        "path": f"/api/v9/webhooks/{ids[i]}",
                        "scheme": "https",
                        "accept": "*/*",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "en-US",
                        "Authorization": f'{tukan4}',
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
                    url1 = f'https://discord.com/api/v9/webhooks/{ids[i]}'
                    t = requests.patch(url1,headers=header2,json={'avatar':url2})

threads = []

for x in range(10):
            t = threading.Thread(target=spammer)
            t.daemon = True
            t.start()
            threads.append(t)

for thread in threads:
            t.join()

print("Finished! Created 10 webhooks named *Nuked by Piak*")