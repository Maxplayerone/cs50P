import random
import sys

final_score = 0

def main():
    generate_math_problems()
    print("You've guessed " + final_score + " points correctly!")

def generate_math_problems():
    digit_count = get_digit_count()

    for i in range(10):
        generate_question(digit_count)

#get number from 1 to 3 from the user
def get_digit_count():
    try:
        response = int(input("Level: "))
    except ValueError as e:
        print("You should type an unsigned integer instead of " + str(e))
        sys.exit()
    
    if response > 3 or response < 1:
        print("The level should not be higher than 3 or lower than 1")
        sys.exit()

    return response

#generates a math problem with the digit count specified by the user
def generate_question(digit_count):
    range_start = 10**(digit_count-1)
    range_end = (10**digit_count)-1

    num1 = random.randint(range_start, range_end)
    num2 = random.randint(range_start, range_end)

    try:
        answer = int(input(f"{num1} + {num2}: "))
    except ValueError:
        print("EEE")
        return

    if answer == num1 + num2:
        print("That was correct!")
        final_score = final_score + 1
    else:
        print("EEE")

if __name__ == "__main__":
    main()