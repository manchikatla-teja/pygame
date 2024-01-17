# coding: cp1252
import pygame
from sys import exit
from AllScenes import display_text

def displayScene():
    arrayOfTexts = display_text("scene16", current_dialogue)
    text_surf1 = test_font.render(arrayOfTexts[0], False, (100, 100, 100))
    text_rect1 = text_surf1.get_rect(topleft = (40, 515))
    text_surf2 = test_font.render(arrayOfTexts[1], False, (100, 100, 100))
    text_rect2 = text_surf2.get_rect(topleft = (40, 565))
    text_surf3 = test_font.render(arrayOfTexts[2], False, (100, 100, 100))
    text_rect3 = text_surf3.get_rect(topleft = (40, 615))
    screen.blit(text_surf1, text_rect1)
    screen.blit(text_surf2, text_rect2)
    screen.blit(text_surf3, text_rect3)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Runenr')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/PixelType.ttf', 56)

text_box = pygame.Surface((1240, 200))
text_box.fill('white')

current_dialogue = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            current_dialogue+=3

    


    screen.blit(text_box, (20, 480))
    displayScene()
    pygame.display.update()
    clock.tick(60)