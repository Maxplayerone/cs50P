import emoji

def main():
    answer = input("Input: ")
    emojize(answer)

def emojize(answer):
    if("_" in answer):
        print(emoji.emojize(answer))
    else:
        print(emoji.emojize(answer, language='alias'))


if __name__ == "__main__":
    main()