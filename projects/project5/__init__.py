from datastructures import *

class Menu:
    def __init__(self, name:str, size:str, price:float) -> None:
        self._name = name
        self._size = size
        self._price = price
    
    def get_name(self) -> str:
        return self._name
    
    def get_size(self) -> str:
        return self._size
    
    def get_price(self) -> float:
        return self._price
    
    def __str__(self) -> None:
        print(f"{self._name} - {self._price}")