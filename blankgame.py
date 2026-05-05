#Name of game:
#By:

from textgame import ask

def start():
    print("YOUR TEXT GOES HERE!")

    choice = ask("YOUR OPTION 1 GOES HERE!", "YOUR OPTION 2 GOES HERE!")
    
    if choice == 1:
        YOUR_OPTION_1_FUNCTION()
    elif choice == 2:
        YOUR_OPTION_2_FUNCTION()

start()

