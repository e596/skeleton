import pygame

pygame.init()
screen = pygame.display.set_mode((1024, 512))
pygame.display.set_caption("Skeleton")
icon = pygame.image.load('images/3792031_halloween_horror_skeleton_skull_icon.png')
pygame.display.set_icon(icon)

player = pygame.image.load('images/Без имени-1.png')
player_right = player
player_left = pygame.transform.flip(player, True, False)
background = pygame.image.load('images/248880a15879483281825de6f0b4c0f4HEqGnLzIi2JXz9nc-0.png')
health = pygame.image.load('images/360_F_487872099_QimOSUlugZRHlny2jgFHaCy5R7m0UYmT.png')

player_speed = 2
player_x = 0
player_y = 0

is_jump = False
jump_count = 5

running = True
while running:

    screen.blit(background, (0, 0))
    screen.blit(player, (player_x, player_y))
    screen.blit(health, (-270, 300))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        player = player_left
    elif keys[pygame.K_RIGHT]:
        player_x += player_speed
        player = player_right

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

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
