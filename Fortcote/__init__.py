from mcstatus import JavaServer
from javascript import require
from numba import prange
import threading, colorama, socket
from colorama import Fore, Back; colorama.init()
from random import randint



def finder():
    print(f'{Fore.LIGHTBLACK_EX}Started...{Fore.RESET}')
    for _ in prange(256256256256):
        ip=f'{randint(1,255)}.{randint(1,255)}.{randint(1,255)}.{randint(1,255)}'
        threading.Thread(target=parser, args=(ip,)).start()

def parser(ip):
    try:
        server = JavaServer.lookup(f"{ip}");status = server.status()
        print(f""" > {Fore.LIGHTBLACK_EX}IP: {Back.LIGHTRED_EX}{Fore.BLACK}{ip}{Fore.RESET}{Back.RESET}
 > {Fore.LIGHTBLACK_EX}Players{Fore.RESET}: {status.players.online} / {Fore.LIGHTRED_EX}{status.players.max}{Fore.RESET}
 > {Fore.LIGHTBLACK_EX}Version:{Fore.RESET} {status.version.name} ; {Fore.LIGHTRED_EX}{status.version.protocol}{Fore.RESET}
 > {Fore.LIGHTBLACK_EX}Ping{Fore.RESET}: {Fore.LIGHTRED_EX}{status.latency}{Fore.RESET}
 > {Fore.LIGHTBLACK_EX}Info{Fore.RESET}: {Fore.LIGHTRED_EX}{status.description}{Fore.RESET}
 {Fore.LIGHTBLACK_EX}-===================-{Fore.RESET}""")
        with open('IPs/IP.txt', 'a') as f:
            f.write(f'{ip}\n')
            f.close
        with open('IPs/IPFULL.txt', 'a') as f:
            f.write(f'IP: {ip} Players: {status.players.online} Version: {status.version.name} Ping: {status.latency} Info: {status.description} ALL: {status.raw}\n')
            f.close
    except:
        None

def TCP_connect(ip, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        output[port_number] = 'Listening'
    except:
        output[port_number] = ''

def scan_ports(host_ip, delay):
    threads = []
    output = {}
    print(f'{Fore.LIGHTBLACK_EX}Scan ip: {Fore.LIGHTRED_EX}{host_ip}{Fore.RESET}')
    print(f'{Fore.LIGHTBLACK_EX}Step {Fore.LIGHTRED_EX}1{Fore.LIGHTBLACK_EX}/3{Fore.RESET}')
    for i in prange(65535):
        t = threading.Thread(target=TCP_connect, args=(host_ip, i, delay, output))
        threads.append(t)
    print(f'{Fore.LIGHTBLACK_EX}Step {Fore.LIGHTRED_EX}2{Fore.LIGHTBLACK_EX}/3{Fore.RESET}')
    for i in prange(65535):
        threads[i].start()
    print(f'{Fore.LIGHTBLACK_EX}Step {Fore.LIGHTRED_EX}3{Fore.LIGHTBLACK_EX}/3{Fore.RESET}')
    for i in prange(65535):
        threads[i].join()
    print(f'{Fore.LIGHTBLACK_EX}Wait...{Fore.RESET}')
    for i in prange(65535):
        if output[i] == 'Listening':
            try:
                server = JavaServer.lookup(f"{host_ip}:{i}")
                status = server.status()
                print(f"{Fore.LIGHTBLACK_EX}{host_ip}:{Fore.RESET}{Fore.LIGHTRED_EX}{i}{Fore.RESET} | {Fore.LIGHTBLACK_EX}Players on server{Fore.RESET}: {Fore.LIGHTRED_EX}{0}{Fore.RESET}".format(status.players.online))
                with open('Ips/IP_PORTS.txt', 'a') as f:
                    f.write(f'{host_ip}:{i}\n')
                    f.close
            except:
                continue

def port():
    with open('IPs/IP.txt') as f:
       for line in f:
            host_ip = line.rstrip('\r\n')
            delay=int(10)
            scan_ports(host_ip, delay)
            continue