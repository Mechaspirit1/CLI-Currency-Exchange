#!/usr/bin/env python3
import requests

#modos diferentes do applicativo dependendo da necessidade
#printa todos os codigos monetarios e suas taxas de cambio relativas a moeda usada como base
def rate_list():
    base_currency = input("Currency to base exchange rates: ").upper()

    try:
        response = requests.get(f"https://open.er-api.com/v6/latest/{base_currency}")
        resParsed = response.json()

        for currency, rate in resParsed['rates'].items():
            print(f"{currency}: {round(rate, 2)}")

    except KeyError:
        print("Invalid currency code")
    except requests.RequestException:
        print("Network/API error")

#faz a conversão de uma quantia de dinheiro baseado nos codigos monetarios
def currency_exchange():
    primary_currency = input("Currency to be converted from: ").upper()
    secondary_currency = input("Currency to be converted to: ").upper()
    ammount = float(input("Value to be converted: "))

    try:
        response = requests.get(f"https://open.er-api.com/v6/latest/{primary_currency}")
        resParsed = response.json()
        rate = resParsed['rates'][secondary_currency]
        conversion = ammount*rate

        print(f"Current exhange rate: {secondary_currency}:{round(rate, 2)}")
        print(f"Value conversion: {secondary_currency}:{round(conversion, 2)}")

    except KeyError:
        print("Invalid currency code")
    except requests.RequestException:
        print("Network/API error")


banner = r"""
  ____ _   _ ____  _______  __
 / ___| | | |  _ \| ____\ \/ /
| |   | | | | |_) |  _|  \  /
| |___| |_| |  _ <| |___ /  \
 \____|\___/|_| \_\_____/_/\_\
"""

print(banner)
print("A CLI currency exchange tool by Pablo Loschi | Powered by the ExchangeRate-API")

while True:
    print("1-Print currency list and rates | 2-Convert between currencies | 3-Exit")

    try:
        start = int(input())

        if start == 1:
            rate_list()
            print("")
        elif start == 2:
            currency_exchange()
            print("")
        elif start == 3:
            break
        else:
            print("Invalid input !")

    except ValueError:
        print("Input only accepts numbers !\n")
        continue