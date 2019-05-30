import tkinter
import random


class unit(object):
    def __init__(self,name,strength,dexterity,\
    constitution,wisdom,intelligence,charisma, BaseHP):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma
        self.name = name
        print("character created")

    def __str__(self):
        return self.name
    def roll(self):
        self.strength = random.randint(1,6)
        print(self.strength)
        


