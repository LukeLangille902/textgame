#This is a sample game that uses the ask() function from the textgame module

from luke_adventure_game_module import ask

def start():
    print("It was a dark and stormy night...")
    print("Brum was snoozing in her doghouse.")
    print("She wakes up to a bolt of lightning!")

    choice = ask("Go back to bed", "Get up and look around")
    
    if choice == 1:
        backtobed()
    elif choice == 2:
        lookaround()

def backtobed():
    print("You decide to go back to bed.")
    print("zzzzzZZZZZzzzzzz")
    print("The end.")

def lookaround():
    print("You decide to get up and have a look around.")
    print("What's that out there...")
    print("It's Ooma the Puma!")
    print("She brings party mix!")
    print("The end.")

start()

