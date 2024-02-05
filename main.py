import pygame
import sys
import random

from MainScreen import MainScreen
from GameScreen import GameScreen
# Initialize Pygame
pygame.init()

# Set up the game window
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake initialization
snake = [pygame.Rect(200, 200, 10, 10),
         pygame.Rect(190, 200, 10, 10),
         pygame.Rect(180, 200, 10, 10),
         pygame.Rect(170, 200, 10, 10)]  # Initial snake segment
snake_direction = (1, 0)  # Initial movement direction
x, y = random.randint(2, 78) * 10, random.randint(2, 58) * 10
# x, y = 200, 200
food = pygame.Rect(x, y, 10, 10)
clock = pygame.time.Clock()
run = True
menu_screen = MainScreen()
game_screen = GameScreen()
current_screen = "menu"
# Game loop
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and snake_direction != (0, 1):
            snake_direction = (0, -1)
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and snake_direction != (0, -1):
            snake_direction = (0, 1)
        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and snake_direction != (1, 0):
            snake_direction = (-1, 0)
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and snake_direction != (-1, 0):
            snake_direction = (1, 0)

        # Move the snake
    new_head = snake[0].move(snake_direction[0] * 10, snake_direction[1] * 10)
    snake.insert(0, new_head)
    snake.pop()
    # Draw game elements here
    screen.fill((0, 0, 0))  # Clear the screen

    # Draw the snake
    positions = {}
    for segment in snake:
        temp = (segment[0], segment[1])
        if positions.get(temp):
            run = False
        positions[temp] = 1
        # print(temp)
    for segment in snake:
        if segment[0] >= SCREEN_WIDTH or segment[0] <= 0 or segment[1] >= SCREEN_HEIGHT or segment[1] <= 0:
            run = False
            print("Game Over!")
        if segment[0] == food[0] and segment[1] == food[1]:
            x, y = random.randint(2, 78) * 10, random.randint(2, 58) * 10
            food = pygame.Rect(x, y, 10, 10)
            new_head = snake[0].move(snake_direction[0] * 10, snake_direction[1] * 10)
            snake.insert(0, new_head)
        pygame.draw.rect(screen, (0, 255, 0), segment)
    pygame.draw.rect(screen, (255, 0, 0), food)
    # Update the display
    pygame.display.update()

# Control the frame rate
    clock.tick(10)  # Adjust the frame rate (e.g., 10 frames per second)

# Quit Pygame properly
pygame.quit()
sys.exit()
