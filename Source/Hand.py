"""

Contains the Hand class
A Hand represents all the tiles a current play can view

"""

class Hand :

    def __init__(self, playerName, tiles) :
        self.playerName = playerName
        self.tilesInHand = tiles
        return

    def GetPlayerName(self) :
        return self.playerName

    def PeekHand(self):
        return self.tilesInHand

    def AddTileToHand(self, tile) :
        self.tilesInHand.append(tile)
        return

    def AddTilesToHand(self, tiles) :
        self.tilesInHand.extend(tiles)
        return        

    def RemoveTileFromHand(self, tile) :
        for handTile in self.tilesInHand :
            if tile.GetLetter() == handTile.GetLetter() :
                self.tilesInHand.remove(handTile)
                return
            
        raise ValueError("Could not find specified tile in the list", tile)

        return

    def IsHandEmpty(self) :
        return not self.tilesInHand