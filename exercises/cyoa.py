"""Choose your own adventure."""


from random import randint


__author__ = "730569838"


SMILEY_FACE: str = "\U0001F601"
UNAMUSED_FACE: str = "\U0001F612"
points: int = 0
player: str = ""


def main() -> None:
    """The main function. Plays the adventure and can loop."""
    greet()
    playing: bool = True
    while playing == True:
        adventure()
        loop_option = input(f"Wow, {player}, you currently have {points} points! Would you like to stop or go back? ")
        if loop_option == "stop":
            playing = False


def greet() -> None:
    """Greets the player and gives them context."""
    global player
    player = input("What is your name adventurer? ")
    print(f"Welcome, {player}. Be wary of the monsters in the cave! ")


def adventure() -> None:
    """This is the actual adventure. Gives the player 3 options to choose from."""
    global points
    choice = input(f"Welcome to the first floor of the cave, {player}. Do you want to go deeper, venture ahead, or escape the cave? ")
    if choice == "escape the cave":
        points = escape(points)
    if choice == "go deeper":
        go_deeper()
    if choice == "venture ahead":
        venture_ahead()


def escape(score: int) -> int:
    """This is if the player chooses to escape the cave, and updates point totals as well."""
    escape_choice = input("Quickly, you can only grab the diamond, the hat, or the sword before the cave collapses. Which one do you want to save? ")
    if escape_choice == "the hat":
        score += 0
    if escape_choice == "the diamond":
        score += 10
    if escape_choice == "the sword":
        score += 5
    print(f"Congratulations, {player}. You escaped the cave with {escape_choice} and finished with {score} points. Thank you for playing! ")
    return score


def go_deeper() -> None:
    """This function is for if the player chooses to go deeper into the cave, and they have to fight a skeleton that is either weak normal or strong."""
    global points
    print("You trek deeper into the caverns. ")
    skeleton_level = randint(1, 3)
    if skeleton_level == 1:
        choice = input("Watch out! A weak skeleton approaches. Would you like to fight or flee? ")
        if choice == "fight":
            fighting1 = randint(1, 4)
            if fighting1 == 1:
                print("You lost and had to run away, losing 3 points. ")
                points = points - 3
            if fighting1 > 1:
                print("You defeated the skeleton! Congratulations, you have been awarded 3 points. ")
                points = points + 3
        if choice == "flee":
            print("You narrowly escape the skeleton. ")
    if skeleton_level == 2:
        choice = input("Watch out! A normal skeleton approaches. Would you like to fight or flee? ")
        if choice == "fight":
            fighting1 = randint(1, 4)
            if fighting1 <= 2:
                print("You lost and had to run away, losing 3 points. ")
                points = points - 3
            if fighting1 > 2:
                print("You defeated the skeleton! Congratulations, you have been awarded 3 points. ")
                points = points + 3
        if choice == "flee":
            print("You narrowly escape the skeleton. ")
    if skeleton_level == 3:
        choice = input("Watch out! A strong skeleton approaches. Would you like to fight or flee? ")
        if choice == "fight":
            fighting1 = randint(1, 4)
            if fighting1 <= 3:
                print("You lost and had to run away, losing 3 points. ")
                points = points - 3
            if fighting1 == 4:
                print("You defeated the skeleton! Congratulations, you have been awarded 3 points. ")
                points = points + 3
        if choice == "flee":
            print("You narrowly escape the skeleton. ")


def venture_ahead() -> None:
    """This is for if the player chooses to venture ahead. They will either encounter a zombie, stone golem, or ghost."""
    global points
    print("You briskly walk forward. ")
    monster = randint(1, 3)
    if monster == 1:
        choice = input("Out of the depths a zombie approaches! Do you want to fight or flee? ")
        if choice == "fight":
            print("You defeated the zombie and earned 2 points! ")
            points = points + 2
        if choice == "flee":
            print("You escape the zombie with ease. ")
    if monster == 2:
        choice = input("You hear loud thuds. Oh no! A stone golem! Fight or flee? ")
        if choice == "fight":
            print(f"The golem bashed your head in. You lost 10 points! I guessed you learned a lesson: Never fight a stone golem {UNAMUSED_FACE}. ")
            points = points - 10
        if choice == "flee":
            print(f"What a smart choice that was. For your intelligence, I will award you a point. Actually, make that 2 points. I got you {SMILEY_FACE}. ")
            points = points + 2
    if monster == 3:
        choice = input("Oh my goodness! Is that a ghost? It is! Would you like to fight or flee? ")
        if choice == "fight":
            fighting1 = randint(1, 5)
            if fighting1 <= 4:
                print("Your sword went right through it. Honestly you should have expected that. No points! ")
            if fighting1 == 5:
                print("Wait, what? How did.... your sword? Okay well I guess you killed the ghost. 10 points to you! ")
                points = points + 10


if __name__ == "__main__":
  main()