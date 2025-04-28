import pygame
import numpy as np

# Initialize Pygame window
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Sand Simulation")
running = True

# Set up grid
grid_width = width // 10
grid_height = height // 10
cell_size = 10
grid = np.zeros((grid_width, grid_height))  # 0 means no sand, 1 means sand

# Set screen background to black
screen.fill((0, 0, 0))

while running:
    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            running = False

    # Check if mouse is pressed
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # Left mouse button is pressed
        # Get mouse position
        x, y = pygame.mouse.get_pos()
        # Convert to grid coordinates
        grid_x = x // cell_size
        grid_y = y // cell_size
        # Mark grid position as '1'
        if 0 <= grid_x < grid_width and 0 <= grid_y < grid_height:
            grid[grid_x, grid_y] = 1  # Mark grid cell as sand

        # Draw particles in the grid and update their positions
    for grid_x in range(grid_width):
        for grid_y in range(grid_height - 1, -1, -1):  # Start from the bottom row to avoid overwriting particles
            if grid[grid_x, grid_y] == 1:  # If there's a sand particle
                # Check if the space below is empty
                if grid_y + 1 < grid_height and grid[grid_x, grid_y + 1] == 0:
                    # Move the particle down
                    grid[grid_x, grid_y] = 0  # Clear the current position
                    grid[grid_x, grid_y + 1] = 1  # Move to the new position

    # Draw the updated grid
    for grid_x in range(grid_width):
        for grid_y in range(grid_height):
            if grid[grid_x, grid_y] == 1:
                pygame.draw.rect(
                    screen,
                    (255, 204, 0),  # Sand particle color
                    (grid_x * cell_size, grid_y * cell_size, cell_size, cell_size)  # Draw sand particle
                )
            elif grid[grid_x, grid_y] == 0:
                pygame.draw.rect(
                    screen,
                    (0,0,0),
                    (grid_x * cell_size, grid_y * cell_size, cell_size, cell_size)
                )


    pygame.display.flip()
    clock.tick(60)

pygame.quit()