#python game for create task

import pygame
from pygame.locals import *

def start_screen():
    pygame.init()
    screen_width = 1000
    screen_height = 800
    screen= pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Platformer")
    
    #load images
    #bg.jpg from Wikimedia Commmons Ludlow at Night - Flickr- Michelle Jones UK.jpg
    bg_img = pygame.image.load("imgs/bg.jpg")
    #player_img from bevouliin.com Flying bird game character 
    player_img= pygame.image.load("imgs/Frame-1.png")
    
    
    run = True
    while run:



        screen.blit(bg_img,(0,0))
        screen.blit(player_img,(0,0))


        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                run= False
    pygame.display.update()
    pygame.quit()   
start_screen()