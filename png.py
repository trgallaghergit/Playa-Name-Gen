# Developer: Tim Gallagher
# Date: TBA
# Subject:
# Program Name: Playa Name Generator

# imported modules
import time
import random
import os
import sys

# joined_lower for functions, methods, attributes, variables

# joined_lower or ALL_CAPS for constants

# StudlyCaps for classes

# camelCase only to conform to pre-existing conventions

# Plan>>>
# Create Random Name Generator with multiple questions.
# Will take in multiple choice inputs from user
# Will gernrate a random names from a list.
# Present name to User.
# algorithem = Name / data type / starting value


# intro with User input - enters name -  intro (varable) GETS the value of user input
# algorithem = Name / data type / starting value

def intro():
    print('Welcome to the Playa Name Generator. I\'m here to provide '
          'you with your Burning Man Playa Name.')
    time.sleep(0.25)
    # User input - enters name -  name (varable) GETS the value of user input
    # algorithem = Name / data type / starting value


intro()


def name():
    name = input(
        "If you would like a Playa Name, please type in your first name now: ")

    # print("Well Hellow " + name + ". Welcome!") Concatenate string
    # print("Well Hellow {}. Welcome!".format(name)) # string interpolation using format method
    print(f"Well Hellow {name}. Welcome!")  # f-string method


name()
time.sleep(2.0)

print('I\'m going to be asking you some questions to help determine the best Playa name for you.')
time.sleep(2.0)

input("When your ready, please hit the Enter to begin...")
time.sleep(.75)

# Program Functions
def bio_type():  # Multiple choice questions 1
    print('Do you consider yourself:\n\n1) Human\n2) Alien\n')

    choice = input("Enter 1 or 2 now: ")
    if choice == '1':
        print("Hello Human being...")

    elif choice == '2':
        print("Looks like someone took something rather visual.... nano nano")

    else:
        choice = input("Enter 1 or 2 now: ")


bio_type()
time.sleep(2.0)
'''
 
def bio_type():    
    choice = ""
    bio_type_options = ["1", "2"]   

    # used "not in" so that no other input besides 1 or 2 could be used.
    while choice not in bio_type_options:
        print('Do you consider yourself:\n\n1) Human\n2) Alien\n')

        choice = input("Enter 1 or 2 now: ")
        if choice == bio_type_options[0]:
            print("Hello Human being...")

        elif choice == bio_type_options[1]:
            print("Looks like someone took something rather visual.... nano nano")


bio_type()

'''
def spirit_animal():  # Multiple choice question 2
    animal_options = ["1", "2", "3", "4", "5"]
    choice = ""

    while choice not in animal_options:
        print('What is your spirit animal?\n\n1) Cat\n2) Dog\n3) Honey Badge\n4) '
              'Unicorn\n5) My Pretty Pony\n\n ')

        choice = input("Enter 1, 2, 3, 4, or 5 now: ")
        if choice == animal_options[0]:   # left out the elses statement
            print("Meeoooooow!")

        elif choice == animal_options[1]:
            print("So if possible, you would lick your own crotch. Nice!.")

        elif choice == animal_options[2]:
            print("So fierce aren't you!")
            time.sleep(1.0)
            print("Honey Badger don't give a shit.")

        elif choice == animal_options[3]:
            print("sigh..... Sooooo overdone")

        elif choice == animal_options[4]:
            print("So you're telling me that you're into Pony Play..... REALLY?!")
            time.sleep(1.0)
            print("So Kinky. Love it.")


spirit_animal()
time.sleep(2.0)

'''
def spirit_animal():  # PNG Function 4 -  Multiple choice question

    print('What is your spirit animal?\n\n1) Cat\n2) Dog\n3) Honey Badge\n4) '
          'Unicorn\n5) My Pretty Pony\n\n ')

    choice= input("Enter 1, 2, 3, 4, or 5 now: ")

    if choice== '1':   # left out the elses statement
        print("Meeoooooow!")

    elif choice== '2':
        print("So if possible, you would lick your own crotch. Nice!.")

    elif choice== '3':
        print("So fierce aren't you!")
        time.sleep(1.0)
        print("Honey Badger don't give a shit.")

    elif choice== '4':
        print("sigh..... Sooooo overdone")

    elif choice== '5':
        print("So you're telling me that you're into Pony Play..... REALLY?!")
        time.sleep(1.0)
        print("So Kinky. Love it.")

    else:
        choice= input("Enter 1, 2, 3, 4, or 5 now: ")


spirit_animal()
'''

def input_joke():  # Multiple choice question 3

    input("Please hit Enter to continue...")
    time.sleep(.75)
    # is using var OK?
    var = 5  # used a while loop becouse I can determine the number of times variable repeats
    while var > 0:
        var -= 1
        var, time.sleep(1.0)
        print("ERROR")
    time.sleep(2.0)

# does these print/inputs really need to be part of this function?
    print("What did you do {}?".format(name))
    time.sleep(2.0)
    print('Did you hit the wrong key?')
    time.sleep(3.0)
    input("To resolve this System Error... Please Hit the Enter Key to the allow the system to reboot.")
    time.sleep(2)
    print("HAHA... Just messing with you {}".format(name))


input_joke()
time.sleep(2.0)


def flurting_robot():  # Multiple choice question 4

    single_options = ["1", "2", "3"]
    single = ""

    while single not in single_options:
        print("Are you single?\n\n 1) Yes\n 2) No\n 3) Maybe\n\n")
        time.sleep(.50)
        single = input("Please enter 1, 2, or 3 now: ")
        if single == single_options[0]:
            print(
                "REALLLLLLLLY?! By the way... I sure love what you're wearing. Wink, Wink..")
            time.sleep(2.0)

        elif single == single_options[1]:
            print(
                "Did you know that dating robots can be very stimulating... just saying!")

        elif single == single_options[2]:
            print("So you're saying there's a chance?!")
            time.sleep(1.0)
            print("We'll check in on this later")


flurting_robot()
time.sleep(2.0)


def pgn_compiling():
    print("Now that I'm done asking you questions, It's time for your New Playa Name. ")
    time.sleep(.75)
    input("Please Hit the Enter Key to continue")

    var = "Compiling"  # trying out a for loop with time.sleep
    for index in range(7):
        var, time.sleep(1)
        print(var)
    time.sleep(2)

    # is there a better way to write this? For loop with some timer option?
    time.sleep(.50)
    input("Hit Enter to see your new Playa Name")
    time.sleep(1.5)
    print("wait for it".upper())
    time.sleep(1.75)
    print("wait for it!".upper())
    time.sleep(2.0)
    print("wait for it!!".upper())
    time.sleep(2.25)
    print("wait for it!!!".upper())
    time.sleep(2.5)


pgn_compiling()


# Randon Name Gen - two lists, one name from each list picked randomly to create name - random.choice()method

def random_gen():

    first = [
        "Slappy", "Pussy", "Sexy", "Shitting", "Twinkle", "Vegan", "Titty", "Sizzle",
        "Sassy", "Heine", "Shitty", "Kissing", "Dripping", "Smelly", "Drunken",
        "Cramping", "Gummy", "Yummy", "Poopy", "Masked", "Horse", "Sparkel", "Bisexual",
        "Tripod", "Messy", "Little"
    ]
    second = [
        "scrotum", "Vegan", "Man", "Horse", "Goblin", "Sperm Doner", "Killer",
        "Butt cheeks", "Pony", "Dick Licker", "Titties", "Heine", "kitten", "Woman",
        "Shirt Cocker", "Stalker", "Foreskins", "Cock", "Two Balls", "lickel's",
        "Nut Sack", "Sparkels"
    ]

    new_playa_name = (random.choice(first) + " " + random.choice(second))

    # building suspence
    print('From this day forward...')
    time.sleep(2.0)
    print('You will be known as....')
    time.sleep(2.0)
    print(new_playa_name.title())
    time.sleep(3.0)

    message = "Thank you and have a great day"
    print("{} {}".format(message, new_playa_name))
    #print("Thank you and have a great day" + new_playa_name)


random_gen()

print("Good Bye")


'''
    first_name = random.choice(first)
    second_name = random.choice(second)
    new_playa_name = (first_name + " " + second_name)
    # str = "Your New Playa Name is: " + new_playa_name
    # print(str.upper())
    time.sleep(3.0)
    print("Thank you and have a great day " + new_playa_name + ".")


'''
