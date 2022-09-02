from multiprocessing.sharedctypes import Value
import sys

def main():
    if(len(sys.argv) > 1):
        print_fuel_gauge(sys.argv[1])
    else:
        print("You should give a command line argument")

def print_fuel_gauge(user_input):
    answer = input(user_input + " ")
    #the input from the user after we check that it
    #has only integers except the "/" character
    formated_input = ''

    for i in range(len(answer)):
        char = answer[i]
        #dealing with this thingy first
        if(char == '/'):
            formated_input = formated_input + char
            continue

        try:
            #check if char can be an int
            #but don't change it
            int(char)
        except ValueError:
            print("You should give a number because " +  char + " is not it")
            return
        else:
            formated_input = formated_input + char

    #computing the number
    num1 = int(formated_input[0]) 
    num2 = int(formated_input[2:])

    if num2 < num1:
        print("The first number should be bigger than the second")
        return
    try:
        fuel_gauge = num1 / num2 * 100
    except ZeroDivisionError:
        print("You can't divide by zero you dummy")
        return
    else:
        if(fuel_gauge == 100):
            print("Fuel gauge: F")
        elif fuel_gauge <= 10:
            print("Fuel gauge E")
        else:
            print("Fuel gauge " + str(fuel_gauge) + "%")



if __name__ == "__main__":
    main()