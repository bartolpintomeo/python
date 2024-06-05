import pygame
import time
pygame.init()

def oscilla(variabile):
    while variabile <-11:
        variabile+=0.7
    while variabile >11:
        variabile+=0.7
area=pygame.display.set_mode((400,400))
area.fill((255,255,255))
fnt = pygame.font.SysFont("Times New Roman", 24)
posy=200
scritta=fnt.render( str(posy), True, "yellow")
posx=60
x=10
pygame.draw.line(area,(0,0,0),(50,250),(350,250))
pygame.draw.line(area,(0,0,0),(200,250),(200,200))
while True:    
    for z in range(1,30):
        pygame.draw.circle(area, (0,255,0),(posx, posy), 10)
        pygame.display.update()
        time.sleep(0.02)
        pygame.draw.circle(area, (255,255,255),(posx, posy), 10)
        posx+=10
        posy-=x
        x-=0.7
        print(posy)
    x=x*-1
    for z in range(1,30):
        pygame.draw.circle(area, (0,255,0),(posx, posy), 10)
        pygame.display.update()
        time.sleep(0.02)
        pygame.draw.circle(area, (255,255,255),(posx, posy), 10)
        posx-=10
        posy-=x
        x-=0.7
        print(posy)
    pygame.draw.circle(area, (0,255,0),(posx, posy), 10)
    pygame.display.update()
    time.sleep(50)