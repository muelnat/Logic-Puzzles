from random import randint

def montyHalloween():
    faveCandy = input("What is your favorite candy?")
    faveCandy = faveCandy.strip()
    candyDoorNum = randint(1,3)
    doorList = [1, 2, 3]
    guess = int(input("You are trick-or-treating and approach 3 doors, numbered 1, 2, and 3.\n" +
                      "Behind one door lives a neighbor who will give you {}, while the other two will give you rocks.\n".format(faveCandy) +
                      "Which door would you like to choose?"))
    while guess not in [1, 2, 3]:
        guess = int(input("Please choose a valid door."))
    doorList.remove(guess)
    
    incorrectDoorOpened = False
    openedDoor = 0
    while incorrectDoorOpened == False:
        openedDoor = randint(1,4)
        if openedDoor != guess and openedDoor != candyDoorNum:
            incorrectDoorOpened = True
    doorList.remove(openedDoor)
    switch = input("Your friend chose Door {}, which gave him rocks. Would you like to switch doors?".format(openedDoor))
    switch = switch.lower()
    switch = switch.strip()
    ##Remove all punctuation from the input??
    counter = 0
    while switch not in ["yes", "y", "yeah", "yep", "yas", "yea", "no", "n", "nope"]:
        if counter == 3:
            switch = input("This is just a simple yes or no question.")
        elif counter == 4:
            switch = input("C'mon, work with me please.")
        elif counter == 5:
            switch = input("Please?")
        elif counter == 6:
            switch = input("Fine. I see how it is.")
        elif counter == 7:
            switch = input("Why don't you want to play with me?")
        elif counter == 8:
            switch = input("I worked hard on this, you know.")
        elif counter == 9:
            switch = input("Alright, that's it. You asked for it.")
        elif counter == 10:
            switch = input("This is your final warning.")
        elif counter == 11:
            print("Fine.\n\nGAME OVER\nPlease come back when you feel like cooperating.\n\nYou obtained a rock.")
            return None
        else:
            switch = input("Please enter yes or no.")
        counter += 1
    if switch in ["yes", "y", "yeah", "yep", "yas", "yea"]:
        guess = doorList[0]

    print("You decided to open Door {} and obtained...".format(guess))
    if guess == candyDoorNum:
        print("{}!! Congratulations! :)".format(faveCandy))
    else:
        print("a rock... The correct door was {}. Better luck next time.".format(candyDoorNum))

    tryagain = input("Would you like to try again?")
    tryagain.lower()
    tryagain.strip()
    if tryagain in ["yes", "y", "yeah", "yep", "yas", "yea"]:
        print("\n\n-------------------------------\n\n")
        montyHalloween()
    else:
        print("Thanks for playing!")
        return None
        
montyHalloween()
