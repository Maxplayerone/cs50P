import sys
import csv

def main():
    if len(sys.argv) > 2:
        scourgify(sys.argv[1], sys.argv[2])
    else:
        print("You should give two CLAs")
        sys.exit()

def scourgify(filename, destination):

    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print("File could not be found")
        sys.exit()
    else:
        reader = csv.DictReader(f)
        csv_rows = []
        for row in reader:
            csv_rows.append(row)

    #rows from a csv file that has first and last name
    #and not only name
    new_rows = []

    for row in csv_rows:
        #to-do: split the name key into first and last name\
        name_split = row["name"].split(",")
        new_rows.append( {"first name": name_split[1], "last name": name_split[0], "house": row["house"]} )

    with open(destination, "w") as f:
        writer = csv.writer(f)
        writer.writerow( ["First name", "last name", "house"] )

        for row in new_rows:
            writer.writerow([row["first name"], row["last name"], row["house"]])


if __name__ == "__main__":
    main()