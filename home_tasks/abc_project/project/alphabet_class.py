import random

class Alphabet:
    """base class"""

    date_of_creating_an_object = ''

    def __init__(self, lang: str, letters: str) -> None:
        self.lang = lang
        self.letters = letters
    
    def print_letters(self) -> str:
        return self.letters

    def amouunt_of_letters(self) -> int:
       return len(self.letters)

    def random_letter(self):
        return random.choice(self.letters)
    
    def is_in_alphabet(self, letter: str):
        return letter in self.letters

    def to_uppercase(self, char: str):
        if char in self.letters and char.islower():
            return char.upper()
        else:
            print("ERROR")

    def to_lowercase(self, char: str):
        if char in self.letters and char.isupper():
            return char.lower()
        else:
            print("ERROR")
    


