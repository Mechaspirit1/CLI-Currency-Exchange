#!/usr/bin/env python3
import requests

#retorna a lista de codigos monetarios baseados na moeda base
def rate_list(base_currency):
    response = requests.get(f"https://open.er-api.com/v6/latest/{base_currency}")
    resParsed = response.json()
    currency_list = ''

    for currency, rate in resParsed['rates'].items():
        currency_list+=(f"{currency}: {round(rate, 2)}" + "\n")

    return currency_list

#converte uma quantia de uma moeda para outra, arredonda os decimais e retorna o resultado
def currency_exchange(primary_currency, secondary_currency, amount):
    response = requests.get(f"https://open.er-api.com/v6/latest/{primary_currency}")
    resParsed = response.json()
    rate = resParsed['rates'][secondary_currency]
    conversion = amount*rate

    return(round(conversion, 2))

def main():
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
                try:
                    base = input("Currency to base exchange rates: ").upper()
                    print(rate_list(base))
                except KeyError:
                    print("Invalid currency code")
                except requests.RequestException:
                    print("Network/API error")

            elif start == 2:
                try:
                    base = input("Currency to base exchange rates: ").upper()
                    sec_base = input("Coversion currency: ").upper()
                    amount = int(input("Ammount to be converted: "))

                    print(f"{sec_base} {currency_exchange(base, sec_base, amount)}")
                except KeyError:
                    print("Invalid currency code")
                except requests.RequestException:
                    print("Network/API error")

            elif start == 3:
                break

            else:
                print("Invalid input !")

        except ValueError:
            print("Input only accepts numbers !\n")
            continue

if __name__ == "__main__":
    main()
