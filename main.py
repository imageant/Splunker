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

# Game environment properties
ground = height - rect_height

# Main game loop
run = True
while run:

		# Process any events. Currently, only processing the "QUIT" event
    for event in pygame.event.get():
    	  # If the game is quit, stop after the next loop
        if event.type == pygame.QUIT:
            run = False
        # If any key is pressed, reset the rectangle's position
        elif event.type == pygame.KEYDOWN:
            # Reset position if it goes off screen
            rect_y = 0

    # Do nothing to the rectangle if we're already on the ground
    # Otherwise move the rectangle down
    if rect_y == ground:
        [] # Do nothing
    else:
        # Move the rectangle down
        rect_y += speed

    # Fill the background
    win.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(win, BLUE, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.update()

	  # Delay to control frame rate
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
sys.exit()

