from validator_collection import validators, checkers, errors
import re

def main():
    print( validate( input("What is your email address: ") ) )

def validate(s):
    try:
        result = validators.email(s)
    except errors.InvalidEmailError:
        return "Invalid"
    else:
        if re.search(f"^{result}$", result):
            return "Valid"
        else:
            return "Invalid"

if __name__ == "__main__":
    main()