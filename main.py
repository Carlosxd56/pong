# Import library
from email.mime import image
import pygame
import random as rd

#initialize pygame
pygame.init()

# colors
background_color = (0, 0, 0)
player_color = (255, 255, 255)
ball_color = (255, 128, 0)
line_color = (255, 255, 255)

# players size
players_width = 15
players_height =  90

# Player 1 coordinates
player_1_x = 50
player_1_y = 300 - (players_height/2)
player_1_y_speed = 0

# Player 2 coordinates
player_2_x = 735
player_2_y = 250
player_2_y_speed = 0

# Ball Coordinates
ball_x = 400
ball_y = 300
ball_radius = 20

ball_speed_x = 0.4
ball_speed_y = 0.4


# window size
screen_width = 800
screen_height = 600

# size variable
size = ( screen_width, screen_height )

#Display the window
screen = pygame.display.set_mode (size)

# icon
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Title
pygame.display.set_caption("pong game 1.0b")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # player key controls

        # Cheks for KEYDOWN event
        if event.type == pygame.KEYDOWN:

            # player 1
            if event.key == pygame.K_w:
                player_1_y_speed = -1

            if event.key == pygame.K_s:
                player_1_y_speed = 1

            # player 2
            if event.key == pygame.K_UP:
                player_2_y_speed = -1
            if event.key == pygame.K_DOWN:
                player_2_y_speed = 1

        if event.type == pygame.KEYUP:

            # Player 1
              if event.key == pygame.K_w:
                player_1_y_speed = 0

              if event.key == pygame.K_s:
                player_1_y_speed = 0

            # Player 2
              if event.key == pygame.K_UP:
               player_2_y_speed = 0
              if event.key == pygame.K_DOWN:
               player_2_y_speed = 0


    # player movement
    player_1_y += player_1_y_speed
    player_2_y += player_2_y_speed
    
    # Players Boundaries

    # Player 1 
    if player_1_y <= 0:
        player_1_y = 0

    if    player_1_y >= screen_height - players_height:
        player_1_y = screen_height - players_height

    # Player 2
    if player_2_y <= 0:
        player_2_y = 0

    if    player_2_y >= screen_height - players_height:
        player_2_y = screen_height - players_height
    
    # ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball Boundaries: top or buttom
    if ball_y > (screen_height - ball_radius) or ball_y < ball_radius:
        ball_speed_y *= -1
    

    # Ball Boundaries: (right or left) and score update
    if ball_x > screen_width:

        ball_x = screen_width/2
        ball_y = screen_height/2
        ball_speed_x *= rd.choice((-1, 1))

    if ball_x < 0:
        ball_x = screen_width/2
        ball_y = screen_height/2
        ball_speed_x *= rd.choice((-1, 1))
         
# fill screen with color
    screen.fill (background_color)

    # Drawing are
    
    # Define The player 1 - left: rectangle
    player_1 = pygame.draw.rect( screen, player_color, (player_1_x, player_1_y, players_width, players_height ))

    # Define The player 2 - left: rectangle
    player_2 = pygame.draw.rect( screen, player_color, (player_2_x, player_2_y, players_width, players_height ))
    
    # Draw the center line
    pygame.draw.aaline(screen, line_color, (screen_width/2,0),(screen_width/2, screen_height) )

     # Draw the ball
    Ball = pygame.draw.circle ( screen, ball_color, (ball_x, ball_y), ball_radius)

    # Colitions
    if Ball.colliderect(player_1) or Ball.colliderect(player_1):
        ball_speed_x *= -1

    if Ball.colliderect(player_2) or Ball.colliderect(player_2):
        ball_speed_x *= -1

    # refresh the windows
    pygame.display.flip()