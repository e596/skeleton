import pygame

pygame.init()
screen = pygame.display.set_mode((1024, 512))
pygame.display.set_caption("Skeleton")
icon = pygame.image.load('images/3792031_halloween_horror_skeleton_skull_icon.png')
pygame.display.set_icon(icon)

player = pygame.image.load('images/skeleton_image1.png')
background = pygame.image.load('images/248880a15879483281825de6f0b4c0f4HEqGnLzIi2JXz9nc-0.png')

player_speed = 5
player_x = 0

running = True
while running:

    screen.blit(background, (0, 0))
    screen.blit(player, (player_x, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT]:
        player_x += player_speed

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
