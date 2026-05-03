#textgame - Luke's Adventure Game Module
#Last updated May 3rd, 2026
#haha I am still learning how git works

def ask(*options):
    print("")
    print("==========")
    print("")

    #Prompt the player
    print("What will you do?")

    #Set up a counting variable, will be used to number the options
    i = 1

    #Display each of the options the programmer has included as arguments, each with an associated number
    for option in options:
        print(str(i), ") ", option)
        i += 1

    print("")
    print("==========")
    print("")

    #Now it's time to prompt the player for their choice, and then attempt to decipher their input.
    #This code will do its best to make a decision based on what the player has entered.
    #If all else fails, it will prompt the player to enter their choice again.

    #Set up a boolean variable to determine later if the player's input has been deciphered yet.
    question_resolved_flag = False

    while question_resolved_flag == False:
        #Ask the player for their choice, and record their input
        print("Write your choice below, then press ENTER:")
        input_choice = input("/> ")
        
        #Check if the player has entered an integer
        try:
            int(input_choice)
        
        #If the player has not entered an integer, follow these instructions:
        except ValueError:
            print("")
            print("==========")
            print("")

            #Reset the counting variable
            i = 1
            
            #Check if the text the player enters matches OR is a part of any of the valid options
            for option in options:
                if str.lower(input_choice) in str.lower(option):
                    #Return the number associated with the player's choice, ending the function call.
                    return i
                
                else:
                    i = i + 1

                    #Check if we have not run out of valid options
                    if i > len(options):
                        print("ERROR: Invalid Input. Please try again.")

        #If the player has entered an integer, follow these instructions:
        else:
            if int(input_choice) > len(options):
                print("ERROR: Invalid Input. Please try again.")

            else:
                print(options[int(input_choice) - 1])

                print("")
                print("==========")
                print("")

                #Return the number associated with the player's choice, ending the function call.
                return(int(input_choice))