import sys
import emoji

class Jar:
    #add a variable called size which is max_size - deposits and withdraws

    def __init__(self, capacity=10):
        self.max_size = capacity
        self.current_size = 0

    def __str__(self):
        cookies = ''
        for _ in range( self.current_size ):
            cookies = cookies + emoji.emojize(":cookie:")

        return cookies

    def deposit(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            print("The amount must be an integer!")
            return
        else:
            if self._current_size + amount > self.max_size:
                print("You cannot deposit because of capacity overflow")
                return
            
            self.current_size = self.current_size + amount

    def withdraw(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            print("The amount must be an integer!")
            return
        else:
            if self._current_size - amount < 0:
                print("You cannot have less than zero cookies")
                return

            self.current_size = self.current_size - amount

    def capacity(self):
        return self.max_size

    def size(self):
        return self.current_size

    @property
    def max_size(self):
        return self._max_size

    @max_size.setter
    def max_size(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            return
            sys.exit()
        else:
            self._max_size = amount

    @property
    def current_size(self):
        return self._current_size
    
    @current_size.setter
    def current_size(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            return
            sys.exit()
        else:
            self._current_size = amount



def main():
    control_panel()

def control_panel():
    #we are sure that a jar object is created
    jar = Jar(input("Size "))

    while True:
        response = input("What to do you want to do (C/P/D/W/CS/S/Q)? ")
        if response == "C":
            jar = Jar(input("Size "))
        elif response == "P":
            print(jar)
        elif response == "D":
            jar.deposit( input("amount ") )
        elif response == "W":
            jar.withdraw( input("amount: ") )
        elif response == "CS":
            print(f"Current size  {jar.size()}")
        elif response == "S":
            print(f"Max size {jar.capacity()}") 
        elif response == "Q":
            return

if __name__ == "__main__":
    main()