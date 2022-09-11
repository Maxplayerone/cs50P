import re

def main():
    print( count( input("Text: ") ) )

def count(s):
    return len( re.findall(r"([,. ]?um[,. ]|^um$)", s) )

if __name__ == "__main__":
    main()