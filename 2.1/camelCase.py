import sys

def Snakify(word):
    word_len = len(word)
    new_word = ''
    for i in range(word_len):
        #the character we looking at is upppercase
        #we are ignoring the situation in which the first
        #character is uppercase
        if(word[i].isupper() and i != 0):
            new_word = new_word + "_" + word[i].lower()
        else:
            new_word = new_word + word[i]
        
    return new_word

def main():
    cmd_len = len(sys.argv)
    if cmd_len > 2:
        print("You should only give one argument")
    elif cmd_len == 1:
        print("You should give an arugment")
    else:
        snake_case = Snakify(sys.argv[1])

    print(snake_case)
    

if __name__ == "__main__":
    main()