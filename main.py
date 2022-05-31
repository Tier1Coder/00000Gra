# RV777, gra oparta na silniku 2D jakim jest Pygame

import pygame                           # sys — System-specific parameters and functions
import sys
from game import Game                   # import klasy Game z game

g = Game()                              # przypisanie klasy do zmiennej (bez tego nie działa, nie wiem czemu)

while g.running:                   # kiedy gra działa
    #if g.is_game_running == True:
    #    g.curr_menu.run_game()
    g.curr_menu.display_menu()     # wyświetl menu
    g.game_loop()                  # zapętl grę

    # poprawne zamykanie okna programu:

else:
    pygame.display.quit()       # wyjście z wyświetlania obrazu jaki generuje pygame
    pygame.quit()               # wyjście z pygame
    sys.exit()                  # wyjście z Pythona
