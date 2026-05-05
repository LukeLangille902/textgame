#This is a sample game that uses the ask() function from the textgame module

from textgame import ask

def start():
    print("You are hiking through the forest deep within Kejimkujik National")
    print("Park, with no other hikers around. You hear a crash behind you and")
    print("spin around, just in time to see a shadowy figure flying through")
    print("the sky, off towards the lake. You can't believe your eyes!")

    choice = ask("Continue on the hike... Must have been my eyes playing tricks on me", "Chase the flying figure towards the lake")
    
    if choice == 1:
        continue_hike()
    elif choice == 2:
        chase_figure()

def continue_hike():
    print("Hmm... strange! Must've been the wind. You decide to keep going on")
    print("your hike. After a few minutes, you approach a fork in the path.")
    print("A sign says: Go left for the haunted forest, go right for the")
    print("uncrossable canyon.")

    choice = ask("Go left", "Go right")

    if choice == 1:
        go_left()
    elif choice == 2:
        go_right()

def go_left():
    print("You decide to go left for the haunted forest. How bad could it be?")
    print("As you approach, things start getting spooky! You're not ready for this!")
    print("You turn around and run back in the direction of home!")
    print("THE END")

def go_right():
    print("You decide to attempt to cross the uncrossable canyon. It's about")
    print("20 metres wide! You take a running start and leap for the other side...")
    print("But come up short by about 19 metres. Good thing you packed your")
    print("emergency parachute!")
    print("THE END")

def chase_figure():
    print("You turn and chase the flying figure towards the lake. You can't")
    print("help but wonder what it was! When you reach the lake, there is")
    print("nothing around. But now you're lost! There's a trail leading...")
    print("somewhere. There's also a canoe in the lake.")

    choice = ask("Follow the trail", "Paddle in the canoe")

    if choice == 1:
        follow_trail()
    elif choice == 2:
        paddle()

def follow_trail():
    print("You decide to follow the trail, hoping it will lead back home.")
    print("After hiking for 12 km, you come across a sign that reads: this is")
    print("the farthest point inside Kejimkujik National Park. Park exit is")
    print("in the other direction. Oops.")
    print("THE END")

def paddle():
    print("You hop in the canoe, and you use the sun to point yourself in the")
    print("direction you're pretty sure the park entrance is. You paddle for")
    print("three hours, but then you finally come across the park entrance and")
    print("visitor centre. The park staff are happy you're okay, but concerned")
    print("that you've taken someone else's canoe without telling them. You")
    print("apologize profusely.")
    print("THE END")

start()

