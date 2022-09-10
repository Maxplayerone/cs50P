import sys

def main():
    if len(sys.argv) > 1:
        line_count = count_lines(sys.argv[1])
        print(f"The file {sys.argv[1]} has {line_count} lines")
    else:
        print("You should provide a cla for a file you want to check")
        sys.exit()

def count_lines(filename):
    line_count = 0

    if (".py" in filename) == False:
        print("The program only expects .py files")
        return -1

    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print("The filename you specified does not exist")
        return -1
    else:
        for line in file:
            line = line.strip()
            if line == "" or line[0] == "#":
                continue

            line_count = line_count + 1
        file.close()

    return line_count


if __name__ == "__main__":
    main()
