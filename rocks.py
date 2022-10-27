# Import class colors
from colors import colors

# Create a symbol class
class symbol():
    x = 0
    y = 0
    color = None
    text = "X"
    colors = colors()

    # Create the init function
    def __init__(self, x, y, color, text):
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        if color not in self.colors.return_colors():
            raise Exception("Color is not available")
    
    # Get the colors
    def get_colors(self):
        if self.color == "red":
            return self.colors.return_red()
        elif self.color == "white":
            return self.colors.return_white()
        elif self.color == "gray":
            return self.colors.return_gray()

# Create a gem class and the symbols
class gem(symbol):
    def __init__(self, x, y):
        super().__init__(x, y, "red", "*")

    # Return the score
    def get_score(self):
        return 1

# Create a rock class and the symbols
class rock(symbol):
    def __init__(self, x, y):
        super().__init__(x, y, "white", "O")

    # Return the score
    def get_score(self):
        return -1