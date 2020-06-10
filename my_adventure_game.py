import time
import random
weapon = []


def print_pause(message):
    print(message)
    time.sleep(1)


def intro():
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here,"
                "and has been terrifying the nearby village....")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                "(but not very effective) dagger.\n\n")


def house():
    print_pause("You approach the door of the house")
    print_pause("You are about to knock when the door opens"
                f"and out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")
    print_pause("You feel a bit under-prepared for this,"
                "what with only having a tiny dagger.")
    option1 = input("Would you like to (1) fight or (2) run away?\n")
    if option1 == '1':
        if "sword" in weapon:
            print_pause(f"As the {enemy} moves to attack,"
                        "you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly"
                        "in your hand as you brace yourself for the attack.")
            print_pause(f"But the {enemy} takes one look at your shiny"
                        "new toy and runs away!")
            print_pause(f"You have rid the town of the {enemy}."
                        "You are victorious!")
            print_pause("you WON the GAME")
            choice()
        else:
            print_pause("You do your best...")
            print_pause("but your dagger is no match for the gorgon.")
            print_pause("You have been defeated!")
            print_pause("you LOST the GAME")
            choice()
    elif option1 == '2':
        print_pause("You run back into the field. Luckily,"
                    "you don't seem to have been followed.\n\n")
    else:
        print_pause("wrong type, try again")


def cave():
    print_pause("You peer cautiously into the cave")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger and"
                "take the sword with you.")
    print_pause("You walk back out to the field.\n\n")
    weapon.append("sword")


def begin():
    while True:
        print_pause("Enter 1 to knock on the door of the house.\n"
                    "Enter 2 to peer into the cave.")
        print_pause("What would you like to do?\n")
        option = input("Please enter 1 or 2\n")
        if option == '1':
            house()
        elif option == '2':
            cave()
        else:
            print_pause("wrong type, try again")


def choice():
    while True:
        choice = input("Would you like to play again? (y/n)\n")
        if choice == "y":
            print("Excellent! Restarting the game ...\n\n")
            enemies = ["pirate", "gorgon", "troll", "skeletor",
                       "bloody baron", "gray lady"]
            enemy = random.choice(enemies)
            print_pause(f"{enemy} is your enemy for this game\n")
            print_pause("Let's Begin\n\n")
            intro()
            begin()
        elif choice == "n":
            print_pause("Goodbye..seeyou next time!\n\n")
            exit()
        else:
            print_pause("wrong type, try again")


def play_game():
    intro()
    begin()


enemies = ["pirate", "gorgon", "troll", "skeletor",
           "bloody baron", "gray lady"]
enemy = random.choice(enemies)
print_pause(f"{enemy} is your enemy for this game\n")
print_pause("Let's Begin\n\n")

play_game()
