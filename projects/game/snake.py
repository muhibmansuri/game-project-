import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Use hardware acceleration if available
flags = pygame.SCALED | pygame.RESIZABLE

# Dimensions
WIDTH = 800
HEIGHT = 600
dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Neon Snake | Advanced Python')

clock = pygame.time.Clock()

# --- Aesthetic Colors (Modern Dark Mode) ---
BG_COLOR = (15, 23, 42)      # Dark Slate Blue
GRID_COLOR = (30, 41, 59)    # Slightly lighter slate
SNAKE_HEAD = (56, 189, 248)  # Sky Blue
SNAKE_BODY = (14, 165, 233)  # Darker Blue
FOOD_COLOR = (244, 114, 182) # Pink/Magenta
TEXT_COLOR = (248, 250, 252) # White-ish
OVERLAY_BG = (15, 23, 42, 200) # Semi-transparent dictating darkness using alpha if surface used

# Snake Properies
SNAKE_BLOCK = 20
SNAKE_SPEED = 10

# Fonts
# Try to find a modern font, fallback to sans-serif
try:
    font_path = pygame.font.match_font('segoeui') # Windows standard modern font
    if not font_path: font_path = pygame.font.match_font('arial')
    font_main = pygame.font.Font(font_path, 35)
    font_score = pygame.font.Font(font_path, 25)
    font_title = pygame.font.Font(font_path, 50)
except:
    font_main = pygame.font.SysFont("bahnschrift", 35)
    font_score = pygame.font.SysFont("comicsansms", 25)
    font_title = pygame.font.SysFont("bahnschrift", 50)

def draw_grid():
    """Draws a subtle grid for a retro-modern look."""
    for x in range(0, WIDTH, SNAKE_BLOCK):
        pygame.draw.line(dis, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, SNAKE_BLOCK):
        pygame.draw.line(dis, GRID_COLOR, (0, y), (WIDTH, y))

def draw_snake(snake_list):
    """Draws the snake with rounded segments and eyes."""
    for i, x in enumerate(snake_list):
        # Determine if head or body
        color = SNAKE_HEAD if i == len(snake_list) - 1 else SNAKE_BODY
        
        # Rect parameters
        rect = [x[0], x[1], SNAKE_BLOCK, SNAKE_BLOCK]
        
        # Draw rounded rect (modern look)
        pygame.draw.rect(dis, color, rect, border_radius=5)
        
        # Draw Eyes if Head
        if i == len(snake_list) - 1:
            # Simple logic to determine direction could be added here for dynamic eyes
            # For now, generic eyes
            eye_radius = 3
            eye_offset = 5
            
            # Left Eye
            pygame.draw.circle(dis, (255, 255, 255), (int(x[0] + eye_offset), int(x[1] + eye_offset)), eye_radius)
            # Right Eye
            pygame.draw.circle(dis, (255, 255, 255), (int(x[0] + SNAKE_BLOCK - eye_offset), int(x[1] + eye_offset)), eye_radius)

def draw_food(x, y):
    """Draws the food as a glowing circle."""
    center = (int(x + SNAKE_BLOCK/2), int(y + SNAKE_BLOCK/2))
    radius = int(SNAKE_BLOCK/2) - 2
    
    # Glow effect (faint outer circle)
    pygame.draw.circle(dis, (FOOD_COLOR[0], FOOD_COLOR[1], FOOD_COLOR[2], 100), center, radius + 2)
    # Core
    pygame.draw.circle(dis, FOOD_COLOR, center, radius)

def show_score(score):
    value = font_score.render(f"Score: {score}", True, TEXT_COLOR)
    # Draw a small pill background for score
    bg_rect = value.get_rect(topleft=(10, 10))
    bg_rect.inflate_ip(20, 10)
    pygame.draw.rect(dis, (30, 41, 59), bg_rect, border_radius=10)
    dis.blit(value, (20, 15))

def game_over_screen(score):
    """Beautiful Game Over Overlay"""
    # Create a semi-transparent surface
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(200)
    overlay.fill((0, 0, 0))
    dis.blit(overlay, (0,0))
    
    # Text
    title = font_title.render("GAME OVER", True, (255, 99, 71))
    score_text = font_main.render(f"Final Score: {score}", True, TEXT_COLOR)
    restart_text = font_score.render("Press C to Play Again or Q to Quit", True, (148, 163, 184))
    
    # Center everything
    dis.blit(title, title.get_rect(center=(WIDTH/2, HEIGHT/2 - 50)))
    dis.blit(score_text, score_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 10)))
    dis.blit(restart_text, restart_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 60)))
    
    pygame.display.update()

def gameLoop():
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
    foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK

    while not game_over:
        
        while game_close:
            game_over_screen(Length_of_snake - 1)
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        
        # --- Drawing Phase ---
        dis.fill(BG_COLOR)
        draw_grid()
        draw_food(foodx, foody)
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(snake_List)
        show_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
            foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
            Length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

if __name__ == "__main__":
    gameLoop()
