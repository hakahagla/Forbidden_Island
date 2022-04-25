#Forbidden Island
#Last updated: 2022/04/26

#Issues&Queries
#We need arrays storing all the treasure cards - Need to know the exact amount of each card and their type

#Imports
import tkinter as tk
import random

#Constants
TileNames = []
NumFlood = 0
Max_Cards = 5
Difficulty = '' #Novice, Beginner, Normal, Master, Lengendary?
C1 = [] #Character1 Cards
C2 = []
C3 = []
C4 = []
C1 = []

#Variable
UnacquiredItems = []
AcquiredItems = []
CurrentGameTile = []
Half_Flooded = []
FloodCardNum = 0 #Number of flood card to be drawn

#Subprograms

def ini():
    print(1) #Called every game start to initialise the array containing cards of the game
    #Use random to randomise order so later the board can be set up following the order of the list
    #Set flood card num according to difficulty
    #Set 6 tiles to half flooded
    
def CharacterAndSpawnLoc():
    print(1) #Give the players a career
    #Place them on the right tile
    
def DrawTreasure():
    print(1)
    
def WaterRise():
    print(1) #Move tick up
    #Reshuffle
    #Place infront of flood array
    
def DrawFlood():
    print(1)
    #Pick random flood cards
    
def Lift():
    print(1)
    #Lift characters
    #Or used to win

def Sandbag():
    print(1)
    #Shore up a tile

def Capture():
    print(1)
    #Discard 4 cards
    #Acquired items move into an array
    
def Move():
    print(1)

#Need subprograms for special abilities

    
#Mainprogram
#Menu page
menu = tk.Tk()
menu.geometry('800x700')
menu.title("ForbiddenIsland-Menu")

#Instructions page

#Options page

menu.mainloop()



