from datetime import date
import re

def main():
    print( get_difference_between_dates( input("When were you born (YYYY-MM-DD)? " )) )

def get_difference_between_dates(s):
   birth_date = get_dates_object_types(s)
   current_date = date.today()

   delta = current_date - birth_date
   return (f"Difference is {delta.days} days")

def get_dates_object_types(s):
    if re.search(r"^(?:[2][0][0-1][0-9]|[0-1][0-9][0-9][0-9]|[2][0][2][0-2])-(?:[0][0-9]|10|11|12)-(?:[0-2][0-9]|30|31)", s):
        birth_date =  date.fromisoformat(s)
        return birth_date

if __name__ == "__main__":
    main()