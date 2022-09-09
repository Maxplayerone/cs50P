import sys

def main():
    if len( sys.argv) < 2:
        print("You should give a cla")
        sys.exit()

    get_value(sys.argv[1])

def get_value(str):
    if str == "hello":
        return 100
    elif str[0] == "h":
        return 20
    else:
        return 0 

if __name__ == "__main__":
    main()