
def main():
    fruits = {
        "Apple" : 130,
        "Avocado" : 50,
        "Banana" : 110,
        "Cantaloupe" : 50,
        "Grapefruit" : 60,
        "Grapes" : 90,
        "Moneydew Melon" : 50,
        "Kiwifruit" : 90,
        "Lemon" : 15,
        "Lime" : 20,
        "Nectrarine" : 60,
        "Orange" : 80,
        "Peach" : 60,
        "Pear" : 100,
        "Pineapple" : 50,
        "Plums" : 50,
        "Strawberries" : 50,
        "Sweet cheries" : 100,
        "Tangerine" : 50,
        "Watermelon" : 80
    }

    user_input = input("What fruit are you looking for: ")
    if user_input in fruits:
       print(fruits[user_input])
    else:
        print("Could not find the thing you were looking for")

if __name__ == '__main__':
    main()