
import requests
import json

def get_balance(address):
    url = f"https://blockchain.info/rawaddr/{address}"
    response = requests.get(url)
    data = response.json()
    return data["final_balance"]

with open("wallets.json") as f:
    wallets = json.load(f)

for w in wallets:
    balance = get_balance(w)
    print(f"{w} balance: {balance}")
