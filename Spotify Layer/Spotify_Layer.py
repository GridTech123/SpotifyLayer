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
    background2 = pygame.image.load('background2.png')
    pause = pygame.image.load('pause.png')
    unpause = pygame.image.load('unpause.png')
    back = pygame.image.load('back.png')
    settings = pygame.image.load('settings.png')
    check = pygame.image.load('check.png')
    cross = pygame.image.load('cross.png')
    logo = pygame.image.load('logo.png')
    menuBack = pygame.image.load('menuBack.png')
    samllWindow = pygame.image.load('smallWindow.png')
    os.chdir('..')
except:
    pyError.newError('temp Error', 'There was an error on start', 'there was an issue getting images', 20, 20) 

#setup
clock = pygame.time.Clock()

#vars
settingsMenu = False
fullscreen = False
songDisplay = ''
artistDisplay = ''

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
pygame.display.set_icon(logo)
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

x1 = 0
x2 = sx - sx - sx
#program
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==VIDEORESIZE:
            screen=pygame.display.set_mode(event.dict['size'], mode)
            sx, sy = screen.get_size()
            x1 = 0
            x2 = sx - sx - sx

    #settings
    screen.fill(gray)
    clock.tick(200)
    mx, my = pygame.mouse.get_pos()

    background = pygame.transform.scale(background, (sx + 10, sy))
    background2 = pygame.transform.scale(background2, (sx + 10, sy))
    menuBack = pygame.transform.scale(menuBack, (sx, sy))
    screen.blit(background, (x1, 0))
    screen.blit(background2, (x2, 0))

    if x1 < sx:
        x1 = x1 + 4
    else:
        x1 = sx - sx - sx

    if x2 < sx:
        x2 = x2 + 4
    else:
        x2 = sx - sx - sx

    try:
        if spotilib.song() != 'There is noting playing at this moment':
            songDisplay = spotilib.song()
        else:
            songDisplay = ''

        if spotilib.artist() != 'There is noting playing at this moment':
            artistDisplay = spotilib.artist()
        else:
            artistDisplay = ''
    except:
        songDisplay = ":'("
        artistDisplay = 'An error occured'            

    screen.blit(big_font.render(songDisplay, True, black),(400, 10))
    screen.blit(menu_font.render(artistDisplay, True, black),(400, 110))

    if spotilib.song() == 'There is noting playing at this moment':
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

    screen.blit(settings, (sx - 200, sy - 110))
    if mx > sx - 200 and mx < sx - 200 + 80 and my > sy - 110 and my < sy - 110 + 80:
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            settingsMenu = True

    screen.blit(samllWindow, (sx - 100, sy - 110))
    if mx > sx - 100 and mx < sx - 100 + 80 and my > sy - 110 and my < sy - 110 + 80:
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            try:
                os.startfile('miniLayer.exe')
            except:
                os.startfile('miniLayer.py')
            sys.exit()

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

    if settingsMenu == True:
        screen.blit(menuBack, (0,0))
        screen.blit(back, (10, 10))
        if mx > 10 and mx < 10 + 90 and my > 10 and my < 10 + 90:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                settingsMenu = False
        screen.blit(menu_font.render('Fullscreen: ', True, black),(100, 100))
        if fullscreen == False:
            screen.blit(cross, (300, 70))
            if mx > 300 and mx < 300 + 90 and my > 70 and my < 70 + 90:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:            
                    fullscreen = True
                    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ( GetSystemMetrics(0) / 4, 1)
                    pygame.init()
                    wsx = GetSystemMetrics(0)
                    wsy = GetSystemMetrics(1)
                    sx = wsx
                    sy = wsy
                    mode = FULLSCREEN
                    screen = pygame.display.set_mode([sx,sy], mode)
        elif fullscreen == True:
            screen.blit(check, (300, 70))
            if mx > 300 and mx < 300 + 90 and my > 70 and my < 70 + 90:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:            
                    fullscreen = False
                    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ( GetSystemMetrics(0) / 4, 1)
                    pygame.init()
                    wsx = GetSystemMetrics(0)
                    wsy = GetSystemMetrics(1)
                    sx = wsx - 100
                    sy = wsy - 100
                    mode = RESIZABLE
                    screen = pygame.display.set_mode([sx,sy], mode)

    clock.tick(18)
    display.update()
