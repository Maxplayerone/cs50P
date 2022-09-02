
def main():
    get_grocery_items()

def get_grocery_items():
    alphabet = ['A','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z''A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
    list_items = []

    while True:
        answer = input("Item: ").upper()
        list_items.append(answer)

        if answer.lower() == "quit":
            list_items.remove(list_items[-1])
            for char in alphabet:
                for item in list_items:
                    if item[0] == char:
                        print(item)
                        list_items.remove(item)
            
            return


if __name__ == "__main__":
    main()