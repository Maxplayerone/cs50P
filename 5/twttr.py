
def main():
    user_input = input("Sentence please: ")
    print( shorten(user_input) )

def shorten(input):
    vowels = ["a", "e", "i", "o", "u", "y"]
    output = ''

    for i in range(len(input)):
        char = input[i]

        if(char.lower() in vowels):
            pass
        else:
            output = output + char
    
    return output


if __name__ == '__main__':
    main()