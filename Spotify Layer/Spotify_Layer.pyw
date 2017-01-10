import spotilib
try:
    import os
    import pygame
    from pygame import *
    from pygame.locals import *
    import random
    import sys
    import pickle
    import time
    import pyError
    from Tkinter import *
    from tkFileDialog import*
    import random
except:
    os.chdir('html')
    os.startfile('missingModule.html')

try:
    import pyError
except:
    os.chdir('html')
    os.startfile('missingPyError.html')

#colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
blue2 = (44, 157, 201)
blue3 = (8, 140, 196)
blue4 = (40, 181, 166)
red = (255, 0, 0)
green = (0, 255, 0)
green2 = (0, 153, 0)
green3 = (0,100,0)
gray = (158, 156, 166)
gray2 = (69, 67, 68)
gray3 = (140, 138, 139)

#images
try:
    os.chdir('images')
    background = pygame.image.load('background.png')
    pause = pygame.image.load('pause.png')
    unpause = pygame.image.load('unpause.png')
    back = pygame.image.load('back.png')
    os.chdir('..')
except:
    pyError.newError('temp Error', 'There was an error on start', 'there was an issue getting images', 20, 20) 

#setup
clock = pygame.time.Clock()

#vars
rendermode = 0

#pygame start
try:
    from win32api import GetSystemMetrics
except:
    pyError.newError('temp Error', 'There was an error on start', 'there was an issue importing win32api(pywin32), make sure to use exe', 20, 20)   
try:  
    #print "Width =", GetSystemMetrics(0)
    #print "Height =", GetSystemMetrics(1)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ( GetSystemMetrics(0) / 4, 1)
    pygame.init()
    wsx = GetSystemMetrics(0)
    wsy = GetSystemMetrics(1)
    sx = wsx - 100
    sy = wsy - 100
    mode = RESIZABLE
    screen = pygame.display.set_mode([sx,sy], mode)
except:
    pyError.newError('poly cities Error', 'There was an error on start', 'We dont know what happened', 20, 20)   

#fonts
menu_font = pygame.font.SysFont('Calibri', 40)
hud_font = pygame.font.SysFont('Calibri', 40)
hud_font2 = pygame.font.SysFont('Calibri', 20)
big_font = pygame.font.SysFont('Calibri', 80)
title_font = pygame.font.SysFont('Calibri', 100)

#window settings
#pygame.display.set_icon(logo)
pygame.display.set_caption("Spotify Layer")

#first time
try:
    pickle_in = open('firstStart.pcr', 'r')
    rendermode = 0
except:
    pickle_out = open('firstStart.pcr', 'w')
    pickle.dump(True, pickle_out)
    pickle_out.close()
    rendermode = 'firstStart'

#program
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==VIDEORESIZE:
            screen=pygame.display.set_mode(event.dict['size'], mode)
            sx, sy = screen.get_size()

    #settings
    screen.fill(gray)
    clock.tick(200)
    mx, my = pygame.mouse.get_pos()

    background = pygame.transform.scale(background, (sx, sy))
    screen.blit(background, (0,0))

    screen.blit(big_font.render(spotilib.song(), True, black),(400, 10))
    screen.blit(menu_font.render(spotilib.artist(), True, black),(400, 110))

    if spotilib.song() == 'There is nothing playing at this moment':
        screen.blit(unpause, ((sx / 2) - (90 / 2), 160))
        if mx > (sx / 2) - (90 / 2) and mx < (sx / 2) - (90 / 2) + 90 and my > 160 and my < 160 + 90:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                spotilib.play()
    else:
        screen.blit(pause, ((sx / 2) - (90 / 2), 160))
        if mx > (sx / 2) - (90 / 2) and mx < (sx / 2) - (90 / 2) + 90 and my > 160 and my < 160 + 90:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                spotilib.pause()

    screen.blit(unpause, ((sx / 2) - (90 / 2) + 100, 160))
    if mx > (sx / 2) - (90 / 2) + 100 and mx < (sx / 2) - (90 / 2) + 100 + 90 and my > 160 and my < 160 + 90:
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            spotilib.next()

    screen.blit(back, ((sx / 2) - (90 / 2) - 100, 160))
    if mx > (sx / 2) - (90 / 2) - 100 and mx < (sx / 2) - (90 / 2) - 100 + 90 and my > 160 and my < 160 + 90:
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            spotilib.previous()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:   
            spotilib.next()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:   
            spotilib.previous()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:   
            spotilib.pause()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:   
            spotilib.play()

    display.update()
