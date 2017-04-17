import spotilib
from shutil import copyfile

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
    logo = pygame.image.load('logo.png')
    settings = pygame.image.load('cog.png')
    share = pygame.image.load('share.png')
    back = pygame.image.load('back.png')
    starClicked = pygame.image.load('starClicked.png')
    starNotClicked = pygame.image.load('starNotClicked.png')
    blockedClicked = pygame.image.load('blockClicked.png')
    blockedNotClicked = pygame.image.load('blockNotClicked.png')
    menuBack = pygame.image.load('menuBack.png')
    lyrics = pygame.image.load('lyrics.png')
    os.chdir('..')
except:
    pyError.newError('temp Error', 'There was an error on start', 'there was an issue getting images', 20, 20) 

#setup
clock = pygame.time.Clock()

#vars
rendermode = 0
shareMenu = False
lyricsMenu = False
gvWait = 29
gvDebug = False
try:
    pickle_in = open('favSongs.sl', 'r+')
    favSongs = pickle.load(pickle_in)
except:
    favSongs = []
    pickle_out = open('favSongs.sl', 'w')
    pickle.dump(favSongs, pickle_out)
    pickle_out.close()

try:
    pickle_in = open('banSongs.sl', 'r')
    banSongs = pickle.load(pickle_in)
except:
    banSongs = []
    pickle_out = open('banSongs.sl', 'w')
    pickle.dump(banSongs, pickle_out)
    pickle_out.close()

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

def note(text):
    pygame.draw.rect(screen, gray, [sx - 400, sy - 300, 400, 200])
    screen.blit(hud_font.render(text, True, black), (sx - 400, sy - 300))
    display.update()

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
    screen.fill(gray2)
    clock.tick(200)
    mx, my = pygame.mouse.get_pos()

    if rendermode == 0:
        if spotilib.song() != 'There is noting playing at this moment':
            song = spotilib.song()
        else:
            song = song
        songText = big_font.render(song, True, black)
        songrect = songText.get_rect()
        songrect.centerx = screen.get_rect().centerx
        screen.blit(songText, (songrect))

        if spotilib.song() != 'There is noting playing at this moment':
            artist = spotilib.artist()
        else:
            artist = artist
        artistText = hud_font.render(artist, True, black)
        artistrect = artistText.get_rect()
        artistrect.centerx = screen.get_rect().centerx
        artistrect.centery = 150
        screen.blit(artistText, (artistrect))

        pygame.draw.rect(screen, gray3, [0,0,50,sy])
        #settings
        screen.blit(settings, (0,0))
        if mx > 0 and mx < 100 and my > 0 and my < 50:
           pygame.draw.rect(screen, gray, [50, 0 , 200, 50]) 
           screen.blit(hud_font.render('settings', True, black), (50, 0))
           if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 'settings'
                pygame.time.wait(100)
        #share
        screen.blit(share, (0,60))
        if mx > 0 and mx < 100 and my > 60 and my < 110:
           pygame.draw.rect(screen, gray, [50, 60 , 200, 50]) 
           screen.blit(hud_font.render('share', True, black), (50, 60))
           if event.type == MOUSEBUTTONDOWN and event.button == 1:
                shareMenu = True
                pygame.time.wait(100)
        #lyrics
        screen.blit(lyrics, (0,120))
        if mx > 0 and mx < 100 and my > 120 and my < 170:
           pygame.draw.rect(screen, gray, [50, 120 , 200, 50]) 
           screen.blit(hud_font.render('lyrics', True, black), (50, 120))
           if event.type == MOUSEBUTTONDOWN and event.button == 1:
                lyricsMenu = True
                pygame.time.wait(100)

        if not spotilib.song() in favSongs:
            screen.blit(starNotClicked, (5, sy - 100)) 
            if mx > 5 and mx < 45 and my > sy - 100 and my < sy - 100 + 40:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    favSongs.append(str(spotilib.song()))
                    pickle_out = open('favSongs.sl', 'r+')
                    pickle.dump(favSongs, pickle_out)
                    pickle_out.close()
                    pygame.time.wait(100)
        else:
            screen.blit(starClicked, (5, sy - 100)) 
            if mx > 5 and mx < 45 and my > sy - 100 and my < sy - 100 + 40:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    favSongs.remove(spotilib.song())
                    pickle_out = open('favSongs.sl', 'r+')
                    pickle.dump(favSongs, pickle_out)
                    pickle_out.close()
                    pygame.time.wait(100)

        if not spotilib.song() in banSongs:
            screen.blit(blockedNotClicked, (5, sy - 50)) 
            if mx > 5 and mx < 45 and my > sy - 50 and my < sy - 50 + 40:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    banSongs.append(str(spotilib.song()))
                    pickle_out = open('banSongs.sl', 'r+')
                    pickle.dump(banSongs, pickle_out)
                    pickle_out.close()
        else:
            screen.blit(blockedClicked, (5, sy - 50)) 
            spotilib.next()
            pygame.time.wait(500)
            if mx > (sx / 2) - (90 / 2) + 200 and mx < (sx / 2) - (90 / 2) + 200 + 40 and my > 160 + 45 and my < 160 + 45 + 40:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    banSongs.remove(spotilib.song())
                    pickle_out = open('banSongs.sl', 'r+')
                    pickle.dump(banSongs, pickle_out)
                    pickle_out.close()


    elif rendermode == 'settings':
        screen.blit(back, (0,0))
        if mx > 0 and mx < 50 and my > 0 and my < 50:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 0
                pygame.time.wait(100)
        
        if gvDebug == False:
            pygame.draw.rect(screen, gray, [0, 100, 300, 50])
            screen.blit(hud_font.render('turn on gv debug', True, black), (0, 100))
            if mx > 0 and mx < 300 and my > 100 and my < 150:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:      
                    gvDebug = True
                    pygame.time.delay(100)
        elif gvDebug == True:
            pygame.draw.rect(screen, gray, [0, 100, 300, 50])
            screen.blit(hud_font.render('turn off gv debug', True, black), (0, 100))
            if mx > 0 and mx < 300 and my > 100 and my < 150:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:      
                    gvDebug = False
                    pygame.time.delay(100)

    if shareMenu == True:
        note('Generating share script')
        f = open('share.html', 'w')
        f.write('<html><head></head><body>')
        f.write('<h1>Favorite Songs</h1>')
        songClock = 0
        while True:
            try:
                f.write('<h4>'+str(favSongs[songClock])+('</h4>'))
                songClock = songClock + 1
            except:
                if songClock == 0:
                    os.write('<h3>You have no favorite songs</h3>')
                break
        f.write('</body></html>')
        f.close()
        os.startfile('share.html')
        shareMenu = False

    if lyricsMenu == True:
        note('Generating lyric script')
        artistEmbed = artist.replace(' ', '-')
        artistEmbed = artistEmbed.replace("'", '-')
        songEmbed = song.replace(' ', '-')
        songEmbed = songEmbed.replace("'", '-')
        f = open('lyrics.html', 'w')
        f.write('<html><head></head><body>')
        f.write('<div><iframe src="http://www.musixmatch.com/lyrics/'+str(artistEmbed)+str('/')+str(songEmbed)+str('/embed?theme=light" style="border:none;background:transparent;" width="100%" height="100%" border=0></iframe></div>'))
        f.write('</body></html>')
        f.close()
        os.startfile('lyrics.html')
        lyricsMenu = False

    if gvDebug == True:
        if gv == True:
            if gvWait > 100:
                note('gv updated')
            else:
                note('time until update ' +str(gvWait))

    if gv == True:
        if gvWait > 100:
            Grid_Vertex.send(song + ' - '+str(artist), 'Spotify Layer')
            gvWait = 0
        else:
            gvWait = gvWait + 1

    display.update()