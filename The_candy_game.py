# For Question , Any Inquiry and Suggestion about the Program Contact me (chauhanrushil45@gmail.com)

#The Candy Game 


import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen Settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The Candy Game")

# Colors
BACKGROUND_COLOR = (240, 248, 255)  # Light Blue
BASKET_COLOR = (139, 69, 19)  # Saddle Brown
CANDY_COLOR = (255, 105, 180)  # Hot Pink
TEXT_COLOR = (50, 50, 50)  # Dark Gray
PILLAR_COLOR = (100, 100, 100)

# Fonts
FONT_TITLE = pygame.font.SysFont('Arial', 48, bold=True)
FONT_MENU = pygame.font.SysFont('Arial', 32)
FONT_TEXT = pygame.font.SysFont('Arial', 24)

# Clock
clock = pygame.time.Clock()
FPS = 60

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
        screen.fill(BACKGROUND_COLOR)
        display_text("The Candy Game", FONT_TITLE, TEXT_COLOR, SCREEN_WIDTH // 2, 100, center=True)
        display_text("1. Start Game", FONT_MENU, TEXT_COLOR, SCREEN_WIDTH // 2, 250, center=True)
        display_text("2. How to Play", FONT_MENU, TEXT_COLOR, SCREEN_WIDTH // 2, 320, center=True)
        display_text("3. Exit", FONT_MENU, TEXT_COLOR, SCREEN_WIDTH // 2, 390, center=True)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    start_game()
                if event.key == pygame.K_2:
                    how_to_play()
                if event.key == pygame.K_3:
                    pygame.quit()
                    sys.exit()

# How to Play
def how_to_play():
    while True:
        screen.fill(BACKGROUND_COLOR)
        display_text("How to Play", FONT_TITLE, TEXT_COLOR, SCREEN_WIDTH // 2, 80, center=True)
        display_text("- Use Arrow Keys to move the basket.", FONT_TEXT, TEXT_COLOR, 50, 200)
        display_text("- Catch the candies to earn points.", FONT_TEXT, TEXT_COLOR, 50, 250)
        display_text("- Missing candies reduces your lives.", FONT_TEXT, TEXT_COLOR, 50, 300)
        display_text("- Press 'B' to return to the main menu.", FONT_TEXT, TEXT_COLOR, 50, 400)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                main_menu()

# Start Game
def start_game():
    basket_width = 120
    basket_height = 30
    basket_x = (SCREEN_WIDTH - basket_width) / 2
    basket_y = SCREEN_HEIGHT - basket_height - 50
    basket_speed = 10

    candy_width = 30
    candy_height = 30
    candy_x = random.randint(0, SCREEN_WIDTH - candy_width)
    candy_y = 0
    candy_speed = 5

    score = 0
    lives = 3

    while True:
        screen.fill(BACKGROUND_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 0:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT] and basket_x < SCREEN_WIDTH - basket_width:
            basket_x += basket_speed

        candy_y += candy_speed

        if (basket_x < candy_x < basket_x + basket_width) and (basket_y < candy_y < basket_y + basket_height):
            score += 1
            candy_x = random.randint(0, SCREEN_WIDTH - candy_width)
            candy_y = 0

        if candy_y > SCREEN_HEIGHT:
            lives -= 1
            candy_x = random.randint(0, SCREEN_WIDTH - candy_width)
            candy_y = 0

        if lives == 0:
            screen.fill(BACKGROUND_COLOR)
            display_text("Game Over", FONT_TITLE, TEXT_COLOR, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, center=True)
            display_text(f"Final Score: {score}", FONT_MENU, TEXT_COLOR, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50, center=True)
            pygame.display.flip()
            pygame.time.wait(3000)
            main_menu()

        pygame.draw.rect(screen, PILLAR_COLOR, (basket_x - 10, basket_y, 10, 50))
        pygame.draw.rect(screen, PILLAR_COLOR, (basket_x + basket_width, basket_y, 10, 50))
        pygame.draw.rect(screen, BASKET_COLOR, (basket_x, basket_y, basket_width, basket_height))
        pygame.draw.ellipse(screen, CANDY_COLOR, (candy_x, candy_y, candy_width, candy_height))

        display_text(f"Score: {score}", FONT_TEXT, TEXT_COLOR, 10, 10)
        display_text(f"Lives: {lives}", FONT_TEXT, TEXT_COLOR, SCREEN_WIDTH - 100, 10)

        pygame.display.flip()
        clock.tick(FPS)

# Start the Game
main_menu()
