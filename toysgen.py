from randomtoys import randomtoys
import random

def toysgen():
    toyaskarr = ["This year I want","I want to receive","I wish to get","I would like","I would love","I would like to receive","I wish for","I wish to get","My wish is to receive"]
    i = random.randint(0,len(toyaskarr)-1)
    toyask = toyaskarr[i]
    toys = [toyask +" ", randomtoys() + ". "]
    return toys
