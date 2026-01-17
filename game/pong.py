import pygame
import sys

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SIZE = 15
PADDLE_SPEED = 7
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NEON_BLUE = (0, 255, 255)
NEON_PINK = (255, 20, 147)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ping Pong Pro')
clock = pygame.time.Clock()

class Paddle:
    def __init__(self, x, color):
        self.rect = pygame.Rect(x, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.color = color
        self.score = 0

    def move(self, up, down):
        keys = pygame.key.get_pressed()
        if keys[up] and self.rect.top > 0:
            self.rect.y -= PADDLE_SPEED
        if keys[down] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += PADDLE_SPEED

    def ai_move(self, ball):
        # Simple AI tracking the ball
        if self.rect.centery < ball.centery and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += PADDLE_SPEED - 2
        if self.rect.centery > ball.centery and self.rect.top > 0:
            self.rect.y -= PADDLE_SPEED - 2

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=5)

class Ball:
    def __init__(self):
        self.reset()

    def reset(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED_X * (-1 if pygame.time.get_ticks() % 2 == 0 else 1)
        self.speed_y = BALL_SPEED_Y * (-1 if pygame.time.get_ticks() % 2 == 0 else 1)

    def update(self, player_p, opponent_p):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Ceiling and Floor collision
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1

        # Paddle collision
        if self.rect.colliderect(player_p.rect) or self.rect.colliderect(opponent_p.rect):
            self.speed_x *= -1.1  # Increase speed slightly
            self.speed_y *= 1.05

        # Score update
        if self.rect.left <= 0:
            opponent_p.score += 1
            self.reset()
        if self.rect.right >= SCREEN_WIDTH:
            player_p.score += 1
            self.reset()

    def draw(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)

def draw_text(text, size, x, y, color=WHITE):
    font = pygame.font.SysFont('Arial', size, bold=True)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def main():
    player = Paddle(20, NEON_BLUE)
    opponent = Paddle(SCREEN_WIDTH - 20 - PADDLE_WIDTH, NEON_PINK)
    ball = Ball()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Input / Logic
        player.move(pygame.K_w, pygame.K_s)
        opponent.ai_move(ball.rect)
        ball.update(player, opponent)

        # Draw
        screen.fill((20, 20, 30))  # Dark background
        
        # Center Line
        pygame.draw.aaline(screen, (50, 50, 50), (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))
        
        player.draw()
        opponent.draw()
        ball.draw()

        # Show Scores
        draw_text(str(player.score), 40, SCREEN_WIDTH // 4, 50, NEON_BLUE)
        draw_text(str(opponent.score), 40, 3 * SCREEN_WIDTH // 4, 50, NEON_PINK)
        
        draw_text("W / S to Move", 15, 60, SCREEN_HEIGHT - 20, (100, 100, 100))

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
