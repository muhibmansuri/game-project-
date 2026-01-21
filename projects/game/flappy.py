import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GRAVITY = 0.25
FLAP_STRENGTH = -6.5
PIPE_SPEED = 3
PIPE_GAP = 150
PIPE_FREQUENCY = 1500  # milliseconds

# Colors
WHITE = (255, 255, 255)
SKY_BLUE = (135, 206, 235)
YELLOW = (255, 255, 0)
GREEN = (34, 139, 34)
BROWN = (139, 69, 19)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird Clone')
clock = pygame.time.Clock()

class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.radius = 15

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self):
        # Draw bird body
        pygame.draw.circle(screen, YELLOW, (int(self.x), int(self.y)), self.radius)
        # Eye
        pygame.draw.circle(screen, WHITE, (int(self.x + 8), int(self.y - 5)), 4)
        pygame.draw.circle(screen, (0, 0, 0), (int(self.x + 9), int(self.y - 5)), 2)
        # Beak
        pygame.draw.polygon(screen, (255, 165, 0), [(self.x + 12, self.y), (self.x + 22, self.y + 5), (self.x + 12, self.y + 10)])

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.top_height = random.randint(100, SCREEN_HEIGHT - PIPE_GAP - 100)
        self.bottom_y = self.top_height + PIPE_GAP
        self.width = 60
        self.passed = False

    def update(self):
        self.x -= PIPE_SPEED

    def draw(self):
        # Top pipe
        pygame.draw.rect(screen, GREEN, (self.x, 0, self.width, self.top_height))
        # Top pipe cap
        pygame.draw.rect(screen, (0, 100, 0), (self.x - 5, self.top_height - 20, self.width + 10, 20))
        
        # Bottom pipe
        pygame.draw.rect(screen, GREEN, (self.x, self.bottom_y, self.width, SCREEN_HEIGHT - self.bottom_y))
        # Bottom pipe cap
        pygame.draw.rect(screen, (0, 100, 0), (self.x - 5, self.bottom_y, self.width + 10, 20))

    def off_screen(self):
        return self.x < -self.width

    def collides_with(self, bird_rect):
        top_rect = pygame.Rect(self.x, 0, self.width, self.top_height)
        bottom_rect = pygame.Rect(self.x, self.bottom_y, self.width, SCREEN_HEIGHT - self.bottom_y)
        return bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect)

def draw_text(text, size, x, y):
    font = pygame.font.SysFont('Arial', size, bold=True)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def main():
    bird = Bird()
    pipes = []
    last_pipe_time = pygame.time.get_ticks()
    score = 0
    game_active = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_active:
                        bird.flap()
                    else:
                        # Reset game
                        bird = Bird()
                        pipes = []
                        score = 0
                        game_active = True

        screen.fill(SKY_BLUE)

        if game_active:
            # Bird logic
            bird.update()
            bird.draw()

            # Pipe logic
            current_time = pygame.time.get_ticks()
            if current_time - last_pipe_time > PIPE_FREQUENCY:
                pipes.append(Pipe())
                last_pipe_time = current_time

            for pipe in pipes[:]:
                pipe.update()
                pipe.draw()
                
                # Check collision
                if pipe.collides_with(bird.get_rect()):
                    game_active = False

                # Check if passed
                if not pipe.passed and pipe.x + pipe.width < bird.x:
                    pipe.passed = True
                    score += 1

                if pipe.off_screen():
                    pipes.remove(pipe)

            # Ground/Ceiling collision
            if bird.y - bird.radius <= 0 or bird.y + bird.radius >= SCREEN_HEIGHT:
                game_active = False

            # Display Score
            draw_text(str(score), 40, SCREEN_WIDTH // 2, 50)
        else:
            # Game Over Screen
            draw_text("GAME OVER", 50, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
            draw_text(f"Final Score: {score}", 30, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10)
            draw_text("Press SPACE to Restart", 20, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
