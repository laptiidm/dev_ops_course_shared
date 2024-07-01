from alphabet_class import Alphabet
from datetime import date
from typing import Self

class UaAlphabet(Alphabet):
    """derived class"""

    _letters_num = 33

    def __init__(self) -> None:
        super().__init__('UA', 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ')

    def is_ua_letter(self, letter: str) -> bool:
        return letter in self.letters
    
    def amouunt_of_letters(self):
        return self._letters_num
    
    @staticmethod 
    def example() -> str:
        return "Текст українською!"
    
    @classmethod
    def snapshot(cls) -> Self:
        instance = cls()
        instance.date_of_creating_an_object = date.today()
        return instance
    

