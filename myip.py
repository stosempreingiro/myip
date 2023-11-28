#!/usr/bin/python3
import requests

def get_ip():
    sito="https://ipinfo.io/json"   #README: Thanks to "https://ipinfo.io/" to make this possible.
    response=requests.get(sito,verify=True)
    if response.status_code!=200:
        print(f"[!] Errore: Status code: {response.status_code}")
        exit()
    dati=response.json()
    return dati

try:
    dati=get_ip()
except requests.ConnectionError:
    print("[!] Errore: connessione fallita.")
    exit()

print(f"\n[+] IP: {dati['ip']}\n[+] City: {dati['city']}\n[+] Org: {dati['org']}")