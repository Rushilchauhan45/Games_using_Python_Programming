# For Question , Any Inquiry and Suggestion about the Program Contact me (chauhanrushil45@gmail.com)

#The Snack game 

import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen Settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The Snake Game")

# Colors
BACKGROUND_COLOR = (240, 248, 255)  # Light Blue
SNAKE_COLOR = (0, 128, 0)  # Green
FOOD_COLOR = (255, 69, 0)  # Red Orange
TEXT_COLOR = (50, 50, 50)  # Dark Gray
MENU_BG = (200, 230, 201)

# Fonts
FONT_TITLE = pygame.font.SysFont('Arial', 48, bold=True)
FONT_MENU = pygame.font.SysFont('Arial', 32)
FONT_TEXT = pygame.font.SysFont('Arial', 24)

# Clock
clock = pygame.time.Clock()
FPS = 15

# Display Text
def display_text(text, font, color, x, y, center=False):
    surface = font.render(text, True, color)
    rect = surface.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(surface, rect)

# Main Menu
def main_menu():
    while True:
        screen.fill(MENU_BG)
        display_text("The Snake Game", FONT_TITLE, TEXT_COLOR, SCREEN_WIDTH // 2, 100, center=True)
        display_text("1. Start Game", FONT_MENU, TEXT_COLOR, SCREEN_WIDTH // 2, 250, center=True)
        display_text("2. Change Snake Design", FONT_MENU, TEXT_COLOR, SCREEN_WIDTH // 2, 320, center=True)
        display_text("3. How to Play", FONT_MENU, TEXT_COLOR, SCREEN_WIDTH // 2, 390, center=True)
        display_text("4. Exit", FONT_MENU, TEXT_COLOR, SCREEN_WIDTH // 2, 460, center=True)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    start_game()
                if event.key == pygame.K_2:
                    change_snake_design()
                if event.key == pygame.K_3:
                    how_to_play()
                if event.key == pygame.K_4:
                    pygame.quit()
                    sys.exit()

# How to Play
def how_to_play():
    while True:
        screen.fill(BACKGROUND_COLOR)
        display_text("How to Play", FONT_TITLE, TEXT_COLOR, SCREEN_WIDTH // 2, 80, center=True)
        display_text("- Use Arrow Keys to move the snake.", FONT_TEXT, TEXT_COLOR, 50, 200)
        display_text("- Eat the red squares to grow.", FONT_TEXT, TEXT_COLOR, 50, 250)
        display_text("- Avoid colliding with the walls or yourself.", FONT_TEXT, TEXT_COLOR, 50, 300)
        display_text("- Press 'B' to return to the main menu.", FONT_TEXT, TEXT_COLOR, 50, 400)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                main_menu()

# Change Snake Design
def change_snake_design():
    global SNAKE_COLOR
    while True:
        screen.fill(BACKGROUND_COLOR)
        display_text("Change Snake Design", FONT_TITLE, TEXT_COLOR, SCREEN_WIDTH // 2, 80, center=True)
        display_text("1. Green Snake", FONT_MENU, TEXT_COLOR, SCREEN_WIDTH // 2, 200, center=True)
        display_text("2. Blue Snake", FONT_MENU, TEXT_COLOR, SCREEN_WIDTH // 2, 270, center=True)
        display_text("3. Yellow Snake", FONT_MENU, TEXT_COLOR, SCREEN_WIDTH // 2, 340, center=True)
        display_text("Press 'B' to return to Main Menu", FONT_TEXT, TEXT_COLOR, SCREEN_WIDTH // 2, 450, center=True)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    SNAKE_COLOR = (0, 128, 0)
                if event.key == pygame.K_2:
                    SNAKE_COLOR = (0, 0, 255)
                if event.key == pygame.K_3:
                    SNAKE_COLOR = (255, 255, 0)
                if event.key == pygame.K_b:
                    main_menu()

# Start Game
def start_game():
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    food_pos = [random.randrange(1, (SCREEN_WIDTH//10)) * 10, random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
    food_spawn = True
    direction = 'RIGHT'
    change_to = direction
    speed = 15

    while True:
        screen.fill(BACKGROUND_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            direction = 'LEFT'
        if keys[pygame.K_RIGHT]:
            direction = 'RIGHT'
        if keys[pygame.K_UP]:
            direction = 'UP'
        if keys[pygame.K_DOWN]:
            direction = 'DOWN'

        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, (SCREEN_WIDTH//10)) * 10, random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
            food_spawn = True

        for pos in snake_body:
            pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(screen, FOOD_COLOR, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        pygame.display.flip()
        clock.tick(speed)

# Start the Game
main_menu()
