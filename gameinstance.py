import pygame
import sys
from gamestate import *
from assetstyles import AssetStyles as ast
from player import Player

class GameInstance:
    def __init__(self):
        pygame.init()
        self.player = Player(name="")

        try:
            pygame.mixer.music.load("reverb.wav")
            pygame.mixer.music.play(-1)
        except pygame.error as e:
            print("Error loading music:", e)
            sys.exit()

        self.current_state = None
        self.states = {
            "title_screen": TitleScreenState(self),
            "confirm_quit": ConfirmQuitState(self),
            "component_menu": ComponentsMenuState(self),
            "text_interact": TextInteraction(self),
            "map_explore": MapExploration(self),
            "combat": CombatSystem(self),
            "begin_new_game": BeginNewGameState(self),
            "dream_sequence": DreamSequenceState(self),
            "tutorial_interaction": TutorialState(self),
        }
        self.change_state("title_screen")

    def change_state(self, state_name):
        if state_name in self.states:
            self.current_state = self.states[state_name]
        else:
            print(f"Error: State '{state_name}' does not exist.")

    def start_new_game(self):
        self.change_state("begin_new_game")
        

    def main_loop(self):
        screen = pygame.display.set_mode((ast.SCREEN_WIDTH, ast.SCREEN_HEIGHT))
        pygame.display.set_caption("Whisperwood")
        clock = pygame.time.Clock()

        while True:
            self.current_state.update()
            self.current_state.render(screen)
            pygame.display.flip()
            clock.tick(60)  # limit of 60 FPS