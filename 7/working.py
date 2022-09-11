import re

def main():
    print( convert( input("Hours: ") ) )

def convert(s):
    parsed_string = ( re.search(r"^(([0-9]|[1][0-2])(?::[0-5][0-9]|60)? (?:AM|PM) to ([0-9]|[1][0-2])(?::[0-5][0-9]|60)? (?:AM|PM))$", s) )
    try:
        result = parsed_string[1]
    except TypeError:
        print("The value of hour cannot be more than 12!")
        return None
    
    first_hour = parsed_string[2]
    second_hour = parsed_string[3]
    converted_string = ""

    #the user typed time with minutes
    if result.find(":") > 0:
        converted_string = result
    #the user typed only hours
    else:
        num_of_iterations = 0
        indexes_with_number = []
        for char in result:
            num_of_iterations = num_of_iterations + 1
            if char.isdigit():
                #if the next character is also a number we skip
                #(that must mean we have a double digit character)
                if result[num_of_iterations].isdigit():
                    continue
                else:
                    indexes_with_number.append(num_of_iterations)

        #adds minutes to strings that have whole hours
        
        converted_string = result[:indexes_with_number[0]] + ":00" + result[indexes_with_number[0]:indexes_with_number[1]] + ":00" + result[indexes_with_number[1]:]

    #changes to 24-hour based clock
    converted_string = re.sub(f"to {second_hour}", f"to {int(second_hour) + 12}",converted_string)

    #deteles AM and PM
    converted_string = converted_string.replace(" AM", "")
    converted_string = converted_string.replace(" PM", "").strip()
    return converted_string

if __name__ == "__main__":
    main()