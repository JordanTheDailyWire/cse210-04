# Import rocks and character
from rocks import symbol, gem, rock
from character import character

# Create a symbol class and the positions for the rocks
class symbol():
    symbols = []
    def __init__(self):
        gems = [(13,3),(23,5),(33,8),(4,7),(8,11),(5,15),(11,16),(39,39),(28,31),(59,30),(57,32),(52,25),(55,27),(53,29),(51,30)]
        rocks = [(2,2),(6,4),(10,6),(15,9),(5,10),(14,12),(4,14),(22,17),(21,21),(24,22),(58,26),(56,35),(49,31),(54,22),(56,12)]
        self.symbols.append(character(30, 39))
        for rock in rocks:
            self.symbols.append(rock[0], rock[1])
        for gem in gems:
            self.symbols.append(gem[0], gem[1])

    # Create the player's position
    def player_position(self, xd):
        for symbol in self.symbols:
            if isinstance(symbol, character):
                symbol.character_move(xd)
                return symbol.character_result(self)
            return None