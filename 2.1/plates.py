def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #no periods, spaces, or punctiuation marks
    #numbers after characters
    #min 2 or max 6 characters
    disalowed = [" ", "!", "?", ",", "."]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] 

    word_len = len(s)
    #if we have any number is s
    #this bool will flag use that we can't
    #have any letters now
    started_numbers = False

    if(word_len < 2 or word_len > 6):
        return False
    else:
        for i in range(len(s)):
            char = s[i]
            if(char in disalowed): return False
            #we have a letter after a number
            elif(char not in numbers and started_numbers): return False 
            elif (char in numbers): started_numbers = True
    return True

if __name__ == "__main__":
    main()