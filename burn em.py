#Message From Admin Virus
#This Is Not Made To Be A Malicious Virus So I Do Not Accept Responsibility For Anything Illegal Done With This Code
#All Illegal Action Is Entirely Your  Fault And Not Mine (Read Above)
#You Can Change The Message From Admin And Ello Governor Parts To Suit Yourself
#Created By VoDkAdRiNkErBoI

import time
import pygame
import os

pygame.init()

screen = pygame.display.set_mode((250,150))
pygame.display.set_caption('Message From Admin')
font = pygame.font.SysFont("Lucida Console", 20)
label = font.render("Ello Governor", 1, (0,0,0))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            time.sleep(0.5)

            screen = pygame.display.set_mode((250,150))
            pygame.display.set_ caption('Message From Admin')


    screen.fill((255,255,255))
    screen.blit(labbel, (50,50))

    pygame.display.update()
    
