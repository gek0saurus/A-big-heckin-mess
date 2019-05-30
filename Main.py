import GridMove
import PathfinderCharacterMaker
import Commands
walls = 20
grid = []
playerlist = []
userinput = ""
position = []
mapcreated = False


print("Commands:")
print("createmap")
print("printmap")
print("createplayer")
print("moveplayer")
print("Sorry, there's no help option yet :(")
print(" ")
## find a better way to sort input options
## put input validation into functions
## Grid system is a little wonky, figure out how to make that an object class
## Make custom map input instead of random maps

while userinput!= "end":
    userinput = input("Input Command")
        
    #---------------------------------------------------

    if userinput == "createmap":
        validinput = False
        while validinput == False:
            x = int(input("map width?"))
            try:
                x = int(x)
                validinput = True
            except:
                print("Input must be integer")
        validinput = False
        while validinput == False:
            y = int(input("map height?"))
            try:
                y = int(y)
                validinput = True
            except:
                print("Input must be integer")
        GridMove.CreateMap(x,y,grid,walls)
        mapcreated = True
    #---------------------------------------------------
    elif userinput == "printmap":
        if mapcreated == True:
            grid = GridMove.PrintMap(grid,playerlist)
        else:
            print("Use createmap first")
    #----------------------------------------------------

    elif userinput == "moveplayer":
        foundplayer = False
        while foundplayer == False:
            print(playerlist)
            nameofmovedplayer = input("Move who?")
            for i in playerlist:
                if nameofmovedplayer == i.name:
                    movedplayer = i
                    foundplayer = True
            if foundplayer == False:
                print("Cannot find player")
        directionstring = str()
        directionstring = input("You can move " + str(movedplayer.movement) + " spaces. (enter wasd directions)")
        movedplayer.Move(grid,directionstring,x,y)      

    #----------------------------------------------------
        
    elif userinput == "createplayer":
        validinput = False
        while validinput == False:  
            playername = input("Player name?")
            if any(playername in str(s) for s in playerlist):
               print("Name taken")
            else:
                validinput = True
        validinput = False
        while validinput == False:
            playerlocation = list()
            playerlocationstring =(input("Player location?"))
            splitplayerlocationstring = list(playerlocationstring.split(","))
            try:
                playerlocationintegers = map(int,splitplayerlocationstring)
                playerlocation = list(playerlocationintegers)
                print(playerlocation)
                coordsareintegers = True
            except:
                coordsareintegers = False
            if len(playerlocation) == 2 and coordsareintegers == True:
                validinput = True
            else:
                print("player location must two integers separated by ','")               
        playerlist = GridMove.CreatePlayer(playername,playerlocation,5,playerlist)
        #The 5 is a temporary placeholder for movement
    #------------------------------------------------------
    
    else:
        print("invalidinput")  





print("Good bye <3")
