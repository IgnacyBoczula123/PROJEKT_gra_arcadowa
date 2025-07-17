import pygame
import sys

WIDTH, HEIGHT = 1300, 800

STATE_MENU               = "menu"
STATE_DIFFICULTY_OPTIONS = "DIFFICULTY"
STATE_PLAYING            = "playing"
STATE_HIGHSCORES         = "highscores"
STATE_QUIT               = "quit"

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumping Franek")
clock = pygame.time.Clock()

def main():

    from gameplay import game_loop
    from screens_def import menu_loop, difficulty_loop, highscores_loop
    from funkcje import play_menu_music, play_game_music, stop_music

    current_difficulty = 'normal'
    pygame.init()
    pygame.mixer.init()   
    state = STATE_MENU
    play_menu_music()

    while state != STATE_QUIT:

        if state == STATE_MENU:
            next_state = menu_loop()

            if next_state == STATE_PLAYING:
                stop_music()
                play_game_music()
            state = next_state

        elif state == STATE_DIFFICULTY_OPTIONS:

            stop_music()
            play_menu_music()

  
            next_state, chosen = difficulty_loop()


            if chosen is not None:
                current_difficulty = chosen

 
            if next_state == STATE_PLAYING:
                stop_music()
                play_game_music()

            state = next_state

        elif state == STATE_PLAYING:

            next_state = game_loop(current_difficulty)

            if next_state == STATE_MENU:
                stop_music()
                play_menu_music()

            state = next_state

        elif state == STATE_HIGHSCORES:
            stop_music()
            play_menu_music()

            next_state = highscores_loop()
            state = next_state
    clock.tick(60)
    pygame.quit()
    sys.exit()



main()
