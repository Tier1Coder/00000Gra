import pygame


class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

    def draw_cursor(self):
        self.game.draw_text("*", 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.start_x, self.start_y = self.mid_w, self.mid_h + 30
        self.options_x, self.options_y = self.mid_w, self.mid_h + 50
        self.credits_x, self.credits_y = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("Main Menu", 20, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 20)
            self.game.draw_text("Start Game", 20, self.start_x, self.start_y)
            self.game.draw_text("Options", 20, self.options_x, self.options_y)
            self.game.draw_text("Credits", 20, self.credits_x, self.credits_y)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.options_x + self.offset, self.options_y)
                self.state = "Options"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.credits_x + self.offset, self.credits_y)
                self.state = "Credits"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.state = "Start"
        elif self.game.UP_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.credits_x + self.offset, self.credits_y)
                self.state = "Credits"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.state = "Start"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.options_x + self.offset, self.options_y)
                self.state = "Options"

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Start":
                self.game.playing = True
                #self.game.is_game_running = True
            elif self.state == "Options":
                self.game.curr_menu = self.game.options
            elif self.state == "Credits":
                self.game.curr_menu = self.game.credits
            self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Volume"
        self.volume_x, self.volume_y = self.mid_w, self.mid_h + 20
        self.controls_x, self.controls_y = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volume_x + self.offset, self.volume_y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text("Options", 20, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 30)
            self.game.draw_text("Volume", 15, self.volume_x, self.volume_y)
            self.game.draw_text("Controls", 15, self.controls_x, self.controls_y)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == "Volume":
                self.state = "Controls"
                self.cursor_rect.midtop = (self.controls_x + self.offset, self.controls_y)
            elif self.state == "Controls":
                self.state = "Volume"
                self.cursor_rect.midtop = (self.volume_x + self.offset, self.volume_y)
        elif self.game.START_KEY:
            # TO-DO: VOLUME AND CONTROLS MENU
            pass


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("Credits", 20, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2-20)
            self.game.draw_text("Game created by Oskar Rydlicki", 10, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2+10)
            self.blit_screen()












"""/////////////////////////////////////////////////////////////////////////////////////////////"""

# Stworzyć całkowicie nową klasę i funkcje zawierające wszystko, co potrzeba do gry - jeśli chce to zrobić
# z poziomu klasy menu, to :

"""
class StartGame(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def run_game(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
                self.game.is_game_running = False
            self.game.display.fill(self.game.BLACK)
            self.blit_screen()
"""