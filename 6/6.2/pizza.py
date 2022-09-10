from email import header
from tabulate import tabulate
import csv

def main():
    response = input("What .csv file do you want to tabulate? ")
    prettify(response)

def prettify(filename):
    try:
        f = open(f"6.2/{filename}", "r")
    except FileNotFoundError:
        print("File could not be found")
        return -1
    else:
        reader = csv.DictReader(f)
        csv_list = []
        for row in reader:
            csv_list.append(row)

        print( tabulate(csv_list[1:], headers=csv_list[0]) )

if __name__ == "__main__":
    main()