import pygame
from path_func import Load_audio_short, Load_graphics
class Rocks(pygame.sprite.Sprite):
    def __init__(self, pos,num ,width, speed=1):
        super().__init__()
        self.image = pygame.image.load(Load_graphics(f"rock_{num}.png")).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = speed
        self.width = width
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
           self.kill()

class Clouds(pygame.sprite.Sprite):
    def __init__(self, num,pos, width=1200, speed = 3):
        super().__init__()
        self.image = pygame.image.load(Load_graphics(f"cloud_{num}.png")).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.width = width
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < -200:
           self.rect.left = self.width



class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, run_images= [Load_graphics('Franek_1.png'),Load_graphics('Franek_2.png')], jump_image= Load_graphics('Franek_2.png') ):
        super().__init__()

        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
        self.shot_sound = Load_audio_short("jump.flac")
  
        self.run_frames = [pygame.image.load(img).convert_alpha() for img in run_images]
        self.jump_frame = pygame.image.load(jump_image).convert_alpha()
        

        self.image = self.run_frames[0]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.positon = y 
        
 
        self.vy = 0
        self.gravity = 0.6
        self.jump_strength = -16
        
        self.on_ground = True
        self.frame_index = 0
        self.animation_timer = 0
        self.animation_speed = 0.1  # im mniejsza, tym szybciej zmiana klatek

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.on_ground:
            self.shot_sound.play()
            self.vy = self.jump_strength
            self.on_ground = False

    def apply_gravity(self):
        ground_level = self.positon
        self.vy += self.gravity
        self.rect.y += int(self.vy)
        if self.rect.bottom >= ground_level:
            self.rect.bottom = ground_level
            self.vy = 0
            self.on_ground = True

    def animate(self):
        if self.on_ground:
   
            self.animation_timer += self.animation_speed
            if self.animation_timer >= len(self.run_frames):
                self.animation_timer = 0
            self.frame_index = int(self.animation_timer)
            self.image = self.run_frames[self.frame_index]
        else:
  
            self.image = self.jump_frame

    def update(self):
        self.handle_input()
        self.apply_gravity()
        self.animate()

        
