
def main():
    #the initial amount of cash the user needs to pay
    max_amount = 50

    while(max_amount > 0):
        print("amount due: ", max_amount)
        answer = (int)(input("Insert coin: "))
        max_amount = max_amount - answer

    if(max_amount < 0):
        print("Change owed: ", max_amount * -1)
    else:
        print("You have paid pefectly! Congratulations")

if __name__ == "__main__":
    main()