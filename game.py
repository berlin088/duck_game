import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Duck Shooting Game")

# Load background
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Load duck image
duck_img = pygame.image.load("duck.png")
duck_img = pygame.transform.scale(duck_img, (60, 40))

# Load sound
shoot_sound = pygame.mixer.Sound("shoot.wav")

# Fonts
font = pygame.font.SysFont("Arial", 36)

# Duck position
duck_x = random.randint(0, WIDTH - 60)
duck_y = random.randint(50, HEIGHT - 100)
duck_speed = 5

# Score and timer
score = 0
timer = 30  # seconds
start_ticks = pygame.time.get_ticks()

# Game loop
clock = pygame.time.Clock()
running = True

# Hide system cursor
pygame.mouse.set_visible(False)

# Crosshair
crosshair = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(crosshair, (255, 0, 0), (10, 10), 10, 2)

while running:
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    time_left = max(0, timer - int(seconds))
    if time_left == 0:
        running = False

    screen.blit(background, (0, 0))

    # Move duck
    duck_x += duck_speed
    if duck_x > WIDTH or duck_x < 0:
        duck_speed *= -1
        duck_y = random.randint(50, HEIGHT - 100)

    screen.blit(duck_img, (duck_x, duck_y))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot_sound.play()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if duck_x < mouse_x < duck_x + 60 and duck_y < mouse_y < duck_y + 40:
                score += 1
                duck_x = random.randint(0, WIDTH - 60)
                duck_y = random.randint(50, HEIGHT - 100)

    # Draw score and timer
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    timer_text = font.render(f"Time: {time_left}s", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(timer_text, (WIDTH - 180, 10))

    # Draw crosshair
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(crosshair, (mouse_pos[0] - 10, mouse_pos[1] - 10))

    pygame.display.update()
    clock.tick(60)

# Game over screen
screen.fill((0, 0, 0))
end_text = font.render(f"Game Over! Final Score: {score}", True, (255, 255, 255))
screen.blit(end_text, (WIDTH//2 - 200, HEIGHT//2 - 20))
pygame.display.update()
pygame.time.wait(3000)

pygame.quit()
sys.exit()
