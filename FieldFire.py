import pygame, random, time

# Size of each cell
size = 8
# Maximum frame rate
fps = 30
# Burn probability
burnChance = 0.00001
# Grow probability
growChance = 0.01

# Height and width of display
xCells = int(1440 / size)
yCells = int(720 / size)
grid = [[0 for x in range(yCells)] for y in range(xCells)]
last = [[0 for x in range(yCells)] for y in range(xCells)]



# Function for calculating next step in automation
def automate():
    for x in range(xCells):
        for y in range(yCells):
            # If current cell is just ground determine if something should grow
            if grid[x][y] == 0:
                grid[x][y] = 1000 if random.uniform(0, 1) < growChance else grid[x][y]    

            # If previous automation step was burning, determine spread of fire
            elif last[x][y] == 2000:
                # Check vicinity of cell on fire
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if x + i >= 0 and x + i < xCells and y + j >= 0 and y + j < yCells and last[x + i][y + j] <= 1000 and last[x + i][y + j] > 0:
                            # Update surrounding cells to be on fire
                            if random.choice([True, False]):
                                grid[x + i][y + j] = 2000
                            
                # Set last cell to be slightly burned out
                grid[x][y] -= 250

            # Otherwise determine if plant is ignited (lightning strike perhaps?)
            elif grid[x][y] > 0:
                grid[x][y] = 2000 if random.uniform(0, 1) < burnChance else grid[x][y]
               


# Function for drawing the current frame
def draw(display, clock):
    for x in range(xCells):
        for y in range(yCells):
            # Update last step in automation
            last[x][y] = grid[x][y]

            # Determine if cell is on fire
            if grid[x][y] > 1000:
                # Draw cell accordingly (should be red)
                pygame.draw.rect(display, (grid[x][y] // 10, 0, 0), (x * size, y * size, size, size), 0)
                # Decay fire appropriately or reset ground
                grid[x][y] -= 250
                if grid[x][y] <= 1000:
                    grid[x][y] = 0

            # Otherwise determine if cell is a plant
            elif grid[x][y] > 0:
                # Draw cell accordingly (should be green)
                pygame.draw.rect(display, (0, (grid[x][y] // 10) + 100, 0), (x * size, y * size, size, size), 0)
                # Age plant appropriately
                grid[x][y] -= 2

    # Update display and increment clock using framerate
    pygame.display.update()
    clock.tick(fps)



# Function to run the cellular automation
def run():
    # Initialize related pygame functions and set starting values
    pygame.init()
    display = pygame.display.set_mode((xCells * size, yCells * size))
    clock = pygame.time.Clock()
    start = time.time()
    generation = 1

    # Game loop
    while True:
        # Update title bar with helpful information
        pygame.display.set_caption(f"Field Fire: Generation: {generation:<10d}   Time: {time.time() - start:<10.3f}   FPS: {clock.get_fps():<4.4f}")

        # Check if "X" is clicked on game window
        if pygame.event.poll().type == pygame.QUIT:
            pygame.quit()
            break

        # Update game loop
        display.fill((92, 127, 0))
        automate()
        draw(display, clock)
        generation += 1



# Start cellular automata
if __name__ == "__main__":
    run()


