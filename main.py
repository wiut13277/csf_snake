#source https://www.edureka.co/blog/snake-game-with-pygame/
#Task:
# Demonstrate your knowledge of Python by modifying a small simple game, “Hungry Snake”, where you need to demonstrate your knowledge of
# python syntax, use of 3 different data types, conditionals, loop, functions. Well commented and organised code will receive higher marks.
# Procedural or object-oriented approach to programming is appreciated. Modifications can include input from the  user, adding different levels
# with increasing difficulty, more snakes on screen, snakes with changing colours. Use your creativity!
#
# The code examples should be pushed to a private git repository.

import pygame
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400


dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game 00013277; 00013075 ')

# menu
start_img = pygame.image.load("Assets/start_btn.png").convert_alpha()
exit_img = pygame.image.load("Assets/exit_btn.png").convert_alpha()


# button class

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mousehover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        dis.blit(self.image, (self.rect.x, self.rect.y))
        return  action

#create button instance
start_button = Button(100, 200, start_img, 0.5)
exit_button = Button(350, 200, exit_img, 0.5)