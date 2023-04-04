"""One shot Wordle with loops."""

__author__ = "730569838"

SECRET: str = "python"
playing: bool = True
guess: str = str(input("What is your 6-letter guess? "))
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
count = 0
boxes: str = ""
in_word: bool = False
secret_count = 0

while playing:
    if guess == SECRET:
        print(GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX)
        print("Woo! You got it! ")
        playing = False
    else:
        if len(guess) != 6:
            guess = str(input("That was not 6 letters! Try again: "))
        else:
            while count < 6:  # this repeats adding boxes until the index is equal to 6, because the index of 6 letter words only goes to 5
                if guess[int(count)] == SECRET[int(count)]:
                    boxes = boxes + GREEN_BOX
                else:
                    in_word == False
                    secret_count = 0
                    while secret_count < 6 and in_word == False:
                        if guess[int(count)] == SECRET[int(secret_count)]:
                            in_word = True
                        else:
                            secret_count = secret_count + 1
                    if in_word == True:
                        boxes = boxes + YELLOW_BOX
                    else:
                        boxes = boxes + WHITE_BOX
                count = count + 1
            print(boxes)
            print("Not quite. Play again soon! ")
            playing = False

