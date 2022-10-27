# Import pyray
import pyray

# Create a keyboard service class
class keyboard_service():
    # Create the keyboard functions
    def __init__(self, cell_size=1):
        self._cell_size = cell_size
        self.x = 0
        self.y = 0

    # Implement the character's move
    def get_direction(self):
        x = 0
        if pyray.is_key_down(pyray.KEY_LEFT):
            x = -1
        elif pyray.is_key_down(pyray.KEY_RIGHT):
            x = 1
        return x