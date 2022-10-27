# Import pyray
import pyray

# Create a video service class
class video_service():
    # Create a keyboard service input
    def __init__(self):
        x, y = self.cell_size()
        self.width = x * 60
        self.height = y * 40
        self.score = 0

    # Create a window with pyray
    def window(self):
        pyray.init_window(self.width, self.height, "Greed")
        pyray.set_target_fps(20)
        pyray.clear_background(pyray.black)
        pyray.begin_drawing()

    # Create the cell size
    def cell_size():
        return 20, 20

    # Get the grid width
    def get_width(self):
        return self.width

    # Get the grid height
    def get_height(self):
        return self.height

    # Display the grid
    def display_grid(self, symbols, x, y):
        pyray.clear_background(pyray.black)
        pyray.begin_drawing()
        for symbol in symbols.symbols:
            pyray.draw_text(symbol.text, symbol.x * x, symbol.y * y, x-2, symbol.display_color())
        pyray.draw_text(f"Score:{self.score}", 20, 100, 16, pyray.white)
        pyray.end_drawing()

    # Create the close window function
    def game(self):
        if pyray.window_should_close() or self.score < 0:
            return False
        return True

    # Create the player scoring
    def player_score(self, red, white, player, symbol):
        if (player.x, player.y) == (symbol.x, symbol.y):
            if symbol.stars:
                self.red = 1
                self.white = -1
            return True
        return False

    # Create the character move
    def character_move(self):
        (self.x, self.y)
        return self.x, self.y

    # Set the score
    def set_score(self):
        self.score

    # Close the window
    def close_window(self):
        pyray.close_window