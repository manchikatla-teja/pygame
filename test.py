# coding: cp1252
import pygame
from sys import exit
from AllScenes import display_text
from pytmx.util_pygame import load_pygame
 
class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)


pygame.init()
screen = pygame.display.set_mode((1280, 720))
screen.fill('red')


 
# for obj in tmx_data.objects:
#     pos = obj.x,obj.y
#     if obj.type in ('Building', 'Vegetation'):
#         Tile(pos = pos, surf = obj.image, groups = sprite_group)

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
        if event.type == pygame.MOUSEBUTTONUP and event.button ==1: #1means left button of mouse
            current_dialogue+=3

#     tmx_data = load_pygame('yes.tmx')
#     sprite_group = pygame.sprite.Group()

 
# # cycle through all layers
#     for layer in tmx_data.visible_layers:
#     # if layer.name in ('Floor', 'Plants and rocks', 'Pipes')
#         if hasattr(layer,'data'):
#             for x,y,surf in layer.tiles():
#                 pos = (x * 64 + 300, y * 64)
#                 Tile(pos = pos, surf = surf, groups = sprite_group)


#     sprite_group.draw(screen)
    image = pygame.image.load("tiles/arjun.jpg").convert_alpha()
    image.set_colorkey('black')
    rect = image.get_rect()
    screen.blit(image, rect)
    screen.blit(text_box, (20, 480))
    
    displayScene()
    pygame.display.update()
    clock.tick(60)