from pyfiglet import Figlet
import random

def main():
    choice = input("Do you want to have a random font (0)? ")
    sentence = input("Choose a sentece: ")

    render_font(choice, sentence)

def render_font(choice, sentence):
    if(choice != "0"):
        font = Figlet(font=choice)
    else:
        fonts = [
        "3-d", "3x5", "5lineoblique", "slant",
        "5lineoblique","alphabet", "banner3-D",
        "doh", "isometric1", "letters",
        "alligator", "bubble"
        ]

        rand_font_index = random.randint(0, len(fonts))
        font = Figlet(font = fonts[rand_font_index])

        print(font.renderText(sentence)) 
        
if __name__ == "__main__":
    main()