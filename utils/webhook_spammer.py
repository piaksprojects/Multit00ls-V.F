import colorama
from colorama import Fore
import time
import requests
print(f"""
  {Fore.YELLOW}
  ██████  ██▓███   ▄▄▄       ███▄ ▄███▓  ███▄ ▄███▓▓█████ ██▀███  
▒██    ▒ ▓██░  ██ ▒████▄    ▓██▒▀█▀ ██▒ ▓██▒▀█▀ ██▒▓█   ▀▓██ ▒ ██▒
░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░ ▓██    ▓██░▒███  ▓██ ░▄█ ▒
  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██  ▒██    ▒██ ▒▓█  ▄▒██▀▀█▄  
▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒▒██▒   ░██▒░▒████░██▓ ▒██▒
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░   ░  ░░░ ▒░ ░ ▒▓ ░▒▓░
░ ░▒  ░  ░▒ ░       ░   ▒▒ ░░  ░      ░░░  ░      ░ ░ ░    ░▒ ░ ▒░
░  ░  ░  ░░         ░   ▒   ░      ░    ░      ░      ░     ░   ░ 
      ░                 ░  ░       ░   ░       ░      ░     ░     


      """)

webhook = input(f'''{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}] {Fore.WHITE}Webhook Link >> ''')
message = input(f'''{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}] {Fore.WHITE}Message >> ''')
delay = float(input(f'''{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}] {Fore.WHITE}Delay>> '''))

while True:
        try:
          time.sleep(delay)
          data = requests.post(webhook, json={'content': message})

          if data.status_code == 204:
            print(f"{message} sent!")
        except:
          print("Error, or wrong webhook: {}".format(webhook))
          time.sleep(delay)