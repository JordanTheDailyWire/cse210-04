# Import keyboard service, video service, character, and symbol
from symbols import symbol
from character import character
from video import video_service
from keyboard import keyboard_service
from time import sleep

# Create a director class
class director():
    def __init__(self):
        self.score = 0

    # Get input from the user
    def user_input(self):
        question = input("Greed is the hardest game is, it seems like you want to play this hard game. Do you accept the challenge? ")
        if question != "y":
            exit()

    # Update the character's position and score
    def update_position(self, symbols, visual_studio):
        for symbol in symbols.symbols:
            if isinstance(symbol, character):
                continue
            if symbol.y < 39:
                symbol.y += 1
            else:
                symbol.y = 0

        score = symbols.character_results(0)
        if score:
            visual_studio.set_score(score)
    
    # Start the Greed game
    def start_game(self):
        self.user_input()
        visual_studio = video_service()
        visual_studio.open_window()
        symbols = symbol()
        keyboard = keyboard_service()
        time = 0
        frame = 0.05
        while visual_studio.game():
            visual_studio.display_grid(symbol)
            xd = keyboard.get_direction()
            if xd != 0:
                score = symbols.player_position()
                if score:
                    visual_studio.set_score(score)
                sleep(frame)
                time += frame
                if time > 1.0:
                    self.update_position(symbols, visual_studio)
                    time = 0.0
                visual_studio.close_window()