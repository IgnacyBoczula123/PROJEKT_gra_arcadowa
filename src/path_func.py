import pygame
import os
def Load_audio_short(filename, volume = (0.1) ):
    path = os.path.join('assets', 'sounds', f'{filename}')
    shot = pygame.mixer.Sound(path)
    shot.set_volume(volume)
    return shot

def Load_audio_long(filename):
    path = os.path.join('assets', 'sounds', f'{filename}')

    return path

def Load_graphics(filename):
    path = os.path.join('assets', 'graphics', f'{filename}')
    return path
def Load_others(filename):
    path = os.path.join('assets', 'others', f'{filename}')
    return path

