import spotilib

try:
    import Grid_Vertex
    Grid_Vertex.init()
    gv = True
except:
    gv = False

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
    import subprocess
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
    pause = pygame.image.load('pause.png')
    unpause = pygame.image.load('unpause.png')
    back = pygame.image.load('back.png')
    settings = pygame.image.load('settings.png')
    check = pygame.image.load('check.png')
    cross = pygame.image.load('cross.png')
    logo = pygame.image.load('logo.png')
    menuBack = pygame.image.load('menuBack.png')
    samllWindow = pygame.image.load('smallWindow.png')
    errorStrip = pygame.image.load('errorStrip.png')
    lyrics = pygame.image.load('lyricsLogo.png')
    os.chdir('..')
except:
    pyError.newError('temp Error', 'There was an error on start', 'there was an issue getting images', 20, 20) 

#setup
clock = pygame.time.Clock()
os.chdir('backgroundImages')
try:
    backgroundInfo = open('backgroundData.txt', 'r')
    backgroundLines = backgroundInfo.readlines()
    backgroundType = backgroundLines[0]
    line2 = backgroundLines[2]
    if backgroundType == '2\n':
        background = pygame.image.load(line2[0:len(line2)-1])
        line3 = backgroundLines[3]
        background2 = pygame.image.load(line3[0:len(line3)])
    elif backgroundType == '1\n':
        background = pygame.image.load(line2[0:len(line2)])
except:
    backgroundInfo = open('background1.png.txt', 'r')
    backgroundLines = backgroundInfo.readlines()
    backgroundType = backgroundLines[0]
    line2 = backgroundLines[2]
    if backgroundType == '2\n':
        background = pygame.image.load(line2[0:len(line2)-1])
        line3 = backgroundLines[3]
        background2 = pygame.image.load(line3[0:len(line3)])
    elif backgroundType == '1\n':
        background = pygame.image.load(line2[0:len(line2)])
os.chdir('..')

#vars
settingsMenu = False
fullscreen = False
songDisplay = ''
artistDisplay = ''
error = 0
lyricsMenu = False
presentationMode = False
fpsMode = True

#pygame start
try:
    from win32api import GetSystemMetrics
except:
    pyError.newError('temp Error', 'There was an error on start', 'there was an issue importing win32api(pywin32), make sure to use exe', 20, 20)   
try:  
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
big2_font = pygame.font.SysFont('Calibri', 100)
big3_font = pygame.font.SysFont('Calibri', 200)

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
            Grid_Vertex.send(None, None)
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
    menuBack = pygame.transform.scale(menuBack, (sx, sy))
    screen.blit(background, (x1, 0))
    try:
        background2 = pygame.transform.scale(background2, (sx + 10, sy))
        screen.blit(background2, (x2, 0))
    except:
        pass

    if backgroundType == '2\n':
        if fpsMode == False:
            if x1 < sx:
                x1 = x1 + 4
            else:
                x1 = sx - sx - sx

            if x2 < sx:
                x2 = x2 + 4
            else:
                x2 = sx - sx - sx
    elif backgroundType == '1\n':
        x1 = x1

    try:
        if spotilib.song() != 'There is noting playing at this moment':
            songDisplay = spotilib.song()
        else:
            songDisplay = songDisplay

        if spotilib.artist() != 'There is noting playing at this moment':
            artistDisplay = spotilib.artist()
        else:
            artistDisplay = artistDisplay
    except:
        errorStrip = pygame.transform.scale(errorStrip, (sx, 100))
        screen.blit(errorStrip, (0,0))
        screen.blit(big_font.render('An error occured', True, black),(0, 0))
        error = 100
        songDisplay = ""
        artistDisplay = ''            

    if presentationMode == True:
        if fpsMode == False:
            screen.blit(big3_font.render(songDisplay, True, gray2),(403, 13 + error))
        screen.blit(big3_font.render(songDisplay, True, white),(400, 10 + error))
        screen.blit(big2_font.render(artistDisplay, True, white),(400, 200 + error))

    if presentationMode == False:
        if fpsMode == False:
            screen.blit(big_font.render(songDisplay, True, gray2),(403, 13 + error))
        screen.blit(big_font.render(songDisplay, True, white),(400, 10 + error))
        screen.blit(menu_font.render(artistDisplay, True, white),(400, 110 + error))

    if presentationMode == False:
        if fpsMode == False:
            if spotilib.song() == 'There is noting playing at this moment':
                screen.blit(unpause, ((sx / 2) - (90 / 2), 160 + error))
                if mx > (sx / 2) - (90 / 2) and mx < (sx / 2) - (90 / 2) + 90 and my > 160 and my < 160 + 90:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        spotilib.play()
            else:
                screen.blit(pause, ((sx / 2) - (90 / 2), 160 + error))
                if mx > (sx / 2) - (90 / 2) and mx < (sx / 2) - (90 / 2) + 90 and my > 160 and my < 160 + 90:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        spotilib.pause()

            screen.blit(unpause, ((sx / 2) - (90 / 2) + 100, 160 + error))
            if mx > (sx / 2) - (90 / 2) + 100 and mx < (sx / 2) - (90 / 2) + 100 + 90 and my > 160 and my < 160 + 90:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    spotilib.next()

            screen.blit(back, ((sx / 2) - (90 / 2) - 100, 160 + error))
            if mx > (sx / 2) - (90 / 2) - 100 and mx < (sx / 2) - (90 / 2) - 100 + 90 and my > 160 and my < 160 + 90:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    spotilib.previous()

            screen.blit(lyrics, (sx - 300, sy - 110))
            if mx > sx - 300 and mx < sx - 300 + 80 and my > sy - 110 and my < sy - 110 + 80:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    lyricsMenu = True

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

    if fpsMode == False:
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

    if lyricsMenu == True:
        screen.blit(menuBack, (0,0))
        screen.blit(menu_font.render('Generating Lyrics', True, black),(sx / 2 - 100, sy / 2))
        pygame.display.update()
        artistEmbed = artistDisplay.replace(' ', '-')
        artistEmbed = artistEmbed.replace("'", '-')
        songEmbed = songDisplay.replace(' ', '-')
        songEmbed = songEmbed.replace("'", '-')
        f = open('lyrics.html', 'w')
        f.write('<html><head></head><body>')
        f.write('<image src="lyricBack.png" width="100%">')
        f.write('<div><iframe src="http://www.musixmatch.com/lyrics/'+str(artistEmbed)+str('/')+str(songEmbed)+str('/embed?theme=light" style="border:none;background:transparent;" width="100%" height="100%" border=0></iframe></div>'))
        f.write('</body></html>')
        f.close()
        os.startfile('lyrics.html')
        lyricsMenu = False

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

        screen.blit(menu_font.render('presentation mode: ', True, black),(100, 200))
        if presentationMode == False:
            screen.blit(cross, (450, 170))
            if mx > 450 and mx < 450 + 90 and my > 170 and my < 170 + 90:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:            
                    presentationMode = True
        elif presentationMode == True:
            screen.blit(check, (450, 170))
            if mx > 450 and mx < 450 + 90 and my > 170 and my < 170 + 90:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:            
                    presentationMode = False

        screen.blit(menu_font.render('Background: ', True, black),(100, 300))
        os.chdir('backgrounds')
        backgrounds = os.listdir(os.getcwd())
        backgroundClock = 0
        backgroundX = 100
        backgroundY = 360
        while True:
            try:
                loadingBackground = pygame.image.load(backgrounds[backgroundClock])
                loadingBackground = pygame.transform.scale(loadingBackground, (190, 190))
                if mx > backgroundX and mx < backgroundX + 200 and my > backgroundY and my < backgroundY + 200:
                    pygame.draw.rect(screen, blue4, [backgroundX, backgroundY, 200, 200])   
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        os.chdir('..')
                        os.chdir('backgroundImages')
                        backgroundInfo = open(backgrounds[backgroundClock]+str('.txt'), 'r')
                        backgroundLines = backgroundInfo.readlines()
                        backgroundType = backgroundLines[0]
                        line2 = backgroundLines[2]
                        if backgroundType == '2\n':
                            background = pygame.image.load(line2[0:len(line2)-1])
                            line3 = backgroundLines[3]
                            background2 = pygame.image.load(line3[0:len(line3)])
                        elif backgroundType == '1\n':
                            background = pygame.image.load(line2[0:len(line2)])
                        x1 = 0
                        x2 = sx - sx - sx
                        w = open('backgroundData.txt', 'w')
                        w.write(backgroundLines[0])
                        w.write(backgroundLines[1])
                        w.write(backgroundLines[2])
                        if backgroundType == '2\n':
                            w.write(backgroundLines[3])
                        w.close()
                        os.chdir('..')           
                        settingsMenu = False   
                        break     
                else:
                    pygame.draw.rect(screen, blue3, [backgroundX, backgroundY, 200, 200])
                screen.blit(loadingBackground, (backgroundX + 5, backgroundY + 5))
                backgroundClock = backgroundClock + 1
                backgroundX = backgroundX + 210
                if backgroundX + 200 + 100 > sx:
                    backgroundY = backgroundY + 210
                    backgroundX = 0
            except:
                os.chdir('..')
                break

    s = subprocess.check_output('tasklist', shell=True)
    if not "Spotify.exe" in s:
        errorStrip = pygame.transform.scale(errorStrip, (sx, 100))
        screen.blit(errorStrip, (0,0))
        screen.blit(big_font.render('Spotify is not running', True, black),(0, 0))
        error = 100
    elif not clock.get_fps < 4:
        error = 0

    if clock.get_fps() < 4:
        errorStrip = pygame.transform.scale(errorStrip, (sx, 100))
        screen.blit(errorStrip, (0,0))
        screen.blit(big_font.render('You are in Low FPS mode', True, black),(0, 0))
        error = 100 
        fpsMode = True
    else:
        error = 0
        fpsMode = False

    if gv == True:
        Grid_Vertex.send(songDisplay + ' - '+str(artistDisplay), 'Spotify Layer')

    clock.tick(18)
    display.update()