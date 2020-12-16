from randomname import randomname
from toysgen import toysgen
from randomintro import randomintro
from randomfiller import randomfiller
from addressgen import addressgen
from reversegeocoder import reversegeocode, randomlocation as randomloc
from reversegeocoder import randomfakelocation as randomfakeloc
from favcolourgen import colgen

import numpy as np
import random

#4 zile - 0,0001 secunde per scrisoare
# 0.882 secunde per scrisoare in momentul actual 

global nrr
nrr = 0
global fileName
fileName = 'LETTERS.txt'

def determineLastLetter():
    global nrr
    global fileName
    try:
        file1 = open(fileName, 'r')
    except:
        file1 = open(fileName, 'w')
        file1.write("n*r=0\n")
        file1.close()
        file1 = open(fileName,'r')
        
    Lines = file1.readlines() 
    for line in Lines: 
        row = line.strip()
        if("n*r" in row):
            row = row.replace("n*r=", "")
            nrr = int(row)
    file1.close()
    #print(nrr)

def generateLetter():

    loc = randomfakeloc()
    toys = toysgen()
    
    #should randomize filler to appear before or after toysgen
    r1 = random.randint(0,100)
    if(r1<30):
        fillpos = 0
    else:
        fillpos = 1
    #30% chance for the filler to appear after toysgen
    
    letter = "Dear Santa, \n" + randomintro() + " My name is " + randomname() + ", "
    letter = letter + loc[0] + " and " + colgen() + ". "
    
    if(fillpos == 0):
        letter = letter + randomfiller() + " " + toys[0] + toys[1] 
    else:
        letter = letter + toys[0] + toys[1] + " " + randomfiller() + "."
        
    letter = letter + "\nexp:" + loc[1]
    return letter

def test():
    print(generateLetter())


def generateL(nrl):
    global nrr
    global fileName
    determineLastLetter()

    x = 10
    try:
        x = nrl
    except:
        x = 1
    
    for i in range(x):
        
        file1 = open(fileName, 'a')
        try:
            
            letter = generateLetter()

            nrr = nrr + 1
            print(nrr)
            
            file1.write("n*r=" + str(nrr) + "\n")
            file1.write(letter + "\r\n")
            file1.write("\n")
            file1.close()
        except:
            file1.close()


global status
status = 1
            
def main():
    global status
    global nrr
    global fileName

    
    while (status == 1):

        
        print("what do you want to do?")
        print("0 - change file name , currently: " + fileName)
        print("1 - generate n letters")
        print("2 - see how many letters are in the file")
        print("3 - test the program (generate one letter and print it without saving)")
        action = input("insert the number of your command here: ")

        if(action == "0"):
            nrr = 0
            fileName = input("Insert new file name to save the letters in:")

        elif(action == "1"):
            ntg = input("how many?: ")
            print("generating...")
            generateL(int(ntg))
        
        elif(action == "3"):
            print("\n \n")
            print(generateLetter())
            print("\n \n")

        elif(action == "2"):
            determineLastLetter()
            print("\n \nThere are")
            print(nrr)
            print("letters in the file \n \n")

        else:
            print("command error, try again")


    if(status == 0):
        print("Could not connect fetch data from firebase")
            

main()
