from datetime import date
from typing import Self
from alphabet_class import Alphabet

class EngAlphabet(Alphabet):
    """class inheritor"""

    _letters_num = 26

    def __init__(self) -> None:
        super().__init__('EN', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def  is_en_letter(self, letter: str) -> bool:
        return letter in self.letters
    
    def amouunt_of_letters(self):
        return self._letters_num
    
    @staticmethod 
    def example() -> str:
        return "Text in English."
    
    @classmethod
    def snapshot(cls) -> Self:
        instance = cls()
        instance.date_of_creating_an_object = date.today()
        return instance
        








   