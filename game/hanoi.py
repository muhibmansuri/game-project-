import pygame
import time

# Initialize Pygame
pygame.init()

# Screen Dimensions
WIDTH = 800
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower of Hanoi - Recursion Visualizer")

# Colors
BG_COLOR = (15, 23, 42)
PEGS_COLOR = (148, 163, 184)
DISK_COLORS = [
    (239, 68, 68),   # Red
    (249, 115, 22),  # Orange
    (234, 179, 8),   # Yellow
    (34, 197, 94),   # Green
    (59, 130, 246),  # Blue
    (168, 85, 247),  # Purple
    (236, 72, 153)   # Pink
]
TEXT_COLOR = (241, 245, 249)

# Game Constants
N_DISKS = 4
DISK_HEIGHT = 25
DISK_WIDTH_FACTOR = 20
PEG_WIDTH = 10
PEG_HEIGHT = 200
BASE_Y = 400
PEGS_X = [200, 400, 600]

# Metrics
moves_count = 0
font = pygame.font.SysFont("bahnschrift", 25)

def draw_game(towers, selected_disk=None, selected_pos=None):
    screen.fill(BG_COLOR)
    
    # Draw Pegs
    for x in PEGS_X:
        pygame.draw.rect(screen, PEGS_COLOR, (x - PEG_WIDTH//2, BASE_Y - PEG_HEIGHT, PEG_WIDTH, PEG_HEIGHT))
        pygame.draw.rect(screen, PEGS_COLOR, (x - 100, BASE_Y, 200, 10)) # Base

    # Draw Disks
    for i, tower in enumerate(towers):
        x = PEGS_X[i]
        for j, disk_val in enumerate(tower):
            width = disk_val * DISK_WIDTH_FACTOR + 40
            height = DISK_HEIGHT
            
            # If this disk is selected/floating
            if selected_disk == disk_val:
                rect_x, rect_y = selected_pos
            else:
                rect_x = x - width // 2
                rect_y = BASE_Y - (j + 1) * height
            
            color = DISK_COLORS[disk_val % len(DISK_COLORS)]
            pygame.draw.rect(screen, color, (rect_x, rect_y, width, height), border_radius=5)
            pygame.draw.rect(screen, (255,255,255), (rect_x, rect_y, width, height), 1, border_radius=5)

    # UI Text
    text_moves = font.render(f"Moves: {moves_count}", True, TEXT_COLOR)
    text_info = font.render("Press 'SPACE' to Solve (Recursion) | Click to Move", True, (148, 163, 184))
    screen.blit(text_moves, (20, 20))
    screen.blit(text_info, (WIDTH//2 - text_info.get_width()//2, 20))
    
    pygame.display.flip()

def get_tower_clicked(mouse_pos):
    """Returns index of tower clicked (0, 1, 2) or None."""
    mx, my = mouse_pos
    # Simple hitboxes around pegs
    for i, x in enumerate(PEGS_X):
        if abs(x - mx) < 80:
            return i
    return None

def move_disk(towers, source, target):
    """Logic to move disk from source to target tower."""
    if not towers[source]: return False
    disk = towers[source][-1]
    
    # Check if move is valid (smaller on larger)
    if towers[target] and towers[target][-1] < disk:
        return False
    
    towers[source].pop()
    towers[target].append(disk)
    return True

# --- RECURSIVE SOLVER ---
def recursive_solver(n, source, auxiliary, target, towers):
    """
    Solves Tower of Hanoi and visualizes it.
    This is a generator to allow the main loop to handle events/rendering.
    """
    if n == 1:
        yield (source, target)
        return
    
    yield from recursive_solver(n - 1, source, target, auxiliary, towers)
    yield (source, target)
    yield from recursive_solver(n - 1, auxiliary, source, target, towers)

def main():
    global moves_count, N_DISKS
    clock = pygame.time.Clock()
    
    # Start: All disks on Tower 0 (Largest at bottom -> index 0)
    # Storing list as [disk_size_largest, ..., disk_size_smallest] ? 
    # Actually, visual stack: index 0 is bottom.
    # disk values: N down to 1.
    towers = [[i for i in range(N_DISKS, 0, -1)], [], []] 
    
    selected_tower_idx = None
    solving = False
    solver_generator = None
    last_move_time = 0
    MOVE_DELAY = 500 # ms

    run = True
    while run:
        mouse_pos = pygame.mouse.get_pos()
        
        # Handle solving steps
        if solving:
            current_time = pygame.time.get_ticks()
            if current_time - last_move_time > MOVE_DELAY:
                try:
                    src, trg = next(solver_generator)
                    move_disk(towers, src, trg)
                    moves_count += 1
                    last_move_time = current_time
                except StopIteration:
                    solving = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            # User Interaction (Only if not auto-solving)
            if not solving:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_tower = get_tower_clicked(mouse_pos)
                    
                    if clicked_tower is not None:
                        if selected_tower_idx is None:
                            # Select
                            if towers[clicked_tower]:
                                selected_tower_idx = clicked_tower
                        else:
                            # Move
                            if selected_tower_idx == clicked_tower:
                                selected_tower_idx = None # Deselect
                            else:
                                if move_disk(towers, selected_tower_idx, clicked_tower):
                                    moves_count += 1
                                selected_tower_idx = None
                                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # Reset and Start Solver
                        towers = [[i for i in range(N_DISKS, 0, -1)], [], []]
                        moves_count = 0
                        solving = True
                        solver_generator = recursive_solver(N_DISKS, 0, 1, 2, towers)
                    
                    # --- CHANGE LOGIC: Dynamic Settings ---
                    elif event.key == pygame.K_UP:
                        if N_DISKS < 8:
                            N_DISKS += 1
                            towers = [[i for i in range(N_DISKS, 0, -1)], [], []]
                            moves_count = 0
                            solving = False
                    elif event.key == pygame.K_DOWN:
                        if N_DISKS > 3:
                            N_DISKS -= 1
                            towers = [[i for i in range(N_DISKS, 0, -1)], [], []]
                            moves_count = 0
                            solving = False
                    elif event.key == pygame.K_RIGHT:
                        MOVE_DELAY = max(50, MOVE_DELAY - 50) # Faster
                    elif event.key == pygame.K_LEFT:
                        MOVE_DELAY = min(1000, MOVE_DELAY + 50) # Slower

        # Logic for dragging visual
        sel_disk = None
        sel_pos = None
        if selected_tower_idx is not None and towers[selected_tower_idx]:
            sel_disk = towers[selected_tower_idx][-1]
            sel_pos = (mouse_pos[0] - (sel_disk*DISK_WIDTH_FACTOR+40)//2, mouse_pos[1] - DISK_HEIGHT//2)

        draw_game(towers, sel_disk, sel_pos)
        
        # Draw Settings Info
        settings_text = font.render(f"Disks: {N_DISKS} (↑/↓) | Speed: {1050-MOVE_DELAY} (←/→)", True, (100, 200, 100))
        screen.blit(settings_text, (WIDTH//2 - settings_text.get_width()//2, HEIGHT - 30))

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
