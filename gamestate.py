import pygame
import sys
import time
from assetstyles import AssetStyles as ast
from art import Art
from colors import Colors

# TODO: default game states, should probably not leave this as it is 
class GameState:
    def __init__(self):
        pass

    def update(self):
        pass

    def render(self, screen):
        pass


######## TITLE SCREEN FUNCTIONALITY ########


class TitleScreenState(GameState):
    def __init__(self, game_instance):
        super().__init__()
        self.game_instance = game_instance
        self.title_font = pygame.font.SysFont("Courier New", ast.TS_TITLE_FONT_SZ)
        self.option_font = pygame.font.SysFont("Courier New", ast.TS_OPTION_FONT_SZ)
        self.selection_index = 0
        self.title_options = ["New Game", "Load Game", "Options", "Quit"]

    def update(self):
        self.handle_events()

    def render(self, screen):
        screen.fill(Colors.BLACK)

        title_art_lines = Art.get_title_art()
        side_tree_art_lines = Art.get_side_tree_art()
        title_line_height = ast.TS_TITLE_FONT_SZ + ast.TS_TITLE_SPACING

        start_y = (ast.SCREEN_HEIGHT // 3) - (len(title_art_lines) * title_line_height) // 2

        for i, line in enumerate(title_art_lines):
            title_surface = self.title_font.render(line, True, Colors.WHITE)
            title_rect = title_surface.get_rect(center=(ast.SCREEN_WIDTH // 2, start_y + i * title_line_height))
            screen.blit(title_surface, title_rect)

        options_start_y = start_y + len(title_art_lines) * title_line_height + 20 

        left_art_x = ast.SCREEN_WIDTH // 4  
        right_art_x = (ast.SCREEN_WIDTH * 3) // 4  
        side_art_start_y = options_start_y

        for j, side_line in enumerate(side_tree_art_lines):
            side_surface = self.title_font.render(side_line, True, Colors.WHITE)
            side_rect = side_surface.get_rect(center=(left_art_x, side_art_start_y + j * (ast.TS_TITLE_FONT_SZ + ast.TS_TITLE_SPACING)))
            screen.blit(side_surface, side_rect)

        for j, side_line in enumerate(side_tree_art_lines):
            side_surface = self.title_font.render(side_line, True, Colors.WHITE)
            side_rect = side_surface.get_rect(center=(right_art_x, side_art_start_y + j * (ast.TS_TITLE_FONT_SZ + ast.TS_TITLE_SPACING)))
            screen.blit(side_surface, side_rect)

        for i, option in enumerate(self.title_options):
            color = Colors.RED if i == self.selection_index else Colors.WHITE
            option_surface = self.option_font.render(option, True, color)
            option_rect = option_surface.get_rect(center=(ast.SCREEN_WIDTH // 2, options_start_y + i * (ast.TS_OPTION_FONT_SZ + ast.TS_OPTION_SPACING)))
            screen.blit(option_surface, option_rect)

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.selection_index = (self.selection_index - 1) % len(self.title_options)
                elif event.key == pygame.K_s:
                    self.selection_index = (self.selection_index + 1) % len(self.title_options)
                elif event.key == pygame.K_RETURN:
                    self.select_option()

    def select_option(self):
        if self.title_options[self.selection_index] == 'New Game':
            self.game_instance.start_new_game()
        elif self.title_options[self.selection_index] == 'Load Game':
            x = 0 # placeholder
        elif self.title_options[self.selection_index] == 'Options':
            x = 0 # placeholder
        elif self.title_options[self.selection_index] == 'Quit':
            self.game_instance.change_state("confirm_quit")


######## QUIT CONFIRMATION SCREEN FUNCTIONALITY ########


class ConfirmQuitState(GameState):
    def __init__(self, game_instance):
        super().__init__()
        self.game_instance = game_instance
        self.confirm_font = pygame.font.SysFont("Courier New", ast.QC_TITLE_FONT_SZ)
        self.confirm_options = ["Yes", "No"]
        self.selection_index = 0

    def update(self):
        self.handle_events()

    def render(self, screen):
        screen.fill(Colors.BLACK)
        confirm_surface = self.confirm_font.render("Are you sure you want to quit?", True, Colors.WHITE)
        confirm_rect = confirm_surface.get_rect(center=(ast.SCREEN_WIDTH // 2, ast.SCREEN_HEIGHT // 2 - ast.QC_TITLE_SPACING))
        screen.blit(confirm_surface, confirm_rect)

        for i, option in enumerate(self.confirm_options):
            color = Colors.RED if i == self.selection_index else Colors.WHITE
            option_surface = self.confirm_font.render(option, True, color)
            option_rect = option_surface.get_rect(center=(ast.SCREEN_WIDTH // 2, ast.SCREEN_HEIGHT // 2 + i * (ast.QC_OPTION_FONT_SZ + ast.QC_OPTION_SPACING)))
            screen.blit(option_surface, option_rect)

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.selection_index = (self.selection_index - 1) % len(self.confirm_options)
                elif event.key == pygame.K_s:
                    self.selection_index = (self.selection_index + 1) % len(self.confirm_options)
                elif event.key == pygame.K_RETURN:
                    self.select_option()

    def select_option(self):
        if self.confirm_options[self.selection_index] == 'Yes':
            pygame.quit()
            sys.exit()
        elif self.confirm_options[self.selection_index] == 'No':
            self.game_instance.change_state("title_screen")


######## INITIAL NEW GAME FUNCTIONALITY ########


class BeginNewGameState(GameState):
    def __init__(self, game_instance):
        super().__init__()
        self.game_instance = game_instance
        self.name_input = ""
        
        # Text stages
        self.text_stages = [
            "You hear a whisper. 'Hello, what is your name?'",
            "The voice replies. 'Of course, but then again, I already knew that..'",
            "The whisper fades. 'Please.. come here.'"
            " "
        ]
        self.current_stage = 0
        
        self.full_text = self.text_stages[self.current_stage]
        self.displayed_text = ""
        self.font = pygame.font.SysFont("Courier New", ast.DIALOGUE_FONT_SZ)
        self.typing_speed = 0.03
        self.last_update_time = time.time()
        
        # Name input flag
        self.awaiting_name_input = True

    def update(self):
        self.handle_events()
        self.update_displayed_text()

    def render(self, screen):
        screen.fill(Colors.BLACK)

        text_surface = self.font.render(self.displayed_text, True, Colors.CYAN)
        text_rect = text_surface.get_rect(center=(ast.CENTER_PAGE_X, (ast.CENTER_PAGE_Y // 2)))
        screen.blit(text_surface, text_rect)

        if self.awaiting_name_input:
            name_surface = self.font.render(self.name_input, True, Colors.YELLOW)
            name_rect = name_surface.get_rect(center=(ast.CENTER_PAGE_X, ast.CENTER_PAGE_Y))
            screen.blit(name_surface, name_rect)

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.awaiting_name_input:
                    # Handle name input events
                    if event.key == pygame.K_RETURN:
                        if self.name_input:
                            self.game_instance.player.name = self.name_input
                            self.advance_to_next_stage()
                    elif event.key == pygame.K_BACKSPACE:
                        self.name_input = self.name_input[:-1]
                    else:
                        self.name_input += event.unicode
                elif event.key == pygame.K_RETURN and self.current_stage < len(self.text_stages):
                    self.advance_to_next_stage()

    def update_displayed_text(self):
        if len(self.displayed_text) < len(self.full_text):
            current_time = time.time()
            if current_time - self.last_update_time >= self.typing_speed:
                self.displayed_text += self.full_text[len(self.displayed_text)]
                self.last_update_time = current_time

    def advance_to_next_stage(self):
        self.awaiting_name_input = False
        self.current_stage += 1

        if self.current_stage < len(self.text_stages):
            self.full_text = self.text_stages[self.current_stage]
            self.displayed_text = ""
            self.last_update_time = time.time()
        else:
            self.game_instance.change_state("dream_sequence")


class DreamSequenceState(GameState):
    def __init__(self, game_instance):
        super().__init__()
        self.game_instance = game_instance
        
        self.dream_map = [
            [',',',',',',',',','],
            [',',',',',',',',','],
            [',',',','S',',',','],
            ['8',',','#',',','8'],
            [',',',','#','.',','],
            ['8',',','#',',','8'],
            [',','.','#','.','.'],
            ['8',',','#','.','8'],
            ['.','.','P','.','.'],
        ]

        self.player_pos = [8, 2]
        self.dialogues = [
            "The woods around you whisper your name.",
            "You venture further into the timber, step by step.",
            "A strange light emits from the inky realm around you.",
            "Captivated by the uncertainty, you're drawn in closer.",
            "A sudden flash of ivory tusks blinds your vision.",
            "Frightened, but determined, you stare back at the darkness."
        ]
        self.current_dialogue_index = 0
        
        self.font = pygame.font.SysFont("Courier New", ast.DIALOGUE_FONT_SZ)

    def update(self):
        self.handle_events()
    
    def render(self, screen):
        screen.fill(Colors.BLACK)
        
        self.draw_dream_map(screen)
        
        self.draw_dialogue(screen)

        pygame.display.flip()

    def draw_dream_map(self, screen):
        tile_size = 40
        start_x = (ast.SCREEN_WIDTH - (len(self.dream_map[0]) * tile_size)) // 2
        start_y = (ast.SCREEN_HEIGHT - (len(self.dream_map) * tile_size)) // 2

        for row in range(len(self.dream_map)):
            for col in range(len(self.dream_map[row])):
                tile = self.dream_map[row][col]
                color = Colors.BLUE
                
                if tile == 'P':
                    color = Colors.LIGHT_GRAY
                elif tile == 'S':
                    color = Colors.CYAN
                elif tile == '#':
                    color = Colors.DARK_GRAY
                elif tile == ',':
                    color = Colors.PURPLE

                pygame.draw.rect(screen, color, (start_x + col * tile_size, start_y + row * tile_size, tile_size, tile_size))

    def draw_dialogue(self, screen):
        dialogue_surface = self.font.render(self.dialogues[self.current_dialogue_index], True, Colors.LIGHT_GRAY)
        dialogue_rect = dialogue_surface.get_rect(center=(ast.SCREEN_WIDTH // 2, ast.SCREEN_HEIGHT - 50))
        screen.blit(dialogue_surface, dialogue_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.move_player_up()

    def move_player_up(self):
        next_x = self.player_pos[0] - 1
        next_y = self.player_pos[1]

        if self.dream_map[next_x][next_y] == 'S':
            self.game_instance.change_state("title_screen")
            return

        if next_x >= 0:
            self.dream_map[self.player_pos[0]][self.player_pos[1]] = '#'
            self.player_pos[0] = next_x
            self.dream_map[self.player_pos[0]][self.player_pos[1]] = 'P'

            if self.current_dialogue_index < len(self.dialogues) - 1:
                self.current_dialogue_index += 1

    