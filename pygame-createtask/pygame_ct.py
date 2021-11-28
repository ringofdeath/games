from os import X_OK, remove
import pygame
import sys
import random
import os
from pygame import sprite
import pygame.freetype
from pygame import surface
from pygame.draw import rect
from pygame.event import post
from pygame.locals import *

pygame.init()
window_width = 640
#1000
window_height = 480
#800
window= pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Platformer")
#load images
#bg.jpg from Wikimedia Commmons Ludlow at Night - Flickr- Michelle Jones UK.jpg
#bg_img = pygame.image.load("imgs/bg.jpg")
#player_img from bevouliin.com Flying bird game character
#player_img= pygame.image.load("")
player=pygame.transform.smoothscale(pygame.image.load('imgs/Frame-1.png'), (100, 100))
#crystal imgs from qubodup opengameart.org
cry_img_blue=pygame.transform.smoothscale(pygame.image.load('Imgs\crystal-qubodup-ccby3-32-blue.png'), (35, 50))
my_font=pygame.font.SysFont("smalle.fon",20)
my_font.render("test",(50,50),(200,255,100),(0,0,0))

#var's
#player score
player_score = 0
#Player starting pos
playerposx= 250
playerposy= 180
step= 15
fps=30
fpsclock=pygame.time.Clock()
#crystal var CRYSTAL=CRY
cryposx=0
cryposy=0
#Set var so I don't have to look for size of cystal everytime I resize new crystals
crysizex=35
crysizey=50
white=(255,255,255)
sprite_group=pygame.sprite.Group


#functions
def resize_image(image,sizex,sizey,posx,posy):
    image=pygame.transform.smoothscale(image, (sizex,sizey))
    window.blit(image,(posx,posy))
def cry_random_pos():
    
    global cryx
    cryx=random.randrange(10,630,15)
    global cryy
    cryy=random.randrange(10,470,15)



while True:    
    #image filling on game window
    window.fill(white)
    window.blit(player,(playerposx,playerposy))
    window.blit(cry_img_blue,(cryposx,cryposy))
    #resize_image(player_img,100,100,playerposx,playerposy)
    #resize_image(cry_img_blue,crysizex,crysizey,cryposx,cryposx)
    for event in pygame.event.get():
        #game quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #rect tracking of sprites
    cry_rect= pygame.Rect(cryposx,cryposy,35,50)
    playerbox = pygame.Rect(playerposx,playerposy,100,90)
    pygame.draw.rect(window,(50,20,150),cry_rect,-1,-1)
    pygame.draw.rect(window,(0,255,0),playerbox,2,1)
    cry_touched = pygame.Rect.colliderect(playerbox,cry_rect)  

    


    #collsion with player and crystal
    if cry_touched:
        cry_random_pos()
        resize_image(cry_img_blue,crysizex,crysizey,cryx,cryy)


    #player movement
    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_LEFT]:
        playerposx -= step
    if key_input[pygame.K_UP]:
        playerposy -= step
    if key_input[pygame.K_RIGHT]:
        playerposx += step
    if key_input[pygame.K_DOWN]:
        playerposy += step
    
    
    
    pygame.display.update()
    fpsclock.tick(fps)