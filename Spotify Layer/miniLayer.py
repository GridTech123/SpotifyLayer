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
    os.chdir('backgroundImages')
    background = pygame.image.load('background.png')
    background2 = pygame.image.load('background2.png')
    os.chdir('..')
    os.chdir('images')
    pause = pygame.image.load('pause.png')
    unpause = pygame.image.load('unpause.png')
    back = pygame.image.load('back.png')
    settings = pygame.image.load('settings.png')
    check = pygame.image.load('check.png')
    cross = pygame.image.load('cross.png')
    logo = pygame.image.load('logo.png')
    menuBack = pygame.image.load('menuBack.png')
    move = pygame.image.load('move.png')
    close = pygame.image.load('close.png')
    errorStrip = pygame.image.load('errorStrip.png')
    more = pygame.image.load('downArrow.png')
    less = pygame.image.load('upArrow.png')
    os.chdir('..')
except:
    pyError.newError('temp Error', 'There was an error on start', 'there was an issue getting images', 20, 20) 

#setup
clock = pygame.time.Clock()

try:
    from win32api import *
except:
    pyError.newError('temp Error', 'There was an error on start', 'there was an issue importing win32api(pywin32), make sure to use exe', 20, 20)   
try:  
    #print "Width =", GetSystemMetrics(0)
    #print "Height =", GetSystemMetrics(1)
    location = ((GetSystemMetrics(0) / 2) - (700 / 2), 0)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (location)
    pygame.init()
    screen_x = 700
    screen_y = 110
    screen = pygame.display.set_mode([screen_x,screen_y], NOFRAME)
    middlex = screen_x/2
    middley = screen_y/2
except:
    pyError.newError('poly cities Error', 'There was an error on start', 'We dont know what happened', 20, 20)  

#fonts
menu_font = pygame.font.SysFont('Calibri', 40)
hud_font = pygame.font.SysFont('Calibri', 40)
hud_font2 = pygame.font.SysFont('Calibri', 20)
big_font = pygame.font.SysFont('Calibri', 50)
title_font = pygame.font.SysFont('Calibri', 100)


#vars
moveTrig = False
error = 0
moreScreen = False
lyricsMenu = False

#window settings
pygame.display.set_icon(logo)
pygame.display.set_caption("Spotify Layer")

sx = 700
sy = 110
x1 = 0
x2 = sx - sx - sx
#program
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(gray)
    clock.tick(200)
    mx, my = pygame.mouse.get_pos()

    background = pygame.transform.scale(background, (sx + 10, sy))
    background2 = pygame.transform.scale(background2, (sx + 10, sy))
    menuBack = pygame.transform.scale(menuBack, (sx, 160))
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
            songDisplay = songDisplay

        if spotilib.artist() != 'There is noting playing at this moment':
            artistDisplay = spotilib.artist()
        else:
            artistDisplay = artistDisplay
    except:
        songDisplay = ":'("
        artistDisplay = 'An error occured'            

    screen.blit(big_font.render(songDisplay, True, black),(10, 20 + error))
    screen.blit(menu_font.render(artistDisplay, True, black),(10, 70 + error))

    screen.blit(move, (1, 1))
    if mx > 1 and mx < 21 and my > 1 and my < 21:
        if event.type == MOUSEBUTTONDOWN and event.button == 1:     
            pygame.display.iconify()

    screen.blit(close, (31, 1))
    if mx > 31 and mx < 51 and my > 1 and my < 21:
        if event.type == MOUSEBUTTONDOWN and event.button == 1:  
            try:   
                os.startfile('Spotify_Layer.exe')
            except:
                os.startfile('Spotify_Layer.py')
            sys.exit()

    if moreScreen == False:
        screen.blit(more, (61, 1))
        if mx > 61 and mx < 81 and my > 1 and my < 21:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:  
                    errorStrip = pygame.transform.scale(errorStrip, (sx, sy))
                    screen.blit(errorStrip, (0,0))
                    screen.blit(big_font.render('Please wait', True, black),(100, 0))
                    error = 100   
                    display.update()

                    screen_x = 700
                    screen_y = 160
                    screen = pygame.display.set_mode([screen_x,screen_y], NOFRAME)
                    middlex = screen_x/2
                    middley = screen_y/2

                    error = 0
                    moreScreen = True

    elif moreScreen == True:
        screen.blit(less, (61, 1))
        if mx > 61 and mx < 81 and my > 1 and my < 21:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:  
                    errorStrip = pygame.transform.scale(errorStrip, (sx, sy))
                    screen.blit(errorStrip, (0,0))
                    screen.blit(big_font.render('Please wait', True, black),(100, 0))
                    error = 100   
                    display.update()

                    screen_x = 700
                    screen_y = 110
                    screen = pygame.display.set_mode([screen_x,screen_y], NOFRAME)
                    middlex = screen_x/2
                    middley = screen_y/2

                    error = 0
                    moreScreen = False

    if moreScreen == True:
        if mx > 0 and mx < sx and my > 110 and my < 160:
            pygame.draw.rect(screen, blue3, [0, 110, sx, 50])
            if event.type == MOUSEBUTTONDOWN and event.button == 1:  
                lyricsMenu = True
                errorStrip = pygame.transform.scale(errorStrip, (sx, sy))
                screen.blit(errorStrip, (0,0))
                screen.blit(big_font.render('Please wait', True, black),(100, 0))
                error = 100   
                display.update()

                screen_x = 700
                screen_y = 110
                screen = pygame.display.set_mode([screen_x,screen_y], NOFRAME)
                middlex = screen_x/2
                middley = screen_y/2

                error = 0
                moreScreen = False
        else:
            pygame.draw.rect(screen, blue2, [0, 110, sx, 50])
        screen.blit(hud_font.render('Lyrics', True, black),(0, 110))

    s = subprocess.check_output('tasklist', shell=True)
    if not "Spotify.exe" in s:
        errorStrip = pygame.transform.scale(errorStrip, (sx, sy))
        screen.blit(errorStrip, (0,0))
        screen.blit(big_font.render('Spotify is not running', True, black),(100, 0))
        error = 100
    else:
        error = 0

    if lyricsMenu == True:
        screen.blit(menuBack, (0,0))
        screen.blit(hud_font.render('Generating Lyrics', True, black),(sx / 2 - 100, 110))
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

    clock.tick(20)
    display.update()
