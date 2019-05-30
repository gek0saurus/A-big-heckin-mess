import random
import PathfinderCharacterMaker
#----------------------------------------------------------
class cell (object):
    def __init__(self,ID):
        assert type(ID) == int
        self.ID = ID
    def __repr__(self):
        return celloptions(self.ID)
    def celloptions(self,option):
        options = {
            1: '#', #wall cell
            2: 'O', #player cell
            3: '.', #trail cell
            4: 'X', #goal cell
        }
        return options.get(option, ' ')
    
    def __str__(self):
        return self.celloptions(self.ID)
    def destroy(self):
        self.ID = 0
#----------------------------------------------------------
class Unit (object):
    def __init__(self,name,position,movement):
        self.name = name
        self.position = position
        self.movement = movement
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name
    def Move(self,grid,directionstring,x,y):
        for j in directionstring:
            grid[int(self.position[0])][int(self.position[1])] = cell(3)#trailcell
            self.position = ObstacleCheck(grid,self.position,j,x,y)
        return grid
                    

                    
    
#-----------------------------------------------------------
class Player(Unit):
    pass  
#----------------------------------------------------------
class NPC(Unit):
    pass
#----------------------------------------------------------   
def PrintMap(grid,playerlist):
    print("Printing map")
    text = ""
    for i in range(0,len(playerlist)):
        try:
            grid[int(playerlist[i].position[0])][int(playerlist[i].position[1])] = playerlist[i].name[:1]#player cell
        except:
           print("cannot place player " + playerlist[i].name)
    for list in grid:
        for string in list:
           text = text + str(string)
        print(text)
        text = ""
    return grid
#----------------------------------------------------------
def CreateMap(x,y,grid,numwalls):
    print("Creating map")
    Row = []
    Goal = []
    grid.clear()
    for i in range(0,x):
        Row.append(cell(0))#blankcell
    for i in range(0,y):
        grid.append(Row[:])
    for i in range(0,numwalls):
        grid[random.randint(0,y-1)][random.randint(0,x-1)] = cell(1)#wallcell
    Goal = [random.randint(0,x-1),random.randint(0,y-1)]
    return Goal
#----------------------------------------------------------
def CreatePlayer(name,position,movement,playerlist):
    print("Created player " + str(name) + " at coordinates " + str(position))
    player = Player(name,position,movement)
    playerlist.append(player)
    return playerlist
#----------------------------------------------------------


    
#----------------------------------------------------------
def ObstacleCheck(grid,position,direction,x,y):
    def moveoptions(option):
        options = {
            #[(0 = verticle 1 = horizontal), increment]
            "w": [-1,0], #Up
            "a": [0,-1], #Left
            "s": [1,0], #Down
            "d": [0,1], #Right
        }
        return options.get(option, " ")
    def detectcollision(position,destination):
        print(destination)
        if destination[0] < 0\
        or destination[1] < 0\
        or destination[0] > x-1\
        or destination[1] > y-1\
        or grid[destination[0]][destination[1]].ID == 1:#wallcell
            print("Bump")
        else:
            position = destination[:]
        return position
    move = moveoptions(direction)
    if move != " ":
        destination = position[:]
        destination[0] += move[0]
        destination[1] += move[1]
        position = detectcollision(position,destination)
        
    else:
        print("invalid input")
    return position
#----------------------------------------------------------

#----------------------------------------------------------

##grid = []
##playerlist = []
##playerlist = CreatePlayer("Carrie",[5,5],5,playerlist)
##CreateMap(20,20,grid,20)
##PrintMap(grid,playerlist)
##grid = playerlist[0].Move(grid,str(playerlist[0].name),playerlist[0].position,playerlist,"wwwwwwwwwwwwwww",20,20)
##PrintMap(grid,playerlist)









