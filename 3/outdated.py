
def main():
    convert_date()

def convert_date():
    date = input("Type a date: " )
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    day = ""
    month = ""
    year = ""

    try:
        random = int(date[0])
    except ValueError:
        #if the user typed the month with letters
        formated = date.split(" ")
        for i in range(len(months)):
            if(str(formated[0]) == str(months[i])):
                month = str(i + 1)
                break
        
        day = formated[1].replace(",", "")
        year = formated[2]
    else:
        #if the user typed the month with numbers
        sliced_date = date.replace(" ", "")
        sliced_date = sliced_date.split("/")
        day = sliced_date[1]
        month = sliced_date[0]
        year = sliced_date[2]

    if int(day) > 31:
        print("Days cannot be bigger than 31")
        return
    elif int(day) < 10:
        day = "0" + day

    if int(month) > 12:
        print("There are no more than 12 months!")
        return
    elif int(month) < 10:
        month = "0" + month
    
    print(year + "/" + month + "/" + day)

if __name__ == "__main__":
    main()