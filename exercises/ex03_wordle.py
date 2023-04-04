"""Final Wordle."""

__author__ = "730569838"

def contains_char(long_string: str, one_character: str) -> bool:
    """When given two strings, the first of any length, the second a single character, returns True if single character is anywhere in long string and False otherwise."""
    assert len(one_character) == 1
    count: int = 0
    while count < len(long_string):
        if long_string[int(count)] == one_character:
            return True
        else:
            count = count + 1
    return False

def emojified(guess: str, secret: str) -> str:
    """Return an emoji box string using the contains_char function to determine if the letters in guess are anywhere in secret."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    count: int = 0
    boxes: str = ""
    secret_count: int = 0
    while count < len(secret):
        if contains_char(secret, guess[count]) == True:
            if secret[int(secret_count)] == guess[int(count)]:
                boxes = boxes + GREEN_BOX
                secret_count = secret_count + 1
            else:
                boxes = boxes + YELLOW_BOX
                secret_count = secret_count + 1
        if contains_char(secret, guess[count]) == False:
            boxes = boxes + WHITE_BOX
            secret_count = secret_count + 1
        count = count + 1
    return boxes

def input_guess(number: int) -> str:
    """Given an integer “number” of a guess as a parameter, prompts user for a guess and continue prompting them until they provide a guess of the expected length."""
    guess: str = str(input(f"Enter a {number} character word: "))
    while len(guess) != number:
            guess = str(input(f"That was not {number} chars! Try again: "))
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    guess_count: int = 1
    SECRET_WORD: str = "codes"
    won: bool = False
    while guess_count < 7 and won == False:
        print(f"=== Turn {guess_count}/6 ===")
        guess = input_guess(5)
        print(emojified(guess, SECRET_WORD))
        if guess == SECRET_WORD:
            print(f"You won in {guess_count}/6 turns!")
            won = True
        else:
            guess_count = guess_count + 1
    if won == False:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()