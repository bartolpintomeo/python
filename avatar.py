import pygame
import time
pygame.init()

area=pygame.display.set_mode((500,500))
area.fill((255,255,255))
face=300
eyes=250
raggio=100
raggiom=raggio
rect=pygame.Rect((200,280), (raggio+20, raggiom))

pygame.draw.circle(area,(0,0,0),(260,face),raggio)
pygame.draw.circle(area,(255,255,255),(260,face),(raggio-3))
pygame.draw.arc(area, (0,0,0), rect, 3.14, 0)
pygame.draw.circle(area,(0,0,0),(225,eyes),raggio/5)
pygame.draw.circle(area,(0,0,0),(295,eyes),raggio/5)
pygame.display.update()
time.sleep(1)
for z in range(0,10):
    pygame.draw.line(area,(0,0,0),(200,328),(320,328))
    pygame.display.update()
    time.sleep(0.5)
    pygame.draw.line(area,(255,255,255),(200,328),(320,328))
    pygame.display.update()
    time.sleep(0.5)