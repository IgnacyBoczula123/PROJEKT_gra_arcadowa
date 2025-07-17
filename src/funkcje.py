import pygame
from klasa import Rocks
from path_func import Load_audio_long, Load_others
import json
import os
def draw_text(surface, text, pos, size=48, color=(153,222,97), center=True):
    font = pygame.font.Font(Load_others("Minecraftia-Regular.ttf"), size)
    txt_surf = font.render(text, True, color)
    txt_rect = txt_surf.get_rect()
    if center:
        txt_rect.center = pos
    else:
        txt_rect.topleft = pos
    surface.blit(txt_surf, txt_rect)

def draw_centered_text(screen, lines, center_x, center_y, line_spacing=20,color=(153,222,97),size = 48):

    font = pygame.font.Font(Load_others("Minecraftia-Regular.ttf"), size)
    rendered = [font.render(line, True, color) for line in lines]
    heights  = [surf.get_height() for surf in rendered]
    total_h = sum(heights) + line_spacing * (len(lines) - 1)
    start_y = center_y - total_h // 2
    y = start_y
    for surf in rendered:
        rect = surf.get_rect(center=(center_x, y + surf.get_height()//2))
        screen.blit(surf, rect)
        y += surf.get_height() + line_spacing


def draw_rocks(pos, num, speed=5):
    group = pygame.sprite.Group()
    for i in range(0, len(num)):
        if num[i] == 2:

           rock = (Rocks(pos=(pos[i],650),num=num[i],width=1320,speed= speed))
           group.add(rock)
        else:
            rock = (Rocks(pos=(pos[i],630),num=num[i],width=1320,speed= speed))
            group.add(rock)
    return group

def play_menu_music():
    pygame.mixer.music.load(Load_audio_long('background_2.wav'))
    pygame.mixer.music.set_volume(0.04)
    pygame.mixer.music.play(-1)    

def play_game_music():
    pygame.mixer.music.load(Load_audio_long("background.wav"))
    pygame.mixer.music.set_volume(0.04)
    pygame.mixer.music.play(-1)

def stop_music(fade_ms = 500):
    pygame.mixer_music.fadeout(fade_ms)

HS_FILE = Load_others('highscores.json')

def load_highscores(filename=HS_FILE):
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_highscores(highscores, filename=HS_FILE):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(highscores, f, ensure_ascii=False, indent=2)

def update_highscores(score,):
    scores = load_highscores()
    
    scores.append({"score": int(score)})
    
    scores = sorted(scores, key=lambda entry: entry["score"], reverse=True)

    scores = scores[:5]
        
    save_highscores(scores)


    

