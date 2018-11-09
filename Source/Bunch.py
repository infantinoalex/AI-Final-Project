"""

Contains the Bunch class
A Bunch represents the list of tiles that are not in the players hand
or have not been played yet

"""

from Tile import Tile
from random import shuffle

class Bunch :

    def __init__(self) :
        self.bunch = []

        # Create 13 A's
        for x in range(13) :
            tile = Tile('A', 0)
            self.bunch.append(tile)

        # Create 3 B's
        for x in range(3) :
            tile = Tile('B', 0)
            self.bunch.append(tile)

        # Create 3 C's
        for x in range(3) :
            tile = Tile('C', 0)
            self.bunch.append(tile)

        # Create 6 D's
        for x in range(6) :
            tile = Tile('D', 0)
            self.bunch.append(tile)

        # Create 18 E's
        for x in range(18) :
            tile = Tile('AE', 0)
            self.bunch.append(tile)

        #Create 3 F's
        for x in range(3) :
            tile = Tile('F', 0)
            self.bunch.append(tile)
        
        # Create 4 G's
        for x in range(4) :
            tile = Tile('G', 0)
            self.bunch.append(tile)

        # Create 3 H's
        for x in range(3) :
            tile = Tile('H', 0)
            self.bunch.append(tile)

        # Create 12 I's
        for x in range(12) :
            tile = Tile('I', 0)
            self.bunch.append(tile)
        
        # Create 2 J's
        for x in range(2) :
            tile = Tile('J', 0)
            self.bunch.append(tile)

        # Create 2 K's
        for x in range(2) :
            tile = Tile('K', 0)
            self.bunch.append(tile)

        # Create 5 L's
        for x in range(5) :
            tile = Tile('L', 0)
            self.bunch.append(tile)

        # Create 3 M's
        for x in range(3) :
            tile = Tile('M', 0)
            self.bunch.append(tile)

        #Create 8 N's
        for x in range(8) :
            tile = Tile('F', 0)
            self.bunch.append(tile)

        # Create 11 O's
        for x in range(11) :
            tile = Tile('O', 0)
            self.bunch.append(tile)

        # Create 3 P's
        for x in range(3) :
            tile = Tile('P', 0)
            self.bunch.append(tile)

        # Create 2 Q's
        for x in range(2) :
            tile = Tile('Q', 0)
            self.bunch.append(tile)

        # Create 9 R's
        for x in range(9) :
            tile = Tile('R', 0)
            self.bunch.append(tile)

        # Create 6 S's
        for x in range(6) :
            tile = Tile('S', 0)
            self.bunch.append(tile)

        # Create 9 T's
        for x in range(9) :
            tile = Tile('T', 0)
            self.bunch.append(tile)

        # Create 6 U's
        for x in range(6) :
            tile = Tile('U', 0)
            self.bunch.append(tile)

        # Create 3 V's
        for x in range(3) :
            tile = Tile('V', 0)
            self.bunch.append(tile)

        # Create 3 W's
        for x in range(3) :
            tile = Tile('W', 0)
            self.bunch.append(tile)

        # Create 2 X's
        for x in range(2) :
            tile = Tile('X', 0)
            self.bunch.append(tile)

        # Create 3 Y's
        for x in range(3) :
            tile = Tile('Y', 0)
            self.bunch.append(tile)

        # Create 2 Z's
        for x in range(2) :
            tile = Tile('Z', 0)
            self.bunch.append(tile)

        for x in range(10) :
            shuffle(self.bunch)

    def GetBunch(self) :
        return self.bunch

    def IsBunchEmpty(self) :
        return not self.bunch

    def DealFromBunch(self, numberOfTiles) :
        if len(self.bunch) < numberOfTiles :
            numberOfTiles = self.bunch.count

        dealtTiles = []

        for x in range(numberOfTiles) :
            dealtTiles.append(self.bunch.pop())

        return dealtTiles
        