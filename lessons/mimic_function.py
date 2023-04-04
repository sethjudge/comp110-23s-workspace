def mimic(my_words: str) -> str:
    """Given the string my_words, outputs the same string"""
    return my_words

mimic("Hello!")
print(mimic("Hello!"))

my_words: str = "Hello!"
response: str = mimic(my_words)
print(response)