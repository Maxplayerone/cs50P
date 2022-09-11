import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if result := re.search(r"^([1-2][1-5][1-5]|[1-9][1-9]|[1-9]|[1][0-9][0-9])\.([1-2][1-5][1-5]|[1-9][1-9]|[1-9]|[1][0-9][0-9])\.([1-2][1-5][1-5]|[1-9][1-9]|[1-9]|[1][0-9][0-9])\.([1-2][1-5][1-5]|[1-9][1-9]|[1-9]|[1][0-9][0-9])$", ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()