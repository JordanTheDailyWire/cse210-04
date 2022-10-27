# Import gems and rocks
from rocks import symbol, gem, rock

# Create a character class
class character(symbol):
    score = 0
    def __init__(self, x, y):
        super().__init__(x, y, "gray", "#")
    
    # Create the result of the character's hit
    def character_result(self, symbols):
        for symbol in symbols.symbols:
            if isinstance(symbol, character):
                continue
            if symbol.x == self.x and symbol.y == self.y:
                hit_gem = False
                hit_rock = False
                if isinstance(symbol, gem):
                    hit_gem = True
                elif isinstance(symbol, rock):
                    hit_rock= True
                return self.character_score(hit_gem, hit_rock)
            return None

    # Create the character's move
    def character_move(self, direction):
        if self.x == 0 and direction < 0:
            return
        if self.x == 59 and direction > 0:
            return
        self.x += direction

    # Create the character score
    def character_score(self, hit_gem):
        if hit_gem:
            self.score += 1
        else:
            self.score -= 1
        return self.score