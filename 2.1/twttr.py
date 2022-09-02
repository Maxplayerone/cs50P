
def twttrify(input):
    vowels = ["a", "e", "i", "o", "u", "y"]
    output = ''

    for i in range(len(input)):
        char = input[i]

        if(char.lower() in vowels):
            pass
        else:
            output = output + char
    
    print("output: ", output)

def main():
    user_input = input("Sentence please: ")
    twttrify(user_input)

if __name__ == '__main__':
    main()