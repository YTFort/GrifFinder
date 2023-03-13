from Fortcote import finder, port
from javascript import require, On
from nickname_generator import generate
import colorama, re
from colorama import Fore, Back; colorama.init()

mineflayer = require('mineflayer')



print(f'''{Fore.LIGHTBLACK_EX}
  ▄▀  █▄▄▄▄ ▄█{Fore.LIGHTRED_EX} ▄████  ▄████ {Fore.LIGHTBLACK_EX} ▄█    ▄   ██▄   ▄███▄   █▄▄▄▄ 
▄▀    █  ▄▀ ██{Fore.LIGHTRED_EX} █▀   ▀ █▀   ▀{Fore.LIGHTBLACK_EX} ██     █  █  █  █▀   ▀  █  ▄▀ 
█ ▀▄  █▀▀▌  ██{Fore.LIGHTRED_EX} █▀▀    █▀▀   {Fore.LIGHTBLACK_EX} ██ ██   █ █   █ ██▄▄    █▀▀▌  
█   █ █  █  ▐█{Fore.LIGHTRED_EX} █      █     {Fore.LIGHTBLACK_EX} ▐█ █ █  █ █  █  █▄   ▄▀ █  █  
 ███    █    ▐{Fore.LIGHTRED_EX}  █      █    {Fore.LIGHTBLACK_EX}  ▐ █  █ █ ███▀  ▀███▀     █   
       ▀      {Fore.LIGHTRED_EX}   ▀      ▀   {Fore.LIGHTBLACK_EX}    █   ██                ▀   
              {Fore.LIGHTBLACK_EX}Version: {Fore.LIGHTRED_EX}1.0 {Fore.RESET}| {Fore.LIGHTBLACK_EX}By {Fore.LIGHTRED_EX}Fortcote {Fore.RESET}  
''')

def startbot1(ip):
    try:
        bot = mineflayer.createBot({
          'host': f'{ip}',
          'port': 25565,
          'username': f'{generate("en")}'
        })
        @On(bot, "login")
        def login(this):
            print(f'{Fore.LIGHTBLACK_EX}{ip}{Fore.RESET} - {Fore.LIGHTGREEN_EX}Join{Fore.RESET}')
            with open('Ips/IP.txt', 'a') as f:
                f.write(f'{ip}\n')
                f.close
            bot.end()
        @On(bot, "error")
        def error(err, *a):
            print(f'{Fore.LIGHTBLACK_EX}{ip}{Fore.RESET} - {Fore.LIGHTRED_EX}Close{Fore.RESET}')
    except:
        print(f'{Fore.LIGHTBLACK_EX}{ip}{Fore.RESET} - {Fore.LIGHTRED_EX}Close{Fore.RESET}')

def startbot2(ip, port):
    try:
        bot = mineflayer.createBot({
          'host': f'{ip}',
          'port': int(port),
          'username': f'{generate("en")}'
        })
        @On(bot, "login")
        def login(this):
            print(f'{Fore.LIGHTBLACK_EX}{ip}:{port}{Fore.RESET} - {Fore.LIGHTGREEN_EX}Join{Fore.RESET}')
            with open('IPs/IP_PORTS.txt', 'a') as f:
                f.write(f'{ip}\n')
                f.close
            bot.end()
        @On(bot, "error")
        def error(err, *a):
            print(f'{Fore.LIGHTBLACK_EX}{ip}:{port}{Fore.RESET} - {Fore.LIGHTRED_EX}Close{Fore.RESET}')
    except:
        print(f'{Fore.LIGHTBLACK_EX}{ip}:{port}{Fore.RESET} - {Fore.LIGHTRED_EX}Close{Fore.RESET}')

def join():
    print(f'{Fore.LIGHTBLACK_EX}1 - IP\n2 - IP:PORT{Fore.RESET}')
    aa=input('> ')
    if aa == '1':
        with open('IPs/IP.txt') as f:
            for line in f:
                ip = line.rstrip('\r\n')
                startbot1(ip)
                continue
    elif aa == '2':
        with open('Ips/IP_PORTS.txt') as f:
            for line in f:
                ipp = line.rstrip('\r\n')
                ip, port = re.findall('([\d.]+)', ipp)
                startbot2(ip, port)
                continue
    else:
        print(f'{Fore.LIGHTRED_EX}Error{Fore.RESET}')



print(f'{Fore.LIGHTRED_EX}1{Fore.LIGHTBLACK_EX} - Finder\n{Fore.LIGHTRED_EX}2{Fore.LIGHTBLACK_EX} - Join\n{Fore.LIGHTRED_EX}3{Fore.LIGHTBLACK_EX} - Port scan{Fore.RESET}')
a=input('> ')
if a=='1':
    finder()
elif a=='2':
    join()
elif a=='3':
    port()
else:
    print(f'{Fore.LIGHTRED_EX}Error{Fore.RESET}')