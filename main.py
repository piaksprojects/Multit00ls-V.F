import ctypes
import os
import subprocess
import threading
import random
import time
try:
    import pystyle
    import colored
    import colorama
    import itertools
    import asyncio
    import requests
    import selenium
    import shutil
    import discord
    import more_itertools
    import tls_client

except ModuleNotFoundError:
    os.system("pip install pystyle")
    os.system("pip install colored")
    os.system("pip install colorama")
    os.system("pip install discord.py==1.7.3")
    os.system("pip install requests")
    os.system("pip install selenium")
    os.system("pip install pyinstaller")
    os.system("pip install requests")
    os.system("pip install more_itertools")
    os.system("pip install pywin32")
    os.system("pip install pycryptodome")
    os.system("pip install discord.py-self")
    os.system("pip install asyncio")
    os.system("pip install tls_client")
    os.system("cls")

from colorama import Fore, Back, Style, init
from pystyle import *
from colored import *
from threading import Thread

def execute_script(script_name):
    script_path = os.path.join('utils', script_name)
    subprocess.run(['python', script_path], check=True)

def set_console_fullscreen():
    # Obtenir le handle de la console
    kernel32 = ctypes.windll.kernel32
    user32 = ctypes.windll.user32
    hwnd = kernel32.GetConsoleWindow()

    # Obtenir le style actuel de la fenêtre
    style = user32.GetWindowLongW(hwnd, -16)
    # Ajouter le style de plein écran
    user32.SetWindowLongW(hwnd, -16, style | 0x00040000)

    # Redimensionner la fenêtre pour qu'elle occupe tout l'écran
    user32.ShowWindow(hwnd, 3)  # SW_MAXIMIZE

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

def cls():
   os.system("cls")

def premium():
    print(Colorate.Horizontal(Colors.yellow_to_red,"Ceci est une option Premium !"))

intro = """
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                                                                                       ┃                   
┃██████╗ ██╗ █████╗ ██╗  ██╗    ███╗   ███╗██╗   ██╗██╗  ████████╗██╗   ████████╗ ██████╗  ██████╗ ██╗     ███████╗    ███████╗██████╗ ███████╗███████╗ ┃
┃██╔══██╗██║██╔══██╗██║ ██╔╝    ████╗ ████║██║   ██║██║  ╚══██╔══╝██║   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝    ██╔════╝██╔══██╗██╔════╝██╔════╝ ┃
┃██████╔╝██║███████║█████╔╝     ██╔████╔██║██║   ██║██║     ██║   ██║█████╗██║   ██║   ██║██║   ██║██║     ███████╗    █████╗  ██████╔╝█████╗  █████╗   ┃
┃██╔═══╝ ██║██╔══██║██╔═██╗     ██║╚██╔╝██║██║   ██║██║     ██║   ██║╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║    ██╔══╝  ██╔══██╗██╔══╝  ██╔══╝   ┃
┃██║     ██║██║  ██║██║  ██╗    ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║      ██║   ╚██████╔╝╚██████╔╝███████╗███████║    ██║     ██║  ██║███████╗███████╗ ┃
┃╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                       
                                                                  Press Enter
"""

menu = '''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                                                                                       ┃                   
┃██████╗ ██╗ █████╗ ██╗  ██╗    ███╗   ███╗██╗   ██╗██╗  ████████╗██╗   ████████╗ ██████╗  ██████╗ ██╗     ███████╗    ███████╗██████╗ ███████╗███████╗ ┃
┃██╔══██╗██║██╔══██╗██║ ██╔╝    ████╗ ████║██║   ██║██║  ╚══██╔══╝██║   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝    ██╔════╝██╔══██╗██╔════╝██╔════╝ ┃
┃██████╔╝██║███████║█████╔╝     ██╔████╔██║██║   ██║██║     ██║   ██║█████╗██║   ██║   ██║██║   ██║██║     ███████╗    █████╗  ██████╔╝█████╗  █████╗   ┃
┃██╔═══╝ ██║██╔══██║██╔═██╗     ██║╚██╔╝██║██║   ██║██║     ██║   ██║╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║    ██╔══╝  ██╔══██╗██╔══╝  ██╔══╝   ┃
┃██║     ██║██║  ██║██║  ██╗    ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║      ██║   ╚██████╔╝╚██████╔╝███████╗███████║    ██║     ██║  ██║███████╗███████╗ ┃
┃╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ┃
┃                                                                                                                                                       ┃
┃                                                                                                                                                       ┃ 
┃                                     Made by _piak_ in 2025 for Piak's Project Discord server!                                                         ┃
┃                         + ────────────────────────────────────────────────────────────────────────────────────────────────────── +                    ┃
┃                         ║  (1) TOKEN AUTO LOGIN  X  (6) TOKEN DMALL   X   (11) DELETE WEBHOOK            (16) SERVER CLONER   X  ║                    ┃
┃                         ║  (2) TOKEN NUKER       X  (7) TOKEN LEAVER  X   (12) SPAM WEBHOOK              (17) SERVER NUKER V2 X  ║                    ┃
┃                         ║  (3) TOKEN INFO           (8) TOKEN JOINER  X   (13) CREATE WEBHOOKS           (18) SERVER MASSDM   X  ║                    ┃
┃                         ║  (4) TOKEN GENERATOR   X  (9) TOKEN GRABBER X   (14) CREATE + SPAM WEBHOOKS X  (19) TIKTOK VIEWS    X  ║                    ┃
┃                         ║  (5) TOKEN CHECKER        (10) WEBHOOK INFO     (15) CHECK WEBHOOK    X        (20) SPOTIFY PREMIUM X  ║                    ┃
┃                         + ────────────────────────────────────────────────────────────────────────────────────────────────────── +                    ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

'''

def main():
    os.system("cls")
    set_console_fullscreen()
    while True:
        os.system("cls")
        Anime.Fade(Center.Center(intro), Colors.blue_to_red, Colorate.Vertical, interval=0.045, enter=True)
        os.system("cls")
        print(Colorate.Horizontal(Colors.yellow_to_red, menu))
        choice = input(Colorate.Horizontal(Colors.yellow_to_red, "Enter your choice >> ")).strip()

        if choice == "1":
            cls()
            premium()
        elif choice == "2":
            cls()
            premium()
        elif choice == "3":
            cls()
            execute_script("token_info.py")
        elif choice == "4":
            cls()
            premium()
        elif choice == "5":
            cls()
            execute_script("token_checker.py")
        elif choice == "6":
            cls()
            premium()
        elif choice == "7":
            cls()
            premium()
        elif choice == "8":
            cls()
            premium()
        elif choice == "9":
            cls()
            premium()
        elif choice == "10":
            cls()
            execute_script("webhook_info.py")
        elif choice == "11":
            cls()
            execute_script("webhook_deleter.py")
        elif choice == "12":
            cls()
            execute_script("webhook_spammer.py")
        elif choice == "13":
            cls()
            execute_script("webhook_creator.py")
        elif choice == "14":
            cls()
            premium()
        elif choice == "15":
            cls()
            premium()
        elif choice == "16":
            cls()
            premium()
        elif choice == "17":
            cls()
            premium()
        elif choice == "18":
            cls()
            premium()
        elif choice == "19":
            cls()
            premium()
        elif choice == "20":
            cls()
            premium()
        elif choice == "21":
            cls()
            premium()
        elif choice == "22":
            cls()
            premium()
        elif choice == "23":
            cls()
            execute_script("proxy_scraper.py")
        elif choice == "24":
            cls()
            execute_script("hypesquad.py")
        elif choice == "25":
            cls()
            premium()
        elif choice == "0":
            import sys
            sys.exit()
        else:
            cls()
            print(Colorate.Horizontal(Colors.red_to_yellow, "Invalid choice, please try again."))

if __name__ == "__main__":
    main()
    