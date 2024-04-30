import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Skeleton")
icon = pygame.image.load('images/3792031_halloween_horror_skeleton_skull_icon.png')
pygame.display.set_icon(icon)

player = pygame.image.load('images/Без имени-1.png')
player_right = player
player_left = pygame.transform.flip(player, True, False)
background = pygame.image.load('images/imgonline-com-ua-Resize-KUuAbTSyS3GwoB.png')
health = pygame.image.load('images/360_F_487872099_QimOSUlugZRHlny2jgFHaCy5R7m0UYmT.png')

player_x = 0
player_y = 150

is_jump = False
jump_count = 5

bg_x = 0

bg_sound = pygame.mixer.Sound('sounds/caverndry_final.mp3')
jump_sound = pygame.mixer.Sound('sounds/411c45ceaa06c92.mp3')
bg_sound.play(-1)

running = True
while running:

    screen.blit(background, (bg_x, 0))
    screen.blit(background, (bg_x + 1280, 0))
    screen.blit(background, (bg_x - 1280, 0))
    screen.blit(player, (player_x, player_y))
    screen.blit(health, (-180, 540))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player = player_left
        bg_x += 2
    elif keys[pygame.K_RIGHT]:
        player = player_right
        bg_x -= 2

    if not is_jump:
        if keys[pygame.K_UP]:
            is_jump = True
    else:
        if jump_count >= -5:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 0.1
        else:
            is_jump = False
            jump_count = 5
            pygame.mixer.Sound.play(jump_sound)

    if bg_x == -1280 or bg_x == 1280:
        bg_x = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
