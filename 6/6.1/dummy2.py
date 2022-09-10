def main():
    print( convert( input("What is your gauge? ")) )
def convert(user_input):
    formated_input = "" 
    has_backslash = False
    for i in range(len(user_input)):
        char = user_input[i]
        if(char == '/'):
            formated_input = formated_input + char
            has_backslash = True
            continue
        try:
            int(char)
        except ValueError:
            print("You should give a number because " +  char + " is not it")
            return "disalowed characters error"
        else:
            formated_input = formated_input + char
    if has_backslash == False:
            return "No backslash error"
    num1 = int(formated_input[0]) 
    num2 = int(formated_input[2:])
    if num2 < num1:
        print("The first number should be smaller than the second")
        return "value bigger than 1"
    try:
        fuel_gauge = num1 / num2 * 100
    except ZeroDivisionError:
        print("You can't divide by zero you dummy")
        return "division by zero error"
    else:
        if(fuel_gauge == 100):
            return "F"
        elif fuel_gauge <= 10:
            return "E"
        else:
            return f"{fuel_gauge}%"
if __name__ == "__main__":
    main()