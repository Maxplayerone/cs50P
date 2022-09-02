
from itertools import product


def main():
    shop_at_toqueria()

def shop_at_toqueria():
    products = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    #the total amount of money the user spend
    total_amount = 0.0
    while True:    
        answer = input("Item: ")
        if answer in products:
            print(f"Total: ${total_amount + products[answer]}")
        elif answer.lower() == "quit":
            return 



if __name__ == "__main__":
    main()