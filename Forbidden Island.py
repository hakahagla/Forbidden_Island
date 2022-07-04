#Forbidden Island
#Last updated: 2022/7/4

#Information
#There are 24tiles
#6 characters(Diver,Engineer,Explorer,Messenger,Navigator&Pilot)
#28 Treasure Cards in Total: 5 Fire ,5 Lion ,5Glode ,5 Cup,2 SandBag, 3 HelicopterLift, 3 WatersRise
#Flood cards 1 of each tile
#Start location: Pilot(Blue) - Fools Landing, Engineer(Red) - Bronze Gate, Messenger(White) - Silver Gate, Diver(Black) - Iron Gate, Explorer(Green) - Copper Gate
                        #Navigator(Gold) - Gold Gate
#CupTiles: Tidal Palace, Coral Palace
#GlobeTiles: Temple of The Sun, Temple of the Moon
#LionTiles: Whispering Garden, Howling Garden
#FireTiles: Cave of Shadows, Cave of Embers

#Ability descriptions
#Pilot: Once per turn, fly to any tile on the island for 1 action
#Engineer: Shore up 2 tiles for 1 action
#Messenger: Give Treasure cards to a player anywhere on the island for 1 action per card
#Diver: Move through 1 of more adjacent flooded and/or missing tiles for 1 action.(Must end your turn on a tile)
#Explorer:Move and/or shore up diagonally.
#Navigator: Move another player up to 2 adjacent tiles for 1 action


#Imports--------------------------------------------------------------------------------------------------------------------
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.simpledialog import askstring
from tkinter.messagebox import askyesno
from tkinter.messagebox import showwarning
from PIL import Image,ImageTk
import random

#Windows
root = tk.Tk()
root.geometry('1000x700')
rulewindow = Toplevel()
rulewindow.geometry('1600x1600')
rulewindow.title("ForbiddenIsland-Instructions")
rulewindow.configure(bg = "#efe0b0")


#Constants------------------------------------------------------------------------------------------------------------------------------------

TileNames = ["Observatory","CoralPalace","CaveOfShadows","MistyMarsh","WhisperingGardens","FoolsLanding","WatchTower",
"CrimsonForest","CliffsOfAbandon","TempleOfTheMoon","DunesOfDeception", "IronGate","BreakersBridge", "BronzeGate","GoldGate","TidalPalace",
"LostLagoon","CopperGate", "CaveOfEmbers", "SilverGate", "TempleOfTheSun", "PhantomRock", "HowlingGardens", "TwilightHollow"]
TreasureCards = ['Lion','Lion','Lion','Lion','Lion','Fire','Fire','Fire','Fire','Fire','Globe','Globe','Globe','Globe','Globe','Cup','Cup','Cup','Cup','Cup','SandBag','SandBag','HelicopterLift','HelicopterLift','WatersRise','WatersRise','WatersRise']
Characters = ['Pilot','Engineer','Messenger','Diver','Explorer','Navigator']
NumFlood = 0
ActionPoint = 3

#Variables------------------------------------------------------------------------------------------------------------------------------------


tCounter = 0 #Treasure Counter
C1 = [] #Character1 Cards
C2 = []
C3 = []
C4 = []
C1Char = ''
C2Char = ''
C3Char = ''
C4Char = ''
Difficulty = 0
NumPlayers = 0
UnacquiredItems = ['TheCrystalOfFire','TheStatueOfTheWind','TheOceansChalice','TheEarthStone']
AcquiredItems = []
CurrentGameTile = []
CurrentCharacter = []
CurrPlayer = 1
CurrentFlood = TileNames[:] #Current Ingame Flood Tiles
TileOrder = []
FloodDiscard = [] #Ingame Discard Pile
HalfFlooded = [] #Currently HalfFlooded
#28 Treasure Cards in Total: 5 Fire ,5 Lion ,5Globe ,5 Cup,2 SandBag, 3 HelicopterLift, 3 WatersRise
TreasureDiscard = []
InPlay = [] #Characters Inplay
WaterTick=0
FloodCardNum = 2 #Number of flood card to be drawn

#Image Import------------------------------------------------------------------------------------------------------------------------------------

#HearthStone
hearthstone = PhotoImage(file = "./images/action_cards/actions_back.png")
hearthstone = hearthstone.subsample(3)

#Rules
rulebookcover = Image.open("./images/Forbidden_Island_game_cover.jpg")
rulebookcover = rulebookcover.resize((400,550))
rulebookcover = ImageTk.PhotoImage(rulebookcover)
pic1 = PhotoImage(file = "./images/rules/page1.png")
pic2 = PhotoImage(file = "./images/rules/page2new.png")
pic3 = PhotoImage(file = "./images/rules/page3new.png")
pic4 = PhotoImage(file = "./images/rules/page4new.png")
pic5 = PhotoImage(file = "./images/rules/page5new.png")
pic6 = PhotoImage(file = "./images/rules/page6new.png")
pic7 = PhotoImage(file = "./images/rules/page7new.png")
pic8 = PhotoImage(file = "./images/rules/page8.png")
pic = Label(rulewindow,image=pic1)
pic.pack()

#TilePicture
#No Flood
WhisperingGardens = Image.open("./images/tiles/whispering_garden.png" )
WhisperingGardens = WhisperingGardens.resize((100,100))
WhisperingGardens = ImageTk.PhotoImage(WhisperingGardens)

WatchTower = Image.open("./images/tiles/watchtower.png" )
WatchTower  = WatchTower.resize((100,100))
WatchTower  = ImageTk.PhotoImage(WatchTower)

TwilightHollow = Image.open("./images/tiles/twilight_hollow.png" )
TwilightHollow = TwilightHollow.resize((100,100))
TwilightHollow  = ImageTk.PhotoImage(TwilightHollow)

TidalPalace = Image.open("./images/tiles/tidal_palace.png" )
TidalPalace = TidalPalace.resize((100,100))
TidalPalace = ImageTk.PhotoImage(TidalPalace)

TempleOfTheSun = Image.open("./images/tiles/temple_of_the_sun.png" )
TempleOfTheSun = TempleOfTheSun.resize((100,100))
TempleOfTheSun = ImageTk.PhotoImage(TempleOfTheSun)

TempleOfTheMoon = Image.open("./images/tiles/temple_of_the_moon.png" )
TempleOfTheMoon = TempleOfTheMoon.resize((100,100))
TempleOfTheMoon = ImageTk.PhotoImage(TempleOfTheMoon)

SilverGate = Image.open("./images/tiles/silver_gate.png" )
SilverGate = SilverGate.resize((100,100))
SilverGate = ImageTk.PhotoImage(SilverGate)

PhantomRock = Image.open("./images/tiles/phantom_rock.png" )
PhantomRock = PhantomRock.resize((100,100))
PhantomRock = ImageTk.PhotoImage(PhantomRock)

Observatory = Image.open("./images/tiles/observatory.png" )
Observatory = Observatory.resize((100,100))
Observatory = ImageTk.PhotoImage(Observatory)

MistyMarsh = Image.open("./images/tiles/misty_marsh.png" )
MistyMarsh = MistyMarsh.resize((100,100))
MistyMarsh = ImageTk.PhotoImage(MistyMarsh)
                                
LostLagoon = Image.open("./images/tiles/lost_lagoon.png" )
LostLagoon = LostLagoon.resize((100,100))
LostLagoon = ImageTk.PhotoImage(LostLagoon)

IronGate = Image.open("./images/tiles/iron_gate.png" )
IronGate = IronGate.resize((100,100))
IronGate = ImageTk.PhotoImage(IronGate)

HowlingGardens = Image.open("./images/tiles/howling_garden.png")
HowlingGardens = HowlingGardens.resize((100,100))
HowlingGardens = ImageTk.PhotoImage(HowlingGardens)

GoldGate= Image.open("./images/tiles/gold_gate.png")
GoldGate = GoldGate.resize((100,100))
GoldGate = ImageTk.PhotoImage(GoldGate)

FoolsLanding = Image.open("./images/tiles/fools_landing.png")
FoolsLanding = FoolsLanding.resize((100,100))
FoolsLanding = ImageTk.PhotoImage(FoolsLanding)

DunesOfDeception= Image.open("./images/tiles/dunes_of_deception.png")
DunesOfDeception = DunesOfDeception.resize((100,100))
DunesOfDeception = ImageTk.PhotoImage(DunesOfDeception)

CrimsonForest = Image.open("./images/tiles/crimson_forest.png")
CrimsonForest = CrimsonForest.resize((100,100))
CrimsonForest = ImageTk.PhotoImage(CrimsonForest)

CoralPalace = Image.open("./images/tiles/coral_palace.png")
CoralPalace = CoralPalace.resize((100,100))
CoralPalace = ImageTk.PhotoImage(CoralPalace)

CopperGate = Image.open("./images/tiles/copper_gate.png")
CopperGate = CopperGate.resize((100,100))
CopperGate = ImageTk.PhotoImage(CopperGate)

CliffsOfAbandon = Image.open("./images/tiles/cliffs_of_abandon.png")
CliffsOfAbandon = CliffsOfAbandon.resize((100,100))
CliffsOfAbandon = ImageTk.PhotoImage(CliffsOfAbandon)

CaveOfShadows = Image.open("./images/tiles/cave_of_shadows.png")
CaveOfShadows = CaveOfShadows.resize((100,100))
CaveOfShadows = ImageTk.PhotoImage(CaveOfShadows)

CaveOfEmbers= Image.open("./images/tiles/cave_of_embers.png")
CaveOfEmbers = CaveOfEmbers.resize((100,100))
CaveOfEmbers = ImageTk.PhotoImage(CaveOfEmbers)

BronzeGate= Image.open("./images/tiles/bronze_gate.png")
BronzeGate = BronzeGate.resize((100,100))
BronzeGate = ImageTk.PhotoImage(BronzeGate)

BreakersBridge = Image.open("./images/tiles/breakers_bridge.png")
BreakersBridge = BreakersBridge.resize((100,100))
BreakersBridge = ImageTk.PhotoImage(BreakersBridge)
#HalfFlood
WhisperingGardensF = Image.open("./images/tiles/whispering_garden_f.png" )
WhisperingGardensF = WhisperingGardensF.resize((100,100))
WhisperingGardensF = ImageTk.PhotoImage(WhisperingGardensF)

WatchTowerF = Image.open("./images/tiles/watchtower_f.png" )
WatchTowerF  = WatchTowerF.resize((100,100))
WatchTowerF  = ImageTk.PhotoImage(WatchTowerF)

TwilightHollowF = Image.open("./images/tiles/twilight_hollow_f.png" )
TwilightHollowF = TwilightHollowF.resize((100,100))
TwilightHollowF  = ImageTk.PhotoImage(TwilightHollowF)

TidalPalaceF = Image.open("./images/tiles/tidal_palace_f.png" )
TidalPalaceF = TidalPalaceF.resize((100,100))
TidalPalaceF = ImageTk.PhotoImage(TidalPalaceF)

TempleOfTheSunF = Image.open("./images/tiles/temple_of_the_sun_f.png" )
TempleOfTheSunF = TempleOfTheSunF.resize((100,100))
TempleOfTheSunF = ImageTk.PhotoImage(TempleOfTheSunF)

TempleOfTheMoonF = Image.open("./images/tiles/temple_of_the_moon_f.png" )
TempleOfTheMoonF = TempleOfTheMoonF.resize((100,100))
TempleOfTheMoonF = ImageTk.PhotoImage(TempleOfTheMoonF)

SilverGateF = Image.open("./images/tiles/silver_gate_f.png" )
SilverGateF = SilverGateF.resize((100,100))
SilverGateF = ImageTk.PhotoImage(SilverGateF)

PhantomRockF = Image.open("./images/tiles/phantom_rock_f.png" )
PhantomRockF = PhantomRockF.resize((100,100))
PhantomRockF = ImageTk.PhotoImage(PhantomRockF)

ObservatoryF = Image.open("./images/tiles/observatory_f.png" )
ObservatoryF = ObservatoryF.resize((100,100))
ObservatoryF = ImageTk.PhotoImage(ObservatoryF)

MistyMarshF = Image.open("./images/tiles/misty_marsh_f.png" )
MistyMarshF = MistyMarshF.resize((100,100))
MistyMarshF = ImageTk.PhotoImage(MistyMarshF)
                                
LostLagoonF = Image.open("./images/tiles/lost_lagoon_f.png" )
LostLagoonF = LostLagoonF.resize((100,100))
LostLagoonF = ImageTk.PhotoImage(LostLagoonF)

IronGateF = Image.open("./images/tiles/iron_gate_f.png" )
IronGateF = IronGateF.resize((100,100))
IronGateF = ImageTk.PhotoImage(IronGateF)

HowlingGardensF = Image.open("./images/tiles/howling_garden_f.png")
HowlingGardensF = HowlingGardensF.resize((100,100))
HowlingGardensF = ImageTk.PhotoImage(HowlingGardensF)

GoldGateF = Image.open("./images/tiles/gold_gate_f.png")
GoldGateF = GoldGateF.resize((100,100))
GoldGateF = ImageTk.PhotoImage(GoldGateF)

FoolsLandingF = Image.open("./images/tiles/fools_landing_f.png")
FoolsLandingF = FoolsLandingF.resize((100,100))
FoolsLandingF = ImageTk.PhotoImage(FoolsLandingF)

DunesOfDeceptionF = Image.open("./images/tiles/dunes_of_deception_f.png")
DunesOfDeceptionF = DunesOfDeceptionF.resize((100,100))
DunesOfDeceptionF = ImageTk.PhotoImage(DunesOfDeceptionF)

CrimsonForestF = Image.open("./images/tiles/crimson_forest_f.png")
CrimsonForestF = CrimsonForestF.resize((100,100))
CrimsonForestF = ImageTk.PhotoImage(CrimsonForestF)

CoralPalaceF = Image.open("./images/tiles/coral_palace_f.png")
CoralPalaceF = CoralPalaceF.resize((100,100))
CoralPalaceF = ImageTk.PhotoImage(CoralPalaceF)

CopperGateF = Image.open("./images/tiles/copper_gate_f.png")
CopperGateF = CopperGateF.resize((100,100))
CopperGateF = ImageTk.PhotoImage(CopperGateF)

CliffsOfAbandonF = Image.open("./images/tiles/cliffs_of_abandon_f.png")
CliffsOfAbandonF = CliffsOfAbandonF.resize((100,100))
CliffsOfAbandonF = ImageTk.PhotoImage(CliffsOfAbandonF)

CaveOfShadowsF = Image.open("./images/tiles/cave_of_shadows_f.png")
CaveOfShadowsF = CaveOfShadowsF.resize((100,100))
CaveOfShadowsF = ImageTk.PhotoImage(CaveOfShadowsF)

CaveOfEmbersF = Image.open("./images/tiles/cave_of_embers_f.png")
CaveOfEmbersF = CaveOfEmbersF.resize((100,100))
CaveOfEmbersF = ImageTk.PhotoImage(CaveOfEmbersF)

BronzeGateF = Image.open("./images/tiles/bronze_gate_f.png")
BronzeGateF = BronzeGateF.resize((100,100))
BronzeGateF = ImageTk.PhotoImage(BronzeGateF)

BreakersBridgeF = Image.open("./images/tiles/breakers_bridge_f.png")
BreakersBridgeF = BreakersBridgeF.resize((100,100))
BreakersBridgeF = ImageTk.PhotoImage(BreakersBridgeF)

#FloodDeck BackCover
FloodDeck = PhotoImage(file = "./images/flood_deck_card.fw.png")
FloodDeck = FloodDeck.subsample(5)
#WaterMark Picture
#water0 = Water Level 0
water0 = Image.open("./images/water_gauge/level_0.png")
water0 = water0.resize((100,150))
water0 = ImageTk.PhotoImage(water0)
water1 = Image.open("./images/water_gauge/level_1.png")
water1 = water1.resize((100,150))
water1 = ImageTk.PhotoImage(water1)
water2 = Image.open("./images/water_gauge/level_2.png")
water2 = water2.resize((100,150))
water2 = ImageTk.PhotoImage(water2)
water3 = Image.open("./images/water_gauge/level_3.png")
water3 = water3.resize((100,150))
water3 = ImageTk.PhotoImage(water3)
water4 = Image.open("./images/water_gauge/level_4.png")
water4 = water4.resize((100,150))
water4 = ImageTk.PhotoImage(water4)
water5 = Image.open("./images/water_gauge/level_5.png")
water5 = water5.resize((100,150))
water5 = ImageTk.PhotoImage(water5)
water6 = Image.open("./images/water_gauge/level_6.png")
water6 = water6.resize((100,150))
water6 = ImageTk.PhotoImage(water6)
water7 = Image.open("./images/water_gauge/level_7.png")
water7 = water7.resize((100,150))
water7 = ImageTk.PhotoImage(water7)
water8 = Image.open("./images/water_gauge/level_8.png")
water8 = water8.resize((100,150))
water8 = ImageTk.PhotoImage(water8)
water9 = Image.open("./images/water_gauge/level_9.png")
water9 = water9.resize((100,150))
water9 = ImageTk.PhotoImage(water9)


#Subprograms------------------------------------------------------------------------------------------------------------------------------------
def ini(): #Initialise the arrays and variables
    global CurrentFlood
    global FloodDiscard
    #Getting the starting flood tiles
    for i in range (0,6):
        temp=random.randint(0, len(CurrentFlood)-1)
        FloodDiscard.append(CurrentFlood[temp])
        HalfFlooded.append(CurrentFlood[temp])
        CurrentFlood.remove(CurrentFlood[temp])
ini()
    #Set water mark
    #Called every game start to initialise the array containing cards of the game
    #Use random to randomise order so later the board can be set up following the order of the list
    #Set flood card num according to difficulty
    #Set 6 tiles to half flooded
#------------------------------------------------------------------------------------------------------------------------------------
def DrawTreasure():
    global NumPlayers
    global FloodDiscard
    global WaterTick
    global tCounter #Treasure Counter
    firstCard = random.randint(0, len(TreasureCards)-1)
    secondCard = random.randint(0, len(TreasureCards)-1)
    if TreasureCards[firstCard] == "WatersRise":
        random.shuffle(FloodDiscard)
        CurrentFlood = FloodDiscard[:]
        WaterTick+=1
        FloodDiscard = []
        SetWaterMark()
        ChangeWaterMark()
        changeFloodCardNum()
    if TreasureCards[secondCard] == "WatersRise":
        random.shuffle(FloodDiscard)
        CurrentFlood = FloodDiscard[:]
        FloodDiscard = []
        WaterTick+=1
        SetWaterMark()
        ChangeWaterMark()
        changeFloodCardNum()

    if tCounter == 3:
        if TreasureCards[firstCard] != 'WatersRise':
            C4.append(TreasureCards[firstCard])
            DiscardSelect()
        if TreasureCards[secondCard] != 'WatersRise':
            C4.append(TreasureCards[secondCard])
            DiscardSelect()
        tCounter = 0
    elif tCounter == 2:
        if TreasureCards[firstCard] != 'WatersRise':
            C3.append(TreasureCards[firstCard])
            DiscardSelect()
        if TreasureCards[secondCard] != 'WatersRise':
            C3.append(TreasureCards[secondCard])
            DiscardSelect()
        if NumPlayers == 3:
            tCounter = 0
        else:
            tCounter +=1
    elif tCounter == 1:
        if TreasureCards[firstCard] != 'WatersRise':
            C2.append(TreasureCards[firstCard])
            DiscardSelect()
        if TreasureCards[secondCard] != 'WatersRise':
            C2.append(TreasureCards[secondCard])
            DiscardSelect()
        if NumPlayers == 2:
            tCounter = 0
        else:
            tCounter += 1
    elif tCounter == 0:
        if TreasureCards[firstCard] != 'WatersRise':
            C1.append(TreasureCards[firstCard])
            DiscardSelect()
        if TreasureCards[secondCard] != 'WatersRise':
            C1.append(TreasureCards[secondCard])
            DiscardSelect()
        tCounter += 1
    print("Character 1 Cards: ",C1)
    print("Character 2 Cards: ",C2)
    print("Character 3 Cards: ",C3)
    print("Character 4 Cards: ",C4) 
#------------------------------------------------------------------------------------------------------------------------------------
def FloodDeckDraw():
    #FloodCard Num
    global WaterTick
    SetWaterMark()
    if WaterTick <= 2:
        firstCard = random.randint(0, len(CurrentFlood)-1)
        FloodDiscard.append(CurrentFlood[firstCard])
        HalfFlooded.append(CurrentFlood[firstCard])
        changeFloodTile()
        CurrentFlood.remove(CurrentFlood[firstCard])
        
        secondCard = random.randint(0, len(CurrentFlood)-1)
        FloodDiscard.append(CurrentFlood[secondCard])
        HalfFlooded.append(CurrentFlood[secondCard])
        changeFloodTile()
        CurrentFlood.remove(CurrentFlood[secondCard])
        
        print("FLOOD DISCARD: " + str(FloodDiscard))

    elif WaterTick > 2 and WaterTick <= 5:
        firstCard = random.randint(0, len(CurrentFlood)-1)
        FloodDiscard.append(CurrentFlood[firstCard])
        HalfFlooded.append(CurrentFlood[firstCard])
        changeFloodTile()
        CurrentFlood.remove(CurrentFlood[firstCard])
        
        secondCard = random.randint(0, len(CurrentFlood)-1)
        FloodDiscard.append(CurrentFlood[secondCard])
        HalfFlooded.append(CurrentFlood[secondCard])
        changeFloodTile()
        CurrentFlood.remove(CurrentFlood[secondCard])
        
        thirdCard = random.randint(0, len(CurrentFlood)-1)
        FloodDiscard.append(CurrentFlood[thirdCard])
        HalfFlooded.append(CurrentFlood[thirdCard])
        changeFloodTile()
        CurrentFlood.remove(CurrentFlood[thirdCard])
        
        print("FLOOD DISCARD: " + str(FloodDiscard))

    elif WaterTick > 5 and WaterTick <= 7:
        firstCard = random.randint(0, len(CurrentFlood)-1)
        FloodDiscard.append(CurrentFlood[firstCard])
        HalfFlooded.append(CurrentFlood[firstCard])
        changeFloodTile()
        CurrentFlood.remove(CurrentFlood[firstCard])
        
        secondCard = random.randint(0, len(CurrentFlood)-1)
        FloodDiscard.append(CurrentFlood[secondCard])
        HalfFlooded.append(CurrentFlood[secondCard])
        changeFloodTile()
        CurrentFlood.remove(CurrentFlood[secondCard])
        
        thirdCard = random.randint(0, len(CurrentFlood)-1)
        FloodDiscard.append(CurrentFlood[thirdCard])
        HalfFlooded.append(CurrentFlood[thirdCard])
        changeFloodTile()
        CurrentFlood.remove(CurrentFlood[thirdCard])

        fourthCard = random.randint(0, len(CurrentFlood)-1)
        FloodDiscard.append(CurrentFlood[fourthCard])
        HalfFlooded.append(CurrentFlood[fourthCard])
        changeFloodTile()
        CurrentFlood.remove(CurrentFlood[fourthCard])

        print("FLOOD DISCARD: " + str(FloodDiscard))

    elif WaterTick > 7  and WaterTick <=9:
        firstCard = random.randint(0, len(CurrentFlood)-1)
        FloodDiscard.append(CurrentFlood[firstCard])
        HalfFlooded.append(CurrentFlood[firstCard])
        changeFloodTile()
        CurrentFlood.remove(CurrentFlood[firstCard])

        secondCard = random.randint(0, len(CurrentFlood)-1)
        FloodDiscard.append(CurrentFlood[secondCard])
        HalfFlooded.append(CurrentFlood[secondCard])
        changeFloodTile()
        CurrentFlood.remove(CurrentFlood[secondCard])
        
        thirdCard = random.randint(0, len(CurrentFlood)-1)
        FloodDiscard.append(CurrentFlood[thirdCard])
        HalfFlooded.append(CurrentFlood[thirdCard])
        changeFloodTile()
        CurrentFlood.remove(CurrentFlood[thirdCard])

        fourthCard = random.randint(0, len(CurrentFlood)-1)
        FloodDiscard.append(CurrentFlood[fourthCard])
        HalfFlooded.append(CurrentFlood[fourthCard])
        changeFloodTile()
        CurrentFlood.remove(CurrentFlood[fourthCard])
        
        fifthCard = random.randint(0, len(CurrentFlood)-1)
        FloodDiscard.append(CurrentFlood[fifthCard])
        HalfFlooded.append(CurrentFlood[fifthCard])
        changeFloodTile()
        CurrentFlood.remove(CurrentFlood[fifthCard])
           
        print("FLOOD DISCARD: " + str(FloodDiscard))

        print("CURRENT FLOOD: " + str(CurrentFlood))  
#------------------------------------------------------------------------------------------------------------------------------------
def changeFloodCardNum():
    global FloodCardNum
    if WaterTick >2 and WaterTick <=5:
        FloodCardNum = 3
    elif WaterTick >5 and WaterTick <=7:
        FloodCardNum = 4
    elif WaterTick >7 and WaterTick <=9:
        FloodCardNum = 5
    elif  WaterTick ==10:
        tk.messagebox.showerror("GG","Game over :(")
     #Game over
#------------------------------------------------------------------------------------------------------------------------------------
def changeFloodTile():
    global FloodDiscard
    global TileOrder
    for x in range(1,24):
        for y in range(0,len(FloodDiscard)):
            if HalfFlooded[y] == TileOrder[x]:
                target = 'mapcard' + str(x+1)
                if TileOrder[x] == 'WhisperingGardens':
                    globals()[target].configure(image = WhisperingGardensF)
                elif TileOrder[x] == 'WatchTower':
                    globals()[target].configure(image = WatchTowerF)                    
                elif TileOrder[x] == 'TwilightHollow':
                    globals()[target].configure(image = TwilightHollowF)
                elif TileOrder[x] == 'TidalPalace':
                    globals()[target].configure(image = TidalPalaceF)
                elif TileOrder[x] == 'TempleOfTheSun':
                    globals()[target].configure(image = TempleOfTheSunF)
                elif TileOrder[x] == 'TempleOfTheMoon':
                    globals()[target].configure(image = TempleOfTheMoonF)
                elif TileOrder[x] == 'SilverGate':
                    globals()[target].configure(image = SilverGateF)
                elif TileOrder[x] == 'PhantomRock':
                    globals()[target].configure(image = PhantomRockF)
                elif TileOrder[x] == 'Observatory':
                    globals()[target].configure(image = ObservatoryF)
                elif TileOrder[x] == 'MistyMarsh':
                    globals()[target].configure(image = MistyMarshF)
                elif TileOrder[x] == 'LostLagoon':
                    globals()[target].configure(image = LostLagoonF)
                elif TileOrder[x] == 'IronGate':
                    globals()[target].configure(image = IronGateF)
                elif TileOrder[x] == 'HowlingGardens':
                    globals()[target].configure(image = HowlingGardensF)
                elif TileOrder[x] == 'GoldGate':
                    globals()[target].configure(image = GoldGateF)
                elif TileOrder[x] == 'FoolsLanding':
                    globals()[target].configure(image = FoolsLandingF)
                elif TileOrder[x] == 'DunesOfDeception':
                    globals()[target].configure(image = DunesOfDeceptionF)
                elif TileOrder[x] == 'CrimsonForest':
                    globals()[target].configure(image = CrimsonForestF)
                elif TileOrder[x] == 'CoralPalace':
                    globals()[target].configure(image = CoralPalaceF)
                elif TileOrder[x] == 'CopperGate':
                    globals()[target].configure(image = CopperGateF)
                elif TileOrder[x] == 'CliffsOfAbandon':
                    globals()[target].configure(image = CliffsOfAbandonF)
                elif TileOrder[x] == 'CaveOfShadows':
                    globals()[target].configure(image = CaveOfShadowsF)
                elif TileOrder[x] == 'CaveOfEmbers':
                    globals()[target].configure(image = CaveOfEmbersF)
                elif TileOrder[x] == 'BronzeGate':
                    globals()[target].configure(image = BronzeGateF)
                elif TileOrder[x] == 'BreakersBridge':
                    globals()[target].configure(image = BreakersBridgeF)
#------------------------------------------------------------------------------------------------------------------------------------                    
def ChangeWaterMark():
    global WaterTick
    WaterTick+=1#Move tick up
#------------------------------------------------------------------------------------------------------------------------------------ 
def SetWaterMark():
    TreasureDiscard.append('WatersRise')
    if WaterTick == 2:
        watertick.configure(image = water1)
    elif WaterTick == 3:
        watertick.configure(image = water2)
    elif WaterTick == 4:
        watertick.configure(image = water3)
    elif WaterTick == 5:
        watertick.configure(image = water4)
    elif WaterTick == 6:
        watertick.configure(image = water5)
    elif WaterTick == 7:
        watertick.configure(image = water6)
    elif WaterTick == 8:
        watertick.configure(image = water7)
    elif WaterTick == 9:
        watertick.configure(image = water8)
    elif WaterTick == 10:
        watertick.configure(image = water9)
    random.shuffle(FloodDiscard)
#------------------------------------------------------------------------------------------------------------------------------------
def DiscardSelect():
    global tCounter
    while tCounter == 0 and len(C1) > 5:
        unwanted = askstring(title="Discard",prompt='Player 1:' +str(C1))
        C1.remove(unwanted)
        TreasureDiscard.append(unwanted)
    while tCounter == 1 and len(C1) > 5:
        unwanted = askstring(title="Discard",prompt='Player 2:' +str(C2))
        C2.remove(unwanted)
        TreasureDiscard.append(unwanted)
    while tCounter == 2 and len(C3) > 5:
        unwanted = askstring(title="Discard",prompt='Player 3:' +str(C3))
        C3.remove(unwanted)
        TreasureDiscard.append(unwanted)
    while tCounter == 3 and len(C4) > 5:
        unwanted = askstring(title="Discard",prompt='Player 4:' +str(C4))
        C4.remove(unwanted)
        TreasureDiscard.append(unwanted)
#------------------------------------------------------------------------------------------------------------------------------------
def Close():
    answer = askyesno(title='Confirmation',
    message='Are you sure to quit?')
    if answer:
        root.destroy()
    
#Pages of instructions page------------------------------------------------------------------------------------------------------------------------------------
def page1():
    pic.configure(image = pic1)
def page2():
    pic.configure(image = pic2)
def page3():
    pic.configure(image = pic3)
def page4():
    pic.configure(image = pic4)
def page5():
    pic.configure(image = pic5)
def page6():
    pic.configure(image = pic6)
def page7():
    pic.configure(image = pic7)
def page8():
    pic.configure(image = pic8)
#------------------------------------------------------------------------------------------------------------------------------------
def startrules():
    rulewindow.deiconify()
#------------------------------------------------------------------------------------------------------------------------------------
def SpawnPlayers():
    #Creates the players and assign them roles
    global NumPlayers
    global Characters
    global C1Char
    global C2Char
    global C3Char
    global C4Char
    global c1label
    global c2label
    global c3label
    global c4label
    characterOrder = []
    LocalCharacters = Characters[:]
    if NumPlayers == 2:
        x = random.randint(0,len(LocalCharacters)-1)
        C1Char = LocalCharacters[x]
        characterOrder.append(LocalCharacters[x])
        LocalCharacters.remove(LocalCharacters[x])
        x = random.randint(0,len(LocalCharacters)-1)
        C2Char = LocalCharacters[x]
        characterOrder.append(LocalCharacters[x])
    elif NumPlayers == 3:
        x = random.randint(0,len(LocalCharacters)-1)
        C1Char = LocalCharacters[x]
        characterOrder.append(LocalCharacters[x])
        LocalCharacters.remove(LocalCharacters[x])
        x = random.randint(0,len(LocalCharacters)-1)
        C2Char = LocalCharacters[x]
        characterOrder.append(LocalCharacters[x])
        LocalCharacters.remove(LocalCharacters[x])
        x = random.randint(0,len(LocalCharacters)-1)
        C3Char = LocalCharacters[x]
        characterOrder.append(LocalCharacters[x])
    elif NumPlayers == 4:
        x = random.randint(0,len(LocalCharacters)-1)
        C1Char = LocalCharacters[x]
        characterOrder.append(LocalCharacters[x])
        LocalCharacters.remove(LocalCharacters[x])
        x = random.randint(0,len(LocalCharacters)-1)
        C2Char = LocalCharacters[x]
        characterOrder.append(LocalCharacters[x])
        LocalCharacters.remove(LocalCharacters[x])
        x = random.randint(0,len(LocalCharacters)-1)
        C3Char = LocalCharacters[x]
        characterOrder.append(LocalCharacters[x])
        LocalCharacters.remove(LocalCharacters[x])
        x = random.randint(0,len(LocalCharacters)-1)
        C4Char = LocalCharacters[x]
        characterOrder.append(LocalCharacters[x])
    print(characterOrder)
    for i in range (0,len(characterOrder)):
        if characterOrder[i] == 'Navigator':
            for j in range (1,25):
                target = 'mapcard' + str(j)
                if globals()[target].cget('text') == 'GoldGate':
                    xvalue = globals()[target].winfo_x() #x is now storage of x coordinates
                    yvalue = globals()[target].winfo_y()
                    if i == 0:
                        c1label = Label(gamepage,width = '5', height = '2', bg = 'yellow')
                        c1label.place(x=xvalue,y=yvalue)
                    elif i == 1:
                        c2label = Label(gamepage,width = '5', height = '2', bg = 'yellow')
                        c2label.place(x=xvalue+50,y=yvalue)
                    elif i == 2:
                        c3label = Label(gamepage,width = '5', height = '2', bg = 'yellow')
                        c3label.place(x=xvalue,y=yvalue+50)
                    elif i == 3:
                        c4label = Label(gamepage,width = '5', height = '2', bg = 'yellow')
                        c4label.place(x=xvalue+50,y=yvalue+50)
                    break
        elif characterOrder[i] == 'Messenger':
            for j in range (1,25):
                target = 'mapcard' + str(j)
                if globals()[target].cget('text') == 'SilverGate':
                    xvalue = globals()[target].winfo_x()
                    yvalue = globals()[target].winfo_y()
                    if i == 0:
                        c1label = Label(gamepage,width = '5', height = '2', bg = 'white')
                        c1label.place(x=xvalue,y=yvalue)
                    elif i == 1:
                        c2label = Label(gamepage,width = '5', height = '2', bg = 'white')
                        c2label.place(x=xvalue+50,y=yvalue)
                    elif i == 2:
                        c3label = Label(gamepage,width = '5', height = '2', bg = 'white')
                        c3label.place(x=xvalue,y=yvalue+50)
                    elif i == 3:
                        c4label = Label(gamepage,width = '5', height = '2', bg = 'white')
                        c4label.place(x=xvalue+50,y=yvalue+50)
                    break
        elif characterOrder[i] == 'Explorer':
            for j in range (1,25):
                target = 'mapcard' + str(j)
                if globals()[target].cget('text') == 'CopperGate':
                    xvalue = globals()[target].winfo_x()
                    yvalue = globals()[target].winfo_y()
                    if i == 0:
                        c1label = Label(gamepage,width = '5', height = '2', bg = 'green')
                        c1label.place(x=xvalue,y=yvalue)
                    elif i == 1:
                        c2label = Label(gamepage,width = '5', height = '2', bg = 'green')
                        c2label.place(x=xvalue+50,y=yvalue)
                    elif i == 2:
                        c3label = Label(gamepage,width = '5', height = '2', bg = 'green')
                        c3label.place(x=xvalue,y=yvalue+50)
                    elif i == 3:
                        c4label = Label(gamepage,width = '5', height = '2', bg = 'green')
                        c4label.place(x=xvalue+50,y=yvalue+50)
                    break
        elif characterOrder[i] == 'Engineer':
            for j in range (1,25):
                target = 'mapcard' + str(j)
                if globals()[target].cget('text') == 'BronzeGate':
                    xvalue = globals()[target].winfo_x()
                    yvalue = globals()[target].winfo_y()
                    if i == 0:
                        c1label = Label(gamepage,width = '5', height = '2', bg = 'red')
                        c1label.place(x=xvalue,y=yvalue)
                    elif i == 1:
                        c2label = Label(gamepage,width = '5', height = '2', bg = 'red')
                        c2label.place(x=xvalue+50,y=yvalue)
                    elif i == 2:
                        c3label = Label(gamepage,width = '5', height = '2', bg = 'red')
                        c3label.place(x=xvalue,y=yvalue+50)
                    elif i == 3:
                        c4label = Label(gamepage,width = '5', height = '2', bg = 'red')
                        c4label.place(x=xvalue+50,y=yvalue+50)
                    break
        elif characterOrder[i] == 'Diver':
            for j in range (1,25):
                target = 'mapcard' + str(j)
                if globals()[target].cget('text') == 'IronGate':
                    xvalue = globals()[target].winfo_x()
                    yvalue = globals()[target].winfo_y()
                    if i == 0:
                        c1label = Label(gamepage,width = '5', height = '2', bg = 'black')
                        c1label.place(x=xvalue,y=yvalue)
                    elif i == 1:
                        c2label = Label(gamepage,width = '5', height = '2', bg = 'black')
                        c2label.place(x=xvalue+50,y=yvalue)
                    elif i == 2:
                        c3label = Label(gamepage,width = '5', height = '2', bg = 'black')
                        c3label.place(x=xvalue,y=yvalue+50)
                    elif i == 3:
                        c4label = Label(gamepage,width = '5', height = '2', bg = 'black')
                        c4label.place(x=xvalue+50,y=yvalue+50)
                    break
        elif characterOrder[i] == 'Pilot':
            for j in range (1,25):
                target = 'mapcard' + str(j)
                if globals()[target].cget('text') == 'FoolsLanding':
                    xvalue = globals()[target].winfo_x()
                    yvalue = globals()[target].winfo_y()
                    if i == 0:
                        c1label = Label(gamepage,width = '5', height = '2', bg = 'blue')
                        c1label.place(x=xvalue,y=yvalue)
                    elif i == 1:
                        c2label = Label(gamepage,width = '5', height = '2', bg = 'blue')
                        c2label.place(x=xvalue+50,y=yvalue)
                    elif i == 2:
                        c3label = Label(gamepage,width = '5', height = '2', bg = 'blue')
                        c3label.place(x=xvalue,y=yvalue+50)
                    elif i == 3:
                        c4label = Label(gamepage,width = '5', height = '2', bg = 'blue')
                        c4label.place(x=xvalue+50,y=yvalue+50)
                    break
 
    #Top Left of tile is always C1
    #Top Right of tile is always C2
    #Bottom Left of tile is always C3
    #Bottom Right of tile is always C4

#------------------------------------------------------------------------------------------------------------------------------------
def PlayerSwitch():
    global CurrPlayer
    global ActionPoint
    ActionPoint = 3
    if CurrPlayer == 1:
        CurrPlayer +=1
    elif CurrPlayer == 2:
        CurrPlayer += 1
    elif CurrPlayer == 3:
        CurrPlayer += 1
    elif CurrPlayer == 4:
        CurrPlayer = 1
        
#------------------------------------------------------------------------------------------------------------------------------------
def Up():
    global CurrPlayer
    global ActionPoint
    global c1label
    global c2label
    global c3label
    global c4label
    target = 'c' + str(CurrPlayer) + 'label'
    xvalue = globals()[target].winfo_x()
    yvalue = globals()[target].winfo_y()
    if yvalue >= 120 and xvalue >= 400 and xvalue <= 500: #Movement of columns 3 and 4  
        globals()[target].place(x = xvalue, y = yvalue - 100)
        ActionPoint -= 1
    elif yvalue >= 220 and xvalue >= 300 and xvalue <= 600: #Movement of columns 2 and 5
        globals()[target].place(x = xvalue, y = yvalue - 100)
        ActionPoint -= 1
    elif yvalue >= 320 and xvalue >= 200 and xvalue <= 700: #Movement of columns 1 and 6
        globals()[target].place(x = xvalue, y = yvalue - 100)
        ActionPoint -= 1
    else:
        tk.messagebox.showwarning(title='Alert',message='Cannot move up.')
def Down():
    global CurrPlayer
    global ActionPoint
    global c1label
    global c2label
    global c3label
    global c4label
    target = 'c' + str(CurrPlayer) + 'label'
    xvalue = globals()[target].winfo_x()
    yvalue = globals()[target].winfo_y()
    if yvalue <= 420 and xvalue >= 400 and xvalue <= 500:
        globals()[target].place(x = xvalue, y = yvalue + 100)
        ActionPoint -= 1
    elif yvalue <= 320 and xvalue >= 300 and xvalue <= 600:
        globals()[target].place(x = xvalue, y = yvalue + 100)
        ActionPoint -= 1
    elif yvalue <= 220 and xvalue >= 200 and xvalue <= 700:
        globals()[target].place(x = xvalue, y = yvalue + 100)
        ActionPoint -= 1
    else:
        tk.messagebox.showwarning(title='Alert',message='Cannot move down.')
def Left():
    global CurrPlayer
    global ActionPoint
    global c1label
    global c2label
    global c3label
    global c4label
    target = 'c' + str(CurrPlayer) + 'label'
    xvalue = globals()[target].winfo_x()
    yvalue = globals()[target].winfo_y()
    if xvalue >= 300 and yvalue >= 220 and yvalue <= 320:
        globals()[target].place(x = xvalue - 100, y = yvalue)
        ActionPoint -= 1
    elif xvalue >= 400 and yvalue >= 120 and yvalue <= 420:
        globals()[target].place(x = xvalue - 100, y = yvalue)
        ActionPoint -= 1
    elif xvalue >= 500 and yvalue >= 20 and yvalue <= 520:
        globals()[target].place(x = xvalue - 100, y = yvalue)
        ActionPoint -= 1
    else:
           tk.messagebox.showwarning(title='Alert',message='Cannot move left.')
def Right():
    global CurrPlayer
    global ActionPoint
    global c1label
    global c2label
    global c3label
    global c4label
    target = 'c' + str(CurrPlayer) + 'label'
    xvalue = globals()[target].winfo_x()
    yvalue = globals()[target].winfo_y()
    if xvalue <= 600 and yvalue >= 220 and yvalue <= 320:
        globals()[target].place(x = xvalue + 100, y = yvalue)
        ActionPoint -= 1
    elif xvalue <= 500 and yvalue >= 120 and yvalue <= 420:
        globals()[target].place(x = xvalue + 100, y = yvalue)
        ActionPoint -= 1
    elif xvalue <= 400 and yvalue >= 20 and yvalue <= 520:
        globals()[target].place(x = xvalue + 100, y = yvalue)
        ActionPoint -= 1
    else:
           tk.messagebox.showwarning(title='Alert',message='Cannot move right.')
    
    
#------------------------------------------------------------------------------------------------------------------------------------
def getinput():
    global NumPlayers
    global WaterTick
    global C1Char
    global C2Char
    global C3Char
    global C4Char
    Difficulty = difficultyvariable.get() ## 1 = Beginner, 2 = Novice, 3 = Medium, 4 = Hard, 5 = Legendary
    NumPlayers = playernumvariable.get() #  2 = 2 players, 3 = 3 players, 4 = 4 players

    #Dealing Cards to Players
    #CurrentTreasureCards are the cards in the current game
    CurrentTreasureCards = TreasureCards[:]
    CurrentCharacter = Characters[:]
    if NumPlayers  >= 2 and len(C1) == 0 and len(C2) == 0:
        for i in range (0,2):
            temp = random.randint(0,len(CurrentTreasureCards)-1)
            while CurrentTreasureCards[temp] == 'WatersRise':
                temp = random.randint(0,len(CurrentTreasureCards)-1)
            C1.append(CurrentTreasureCards[temp])
            CurrentTreasureCards.remove(CurrentTreasureCards[temp])
        for i in range (0,2):
            temp = random.randint(0,len(CurrentTreasureCards)-1)
            while CurrentTreasureCards[temp] == 'WatersRise':
                temp = random.randint(0,len(CurrentTreasureCards)-1)
            C2.append(CurrentTreasureCards[temp])
            CurrentTreasureCards.remove(CurrentTreasureCards[temp])
        #Give players a role
        temp = random.randint(0,len(CurrentCharacter)-1)
        C1Char = CurrentCharacter[temp]
        CurrentCharacter.remove(CurrentCharacter[temp])
        temp = random.randint(0,len(CurrentCharacter)-1)
        C2Char = CurrentCharacter[temp]
        CurrentCharacter.remove(CurrentCharacter[temp])

    if NumPlayers >= 3 and len(C3) == 0:
        for i in range (0,2):
            temp = random.randint(0,len(CurrentTreasureCards)-1)
            while CurrentTreasureCards[temp] == 'WatersRise':
                temp = random.randint(0,len(CurrentTreasureCards)-1)
            C3.append(CurrentTreasureCards[temp])
            CurrentTreasureCards.remove(CurrentTreasureCards[temp])
        temp = random.randint(0,len(CurrentCharacter)-1)
        C3Char = CurrentCharacter[temp]
        CurrentCharacter.remove(CurrentCharacter[temp])

    if NumPlayers == 4 and len(C4) == 0:
            for i in range (0,2):
                temp = random.randint(0,len(CurrentTreasureCards)-1)
                while CurrentTreasureCards[temp] == 'WatersRise':
                    temp = random.randint(0,len(CurrentTreasureCards)-1)
                C4.append(CurrentTreasureCards[temp])
                CurrentTreasureCards.remove(CurrentTreasureCards[temp])
            temp = random.randint(0,len(CurrentCharacter)-1)
            C4Char= CurrentCharacter[temp]
            CurrentCharacter.remove(CurrentCharacter[temp])
    #Set WaterTick
    WaterTick = Difficulty
    if WaterTick == 2:
        watertick.configure(image = water1)
    elif WaterTick == 3:
        watertick.configure(image = water2)
    elif WaterTick == 4:
        watertick.configure(image = water3)
    elif WaterTick == 5:
        watertick.configure(image = water4)

    SpawnPlayers()
    gamepage.tkraise()   

#Creating Frames------------------------------------------------------------------------------------------------------------------------------------  
gamepage = tk.Frame(root,bg='black',height=1000,width=1000)
gamepage.place(x=0,y=0)
optionpage = tk.Frame(root,bg='black',height=1000,width=1000)
optionpage.place(x=0,y=0)
difficultypage = tk.Frame(root,bg='black',height=1000,width=1000)
difficultypage.place(x=0,y=0)
menupage = tk.Frame(root,bg='black',height=1000,width=1000)
menupage.place(x=0,y=0)

#MenuPage Setup------------------------------------------------------------------------------------------------------------------------------------  
coverlabel = tk.Label(menupage,image=rulebookcover)
coverlabel.place(x=150,y=65)

Start = tk.Button(menupage, height = 3,width=20,text = "Start Game", bg = "#9907b7",command=difficultypage.tkraise)
Start.place(x=700,y=220)

Rules = tk.Button(menupage, height = 3,width=20, text = "Rules", bg = "#de6009",command=startrules)
Rules.place(x=700,y=280)

Options = tk.Button(menupage, height = 3,width=20,text = "Options", bg = "#e87a1a",command=optionpage.tkraise)
Options.place(x=700,y=340)

Exit = tk.Button(menupage, height = 3,width=20, text = "Exit", bg = "#e0da05",command=Close)
Exit.place(x=700,y=400)


#DifficultyPage Setup------------------------------------------------------------------------------------------------------------------------------------  
difficultyvariable  = IntVar()
difficultylabel=Label(difficultypage, text="Difficulty:",fg='white',bg='black')
difficultylabel.place(x=500,y=100)
check1=Checkbutton(difficultypage, text="Beginner", variable = difficultyvariable , onvalue = 1,fg='white',bg='black',selectcolor='black')
check1.place(x=490,y=120)
check2=Checkbutton(difficultypage, text="Novice", variable = difficultyvariable, onvalue = 2,fg='white',bg='black',selectcolor='black')
check2.place(x=490,y=140)
check3=Checkbutton(difficultypage, text="Medium", variable = difficultyvariable, onvalue = 3,fg='white',bg='black',selectcolor='black')
check3.place(x=490,y=160)
check4=Checkbutton(difficultypage, text="Hard", variable = difficultyvariable, onvalue = 4,fg='white',bg='black',selectcolor='black')
check4.place(x=490,y=180)
check5=Checkbutton(difficultypage, text="Legendary", variable = difficultyvariable, onvalue = 5,fg='white',bg='black',selectcolor='black')
check5.place(x=490,y=200)

playernumvariable  = IntVar()
pNumLabel=Label(difficultypage, text="Number of players:",fg='white',bg='black')
pNumLabel.place(x=475,y=220)
check6=Checkbutton(difficultypage, text="2", variable = playernumvariable, onvalue = 2,fg='white',bg='black',selectcolor='black')
check6.place(x=515,y=240)
check7=Checkbutton(difficultypage, text="3", variable = playernumvariable, onvalue = 3,fg='white',bg='black',selectcolor='black')
check7.place(x=515,y=260)
check8=Checkbutton(difficultypage, text="4", variable = playernumvariable, onvalue = 4,fg='white',bg='black',selectcolor='black')
check8.place(x=515,y=280)

continuebutton=Button(difficultypage, text='Continue', command=getinput,fg='white',bg='black')
continuebutton.place(x=505,y=300)
difficultyback=Button(difficultypage, text='Back', command=menupage.tkraise,fg='white',bg='black')
difficultyback.place(x=505,y=325)


#Gamepage Setup------------------------------------------------------------------------------------------------------------------------------------  
FloodButton = Button(gamepage, image = FloodDeck, command = FloodDeckDraw, borderwidth = 1)
FloodButton.place(x = 100, y = 600)

TreasureButton= Button(gamepage, image=hearthstone,command= DrawTreasure,borderwidth=0)
TreasureButton.place(x = 100, y =500)

#MovementButtons
UpButton = Button(gamepage, text = 'Up', command = Up)
UpButton.place(x = 700, y = 600)

DownButton = Button(gamepage, text = 'Down', command = Down)
DownButton.place(x = 730, y = 600)

LeftButton = Button(gamepage, text = 'Left', command = Left)
LeftButton.place(x = 700, y = 620)

RightButton = Button(gamepage, text = 'Right', command = Right)
RightButton.place(x = 730, y = 620)

watertick = Label(gamepage,image=water0)
watertick.place(x = 900,y=0)

gameback = tk.Button(gamepage,text = "Back", bg = "#9907b7",command=difficultypage.tkraise)
gameback.place(x=0,y=0)


#Board
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard1=tk.Label(gamepage, borderwidth = 2, relief = "solid", image=globals()[temptilename], text=temptilename)
mapcard1.place(x= 400 , y= 20)
#Row 1x2
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard2=tk.Label(gamepage, borderwidth = 2, relief = "solid", image=globals()[temptilename], text=temptilename)
mapcard2.place(x= 500 , y= 20)
#Row2x1
xcoor= 300
ycoor = 120
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard3=tk.Label(gamepage,borderwidth = 2, relief = "solid", image=globals()[temptilename], text=temptilename)
mapcard3.place(x=300 , y= 120)
#Row2x2
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard4=tk.Label(gamepage,borderwidth = 2, relief = "solid", image=globals()[temptilename], text=temptilename)
mapcard4.place(x=400 , y= 120)
#Row2x3
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard5=tk.Label(gamepage,borderwidth = 2, relief = "solid", image=globals()[temptilename], text=temptilename)
mapcard5.place(x=500 , y= 120)
#Row2x4
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard6=tk.Label(gamepage,borderwidth = 2, relief = "solid", image=globals()[temptilename], text=temptilename)
mapcard6.place(x=600 , y= 120)
xcoor = xcoor+100
#Row3x1
xcoor = 200
ycoor = 220
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard7=tk.Label(gamepage,borderwidth = 2,  relief = "solid", image=globals()[temptilename], text=temptilename)
mapcard7.place(x=200 , y= 220)
#Row3x2
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard8=tk.Label(gamepage,borderwidth = 2,  relief = "solid", image= globals()[temptilename], text=temptilename)
mapcard8.place(x=300 , y= 220)
#Row3x3
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard9=tk.Label(gamepage,borderwidth = 2,  relief = "solid", image=globals()[temptilename], text=temptilename)
mapcard9.place(x=400 , y= 220)
#Row3x4
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard10=tk.Label(gamepage,borderwidth = 2,  relief = "solid", image=globals()[temptilename], text=temptilename)
mapcard10.place(x=500 , y= 220)
#Row3x5
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard11=tk.Label(gamepage,borderwidth = 2,  relief = "solid", image= globals()[temptilename], text=temptilename)
mapcard11.place(x=600 , y= 220)
#Row3x6
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard12=tk.Label(gamepage,borderwidth = 2,  relief = "solid", image= globals()[temptilename], text=temptilename)
mapcard12.place(x=700 , y= 220)
#Row4x1
xcoor = 200
ycoor = 320
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard13=tk.Label(gamepage,borderwidth = 2, relief = "solid", image= globals()[temptilename], text=temptilename)
mapcard13.place(x=200 , y= 320)
#Row4x2
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard14=tk.Label(gamepage,borderwidth = 2, relief = "solid", image= globals()[temptilename], text=temptilename)
mapcard14.place(x=300 , y= 320)
#Row4x3
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard15=tk.Label(gamepage,borderwidth = 2,  relief = "solid", image= globals()[temptilename], text=temptilename)
mapcard15.place(x=400 , y= 320)
#Row4x4
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard16=tk.Label(gamepage,borderwidth = 2,  relief = "solid", image= globals()[temptilename], text=temptilename)
mapcard16.place(x=500 , y= 320)
#Row4x5
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard17=tk.Label(gamepage,borderwidth = 2, relief = "solid",image= globals()[temptilename], text=temptilename)
mapcard17.place(x=600 , y= 320)
#Row4x6
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard18=tk.Label(gamepage,borderwidth = 2,  relief = "solid", image= globals()[temptilename], text=temptilename)
mapcard18.place(x=700 , y= 320)
#Row5x1
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard19=tk.Label(gamepage,borderwidth = 2,  relief = "solid", image= globals()[temptilename], text=temptilename)
mapcard19.place(x=300 , y= 425)
#Row5x2
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard20=tk.Label(gamepage,borderwidth = 2,  relief = "solid", image= globals()[temptilename], text=temptilename)
mapcard20.place(x=400 , y= 425)
#Row5x3
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard21=tk.Label(gamepage,borderwidth = 2,  relief = "solid", image= globals()[temptilename], text=temptilename)
mapcard21.place(x=500 , y= 425)
#Row5x4
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard22=tk.Label(gamepage,borderwidth = 2,  relief = "solid", image=globals()[temptilename], text=temptilename)
mapcard22.place(x=600 , y= 425)
#Row6x1
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard23=tk.Label(gamepage, borderwidth = 2,  relief = "solid", image=globals()[temptilename], text=temptilename)
mapcard23.place(x=400 , y= 530)
#Row6x2
temptilename = random.choice(TileNames)
TileNames.remove(temptilename)
CurrentGameTile.append(temptilename)
TileOrder.append(temptilename)
mapcard24=tk.Label(gamepage, borderwidth = 2,  relief = "solid", image=globals()[temptilename], text=temptilename)
mapcard24.place(x=500 , y= 530)

#Rulepage Setup------------------------------------------------------------------------------------------------------------------------------------  
#p1 = Page 1
p1 = Button(rulewindow, text ="Page 1", bg='white', fg='black', height=3,width=7, command = page1)
p1.place(x=200, y=70)
p2 = Button(rulewindow, text ="Page 2", bg='white', fg='black', height=3,width=7, command = page2)
p2.place(x=200, y=140)
p3 = Button(rulewindow, text ="Page 3", bg='white', fg='black', height=3,width=7, command = page3)
p3.place(x=200, y=210)
p4 = Button(rulewindow, text ="Page 4", bg='white', fg='black', height=3,width=7, command = page4)
p4.place(x=200, y=280)
p5 = Button(rulewindow, text ="Page 5", bg='white', fg='black', height=3,width=7, command = page5)
p5.place(x=200, y=350)
p6 = Button(rulewindow, text ="Page 6", bg='white', fg='black', height=3,width=7, command = page6)
p6.place(x=200, y=420)
p7 = Button(rulewindow, text ="Page 7", bg='white', fg='black', height=3,width=7, command = page7)
p7.place(x=200, y=490)
p8 = Button(rulewindow, text ="Page 8", bg='white', fg='black', height=3,width=7, command = page8)
p8.place(x=200, y=560)


#Optionpage Setup------------------------------------------------------------------------------------------------------------------------------------  
optionback = tk.Button(optionpage,height = 3,width=20,text = "Back", bg = "#9907b7",command=menupage.tkraise)
optionback.place(x=100,y=100)


rulewindow.withdraw()#Hide the rule window to begin with

changeFloodTile()#To set the first 6 tile cards appended into FloodDiscard by ini()

root.mainloop()
