#Message From Admin Virus
#This Is Not Made To Be A Malicious Virus So I Do Not Accept Responsibility For Anything Illegal Done With This Code
#Created By VoDkAdRiNkErBoI

import time
import pygame
import os

pygame.init()

screen = pygame.display.set_mode((250,150))
pygame.display.set_caption('Message From Admin')
font = pygame.font.SysFont("Lucida Console", 20)
label = font.render("U R A MORON", 1, (0,0,0))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            time.sleep(0.10)

            screen = pygame.display.set_mode((250,150))
            pygame.display.set_ caption('Message From Admin')


    screen.fill((255,255,255))
    screen.blit(labbel, (50,50))

    pygame.display.update()
    
