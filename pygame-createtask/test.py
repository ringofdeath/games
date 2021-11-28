
import pygame
import sys
pygame.init()
fps=30
fpsclock=pygame.time.Clock()
bg=pygame.display.set_mode((640,480))
pygame.display.set_caption("Keyboard_Input")
White=(255,255,255)
#var
p1=10
p2=10
step=5


#imgs 

#crystal imgs from qubodup opengameart.org
cry_img_blue=pygame.image.load("Imgs\crystal-qubodup-ccby3-32-blue.png")
player_img= pygame.image.load("imgs/Frame-1.png")

#functions

def resize_image(image,sizex,sizey,posx,posy):
    image=pygame.transform.smoothscale(image, (sizex,sizey))
    bg.blit(image,(posx,posy))


while True:
    bg.fill(White)
    resize_image(player_img,100,100,p1,p2)
    
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_LEFT]:
        p1 -= step
    if key_input[pygame.K_UP]:
        p2 -= step
    if key_input[pygame.K_RIGHT]:
        p1 += step
    if key_input[pygame.K_DOWN]:
        p2 += step
    pygame.display.update()
    fpsclock.tick(fps)