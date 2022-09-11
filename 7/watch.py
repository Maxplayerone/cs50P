import sys
import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if result := re.search(r"^https?://(?:www.)?youtube.com/embed/([a-zA-Z0-9]+)", s):
        return f"https://youtu.be/{result[1]}"
    else:
        return None


if __name__ == "__main__":
    main()