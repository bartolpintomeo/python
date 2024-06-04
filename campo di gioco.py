import pygame
import time
pygame.init()

area=pygame.display.set_mode((400,400))
area.fill((255,255,255))
pygame.draw.circle(area, (0,0,0), (350, 175),75)
pygame.draw.circle(area, (255,255,255), (360, 175),75)
pygame.draw.circle(area, (0,0,0), (50, 175),75)
pygame.draw.circle(area, (255,255,255), (40, 175),75)
pygame.draw.line(area,(0,0,0),(350,100),(350,250))
pygame.draw.line(area,(0,0,0),(50,100),(50,250))
pygame.draw.line(area,(0,0,0),(50,100),(350,100))
pygame.draw.line(area,(0,0,0),(50,250),(350,250))
pygame.draw.circle(area, (0,0,0), (200,175), 10)
pygame.draw.circle(area, (255,255,255), (200,175), 8)
pygame.draw.line(area,(0,0,0),(200,100),(200,250))
pygame.display.update()
time.sleep(50)
