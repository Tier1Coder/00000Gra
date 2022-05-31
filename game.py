from menu import *      # import wszystkiego z menu
# używanie self - pozwala nam na dostęp do atrybutów i metod w klasie. Działa jak wskaźnik THIS w C++

class Game:
    def __init__(self):  # funkcja główna(inicjalizująca)
        # Po wywołaniu Game() będziemy mieli to, co jest w tej funkcji (instance), natomiast używając np.
        # zmiennej znajdującej się poza tą funkcją __init__, np. a = 10, po komendzie print(Game.a) program wypisze to,
        # co znajdzie poza funkcją __init__ (variable inside class)

        # inicjalizacja pygame
        pygame.init()

        self.running, self.playing = True, False

        #    Strzałki góra/dół           Enter           Backspace
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W = 480
        self.DISPLAY_H = 270

        # pygame object for representing images
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))

        # Initialize a window or screen for display
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))

        self.font_name = "font\\8bit_wonder\\8-BIT WONDER.TTF"
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)

        # menu.py:
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

        # menu.py - StartGame
        #self.is_game_running = False
        #self.my_game = StartGame(self)



    # TWORZENIE GRY ODBYWA SIĘ TUTAJ
    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:      # po użyciu ENTER gra kończy się
                self.playing = False
            self.display.fill(self.BLACK)
            pygame.draw.rect(self.display, 255, [200, 150, 10, 10])
            self.draw_text('Thanks for playing', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:               # co jeśli naciśniemy czerwony krzyżyk
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:            # co jeśli klawisz jest wciśnięty
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.DOWN_KEY, self.UP_KEY, self.BACK_KEY, self.START_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

