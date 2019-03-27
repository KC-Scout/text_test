import pygame
import sys

screen = pygame.display.set_mode((1200, 800))
screen_rect = screen.get_rect()
# ~ screen.fill((0, 0, 0))

width = 250
height = 50

pygame.font.init()
button_color = (0, 200, 184)
text_color = (0, 0, 0)
font = pygame.font.SysFont(None, 50)

# Makes a rectange for the button, coordinates and size
button_rect = pygame.Rect(0, 0, width, height)  
button_rect.center = screen_rect.center

text = "Colors"
text = text.lower()
text_image = font.render(text, True, text_color, button_color)
text_image_rect = text_image.get_rect()
text_image_rect.center = button_rect.center

purple_button_rect = pygame.Rect(0, 0, 150, 150) 
purple_button_color = (128, 0, 128)

green_button_rect = pygame.Rect(400, 0, 150, 150)
green_button_color = (50, 205, 50)
green_button_rect.topright = screen_rect.topright

blue_button_rect = pygame.Rect(0, 0, 150, 150)
blue_button_color = (0, 0, 200)
blue_button_rect.bottomleft = screen_rect.bottomleft

yellow_button_rect = pygame.Rect(0, 0, 150, 150)
yellow_button_color = (255, 255, 0 )
yellow_button_rect.bottomright = screen_rect.bottomright

purple = "purple"
purple = purple.upper()
purple_image = font.render(purple, True, text_color, 
    purple_button_color)
purple_image_rect = purple_image.get_rect()
purple_image_rect.center = purple_button_rect.center

green = "green"
green = green.upper()
green_image = font.render(green, True, text_color, green_button_color)
green_image_rect = green_image.get_rect()
green_image_rect.center = green_button_rect.center


blue = "blue"
blue = blue.upper()
blue_image = font.render(blue, True, text_color, blue_button_color)
blue_image_rect = blue_image.get_rect()
blue_image_rect.center = blue_button_rect.center

yellow = "yellow"
yellow = yellow.upper()
yellow_image = font.render(yellow, True, text_color, yellow_button_color)
yellow_image_rect = yellow_image.get_rect()
yellow_image_rect.center = yellow_button_rect.center

while True:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
    
    # Puts the rectangle for the button on the screen         
    screen.fill(button_color, button_rect)
    screen.fill(purple_button_color, purple_button_rect)
    screen.fill(green_button_color, green_button_rect)
    screen.fill(blue_button_color, blue_button_rect)
    screen.fill(yellow_button_color, yellow_button_rect)
    
    # Draw the button on the button rectangle
    screen.blit(text_image, text_image_rect)
    screen.blit(purple_image, purple_image_rect)
    screen.blit(green_image, green_image_rect)
    screen.blit(blue_image, blue_image_rect)
    screen.blit(yellow_image, yellow_image_rect)
            
    pygame.display.flip()
