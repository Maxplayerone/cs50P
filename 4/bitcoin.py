from textwrap import indent
import requests
import json
import sys

def main():
    try:
        num = float(input("How much money do you want to check? "))
    except ValueError:
        print("You should have typed a float value")
        sys.exit()

    get_bitcoin_value(num)

def get_bitcoin_value(multiplier):
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = (requests.get(url)).json()
    
    value = str(response["bpi"]["USD"]["rate"]).replace(",", "")
    float_value = float(value)
    print("$" + str(float_value * multiplier))

if __name__ == "__main__":
    main()