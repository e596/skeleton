import pygame

pygame.init()
screen = pygame.display.set_mode((1024, 512))
pygame.display.set_caption("Skeleton")
icon = pygame.image.load('images/3792031_halloween_horror_skeleton_skull_icon.png')
pygame.display.set_icon(icon)

player = pygame.image.load('images/skeleton_image1.png')
player_right = player
player_left = pygame.transform.flip(player, True, False)
background = pygame.image.load('images/248880a15879483281825de6f0b4c0f4HEqGnLzIi2JXz9nc-0.png')
health = pygame.image.load('images/360_F_487872099_QimOSUlugZRHlny2jgFHaCy5R7m0UYmT.png')

player_speed = 5
player_x = 0

running = True
while running:

    screen.blit(background, (0, 0))
    screen.blit(player, (player_x, 0))
    screen.blit(health, (-270, 300))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        player = player_left
    elif keys[pygame.K_RIGHT]:
        player_x += player_speed
        player = player_right

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
