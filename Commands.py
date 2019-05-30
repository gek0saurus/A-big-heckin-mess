import GridMove

def createmap(x,y,grid,walls):
    print("Creating map")
    GridMove.CreateMap(x,y,grid,walls)
    
def printmap(grid,playerlist):
    print("Printing map")
    GridMove.PrintMap(grid,playerlist)

def move(grid,position,x,y):
    input("move what?")
    GridMove.move(grid,position,x,y)
def createplayer(name,position,playerlist):
    player = GridMove.player(name,position)
    playerlist.append(player)
    return playerlist
