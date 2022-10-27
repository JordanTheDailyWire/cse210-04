# Import colors
import colors

# Create a colors class and the colors
class colors():
    def __init__(self):
        self.red = (253, 35, 35, 1)
        self.white = (252, 252, 252, 1)
        self.gray = (66, 64, 64, 0.53)

    # Allow the colors to return
    def return_colors(self):
        return ["red, white, gray"]

    # Return the color red
    def return_red(self):
        return self.red

    # Return the color white
    def return_white(self):
        return self.white

    # Return the color gray
    def return_gray(self):
        return self.gray