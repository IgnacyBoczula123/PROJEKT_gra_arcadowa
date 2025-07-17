import pygame

pygame.init()
WIDTH, HEIGHT = 1300, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

STATE_MENU = "menu"
STATE_PLAYING = "playing"
STATE_QUIT = "quit"
STATE_PAUSE   = "pause"
STATE_HIGHSCORES  = "highscores"
STATE_DIFFICULTY_OPTIONS = 'DIFFICULTY'

def menu_loop():
    from funkcje import draw_text
    from path_func import Load_graphics
    Title_img = pygame.image.load(Load_graphics("Title.png")).convert_alpha()
    selected = 0
    options = ["Start", "Najlepsze wyniki", 'Poziom trudnosci', "Wyjście"]
    bg_menu_img = pygame.image.load(Load_graphics("background_menu.jpg")).convert()
    bg_menu_img = pygame.transform.scale(bg_menu_img, (WIDTH, HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return STATE_QUIT
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    choice = options[selected]
                    if choice == "Start":
                        return STATE_PLAYING
                    elif choice == "Najlepsze wyniki":
                        return STATE_HIGHSCORES
                    elif choice == 'Poziom trudnosci':
                        return STATE_DIFFICULTY_OPTIONS
                    elif choice == "Wyjście":
                        return STATE_QUIT
        screen.blit(bg_menu_img, (0,0))
        screen.blit(Title_img, (WIDTH//2-220,0))
        for i, option in enumerate(options):
            color = (153,222,97) if i == selected else (64, 64, 64)
            draw_text(screen, option, (WIDTH // 2, 300 + i * 60), size=48, color=color)

        pygame.display.flip()
        clock.tick(60)

def Pause_loop():
    from funkcje import draw_text
    from path_func import Load_graphics
    options = ["Kontynuuj", "Wyjdź do menu"]
    selected = 0
    bg_Pause_img = pygame.image.load(Load_graphics("background.jpg")).convert()
    bg_Pause_img = pygame.transform.scale(bg_Pause_img, (WIDTH, HEIGHT))
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return STATE_QUIT
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif e.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif e.key == pygame.K_RETURN:
                    if options[selected] == "Kontynuuj":
                        return STATE_PLAYING
                    else:
                        return STATE_MENU
        
        screen.blit(bg_Pause_img, (0,0))
        draw_text(screen,"PAUZA", (WIDTH//2, 150), color=(200,200,200))
        for i, opt in enumerate(options):
            col = (153,222,97) if i == selected else (64, 64, 64)
            draw_text(screen, opt, (WIDTH//2, 350 + i*60),color=col)

        pygame.display.flip()
        clock.tick(60)

def highscores_loop():
    from funkcje import draw_text, load_highscores, draw_centered_text
    from path_func import Load_graphics
    highscores = load_highscores()
    bg_img = pygame.image.load(Load_graphics("background_menu.jpg")).convert()
    bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return STATE_QUIT
            elif event.type == pygame.KEYDOWN:
                # ESC lub ENTER – powrót do menu
                if event.key in (pygame.K_ESCAPE, pygame.K_RETURN):
                    return STATE_MENU

        screen.blit(bg_img, (0, 0))

        draw_text(screen, 'Najlepsze wyniki ',(WIDTH//2, 80),64)
    
        wyniki = []
        for i, entry in enumerate(highscores, start=1):
            wyniki.append(f"{i}. {entry['score']}")
        draw_centered_text(screen, wyniki, WIDTH//2, 400)

        draw_text(screen, 'Naciśnij ESC lub ENTER, aby wrócić',(WIDTH//2, HEIGHT - 50))

        pygame.display.flip()
        clock.tick(60)

def difficulty_loop():
    from funkcje import draw_text
    from path_func import Load_graphics

    options = ['Easy', 'Normal', 'Hard']
    selected = 0

    bg_menu_img = pygame.image.load(Load_graphics("background_menu.jpg")).convert()
    bg_menu_img = pygame.transform.scale(bg_menu_img, (WIDTH, HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return STATE_QUIT, None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)

                elif event.key == pygame.K_ESCAPE:
                    return STATE_MENU, None

                elif event.key == pygame.K_RETURN:
                    chosen = options[selected].lower()
                    return STATE_PLAYING, chosen

        screen.blit(bg_menu_img, (0,0))
        draw_text(screen, 'Wybierz poziom trudności i zacznij gre', (WIDTH//2, 200), size=48)
        draw_text(screen, 'Naciśnij ESC, aby wrócić', (WIDTH//2, HEIGHT - 50), size=32)

        for i, option in enumerate(options):
            color = (153,222,97) if i == selected else (64, 64, 64)
            draw_text(screen, option,(WIDTH // 2, 300 + i * 60),size=48, color=color)

        pygame.display.flip()
        clock.tick(60)
