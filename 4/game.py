import sys

def main():
    guessing_number_game()

def get_int(message):
    try:
        response = int(input(message))
    except ValueError as e:
        print("You should type an unsigned integer instead of " + str(e))
        sys.exit()

    return response

def guessing_number_game():
    level = 0
    while level <= 0:
        level = get_int("What level do you want to pick? ")

    response = -1
    guess_count = 0

    while response != level:
        response = get_int("Guess: ")
        guess_count = guess_count + 1

        if(response > level):
            print("Too big!")
        elif(response < level):
            print("Too low!")

    print("The number was " + str(level) + " and it took you " + str(guess_count) + " to get it")

if __name__ == "__main__":
    main()