import pygame
import sys

# Initialize Pygame
pygame.init()

# Load the background image
background_image = pygame.image.load('splunker-background.png')

# Get the width and height of the background image
width, height = background_image.get_size()

# Setup the display at the same size of the background image
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
speed = 0

# Game environment properties

# Set the ground to the ground in the background
# image minus the height of the rectangle
ground = height - 100 - rect_height

# Main game loop
run = True
while run:

		# Process any events. Currently, only processing the "QUIT" event
    for event in pygame.event.get():
    	  # If the game is quit, stop after the next loop
        if event.type == pygame.QUIT:
            run = False
        # Process key presses
        elif event.type == pygame.KEYDOWN:
            # Decrease speed if up arrow is pressed
            if event.key == pygame.K_UP:
                speed -= 3
            # Quit if escape key is pressed
            if event.key == pygame.K_ESCAPE:
                run = False

    # Adjust speed by gravity
    speed += 0.25
                    
    # If the rectangle is on the ground or about to go
    # past the ground, set position to ground. Set downward
    # speed to zero
    if rect_y + speed > ground:
        rect_y = ground
        speed = 0
    # Otherwise move the rectangle by the speed
    else:
        rect_y += speed

    # Fill the background
    win.blit(background_image, (0, 0))

    # Draw the rectangle
    pygame.draw.rect(win, BLUE, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.update()

	  # Delay to control frame rate
    pygame.time.delay(15)

# Quit Pygame
pygame.quit()
sys.exit()

