#!/usr/bin/env python
# -*- coding: utf-8 -*-

maxPosition = 0
totalPositions = 0
birdNames = {1: "Green head", 2: "Red head", 3: "Blue head", 4: "Spotted head", 5: "Spotted tail", 6: "Blue tail", 7: "Red tail", 8: "Green tail"}

class Tile:
    def __init__(self, side1, side2, side3, side4):
        self.sides = []
        self.sides.append(side1)
        self.sides.append(side2)
        self.sides.append(side3)
        self.sides.append(side4)
        
    def __str__(self):
        sideString = ""
        for x in self.sides:
            sideString += birdNames[x] + ", "
        return sideString[:-2]
        
    def getEdge(self, edge): # 0 = top, 1 = right, 2 = bottom, 3 = left
    		if edge == 0:
    			return self.sides[0]
    		elif edge == 1:
    			return self.sides[1]
    		elif edge == 2:
    			return self.sides[2]
    		elif edge == 3:
    			return self.sides[3]
    		else:
    			return null

class Edge:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
    def __str__(self):
        return (birdNames[self.side1] + " " + birdNames[self.side2])

class Placement: # rotation: 0 = not rotated, 1 = rotated 90° clockwise, 2 = 180°, 3 = 270°

    def __init__(self, baseTile, rotation):
        if rotation == 0:
            self.virtualTile = Tile(baseTile.sides[0], baseTile.sides[1], baseTile.sides[2], baseTile.sides[3])
        elif rotation == 1:
            self.virtualTile = Tile(baseTile.sides[3], baseTile.sides[0], baseTile.sides[1], baseTile.sides[2])
        elif rotation == 2:
            self.virtualTile = Tile(baseTile.sides[2], baseTile.sides[3], baseTile.sides[0], baseTile.sides[1])
        elif rotation == 3:
            self.virtualTile = Tile(baseTile.sides[1], baseTile.sides[2], baseTile.sides[3], baseTile.sides[0])
    def getEdge(self, edge):
        return self.virtualTile.getEdge(edge)
    def __str__(self):
        return str(self.virtualTile)

class Grid:
    def __init__(self):
        self.positionArray = [None] * 9
    
    def place(self, placement, location): 
        if (location % 3 != 0): # If the tile is in the middle column or right, check that its left edge matches
            if placement.getEdge(3) + self.positionArray[location - 1].getEdge(1) != 9:
                return False
        if (location > 2): # If the tile isn't in the first row, check that its top edge matches 
            if placement.getEdge(0) + self.positionArray[location - 3].getEdge(2) != 9:
                return False
                
        self.positionArray[location] = placement
        return True
        
    def remove(self, location):
        self.positionArray[location] = None       
    
    def __str__(self):
        s = ""
        for i in range(0, 8):
            s += "Tile " + str(i) + ":" + str(self.positionArray[i]) + "\n"
        return s

def addToGrid(grid, positionIndex, remainingTiles):
    global maxPosition
    global totalPositions
    if positionIndex > maxPosition:
        print "Found grid of " + str(positionIndex) + " tiles:\n"
        print str(grid) + "---"
        maxPosition = positionIndex
    for i in remainingTiles:
        for j in range(4):
            if grid.place(Placement(i, j), positionIndex):
                if (positionIndex == 8): ## if we placed it correctly and we're on the final spot, we're done
                    print grid
                    return True
                newTiles = []
                for k in remainingTiles:
                    if k != i:
                        newTiles.append(k)
                validPosition = addToGrid(grid, positionIndex+1, newTiles)
                if validPosition:
                    return True
    totalPositions += 1
    return False # we were not able to add the tile


tiles = [None] * 9
# 1 green head
# 2 red head
# 3 blue head
# 4 spotted head
# 5 spotted tail
# 6 blue tail
# 7 red tail
# 8 green tail

tiles[0] = Tile(1, 7, 5, 6)
tiles[1] = Tile(8, 4, 8, 2)
tiles[2] = Tile(3, 4, 2, 8)
tiles[3] = Tile(6, 7, 1, 5)
tiles[4] = Tile(2, 5, 8, 6)
tiles[5] = Tile(7, 5, 2, 3)
tiles[6] = Tile(4, 6, 8, 2)
tiles[7] = Tile(5, 1, 6, 3)
tiles[8] = Tile(1, 3, 5, 7)

grid = Grid()
foundSolution = addToGrid(grid, 0, tiles)
print "Was a solution found? " + str(foundSolution)