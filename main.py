import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 500, 480
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Splunker")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Rectangle properties
rect_x = width // 2
rect_y = 0
rect_width = 40
rect_height = 40
speed = 5

# Main game loop
run = True
while run:

		# Process any events. Currently, only processing the "QUIT" event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Move the rectangle to the right
    rect_y += speed

    # Reset position if it goes off screen
    if rect_y > height:
        rect_y = 0  # Start from the top again

    # Fill the background
    win.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(win, BLUE, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.update()

    pygame.time.delay(30)  # Delay to control frame rate

# Quit Pygame
pygame.quit()
sys.exit()

