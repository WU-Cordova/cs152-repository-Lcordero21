import random
import bag

class Character:
    name: str
    score: int
    attack_power: int

class Game:
    def __init__(self,player:Character, dealer:Character):
