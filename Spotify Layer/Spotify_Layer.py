import pygame
from pygame import *
from pygame.locals import *

pygame.init()
#fonts
menu_font = pygame.font.SysFont('Calibri', 40)
hud_font = pygame.font.SysFont('Calibri', 40)
hud_font2 = pygame.font.SysFont('Calibri', 20)
big_font = pygame.font.SysFont('Calibri', 80)
title_font = pygame.font.SysFont('Calibri', 100)
big2_font = pygame.font.SysFont('Calibri', 100)
big3_font = pygame.font.SysFont('Calibri', 200)

def loadingScreen(text):
    mode = RESIZABLE
    screen = pygame.display.set_mode([1920,1080], mode)
    screen.fill((0,0,0))
    screen.blit(pygame.image.load('logo.png'), (860, 440))
    screen.blit(hud_font.render('Loading: '+str(text), True, (255, 255, 255)), (0, 0))
    pygame.time.delay(50)
    pygame.display.update()

loadingScreen('spotilib')
import spotilib
loadingScreen('shutil')
from shutil import copyfile

try:
    loadingScreen('GridVertex')
    import Grid_Vertex
    Grid_Vertex.init()
    gv = True
except:
    gv = False

try:
    loadingScreen('os')
    import os
    loadingScreen('pygame')
    import pygame
    from pygame import *
    from pygame.locals import *
    loadingScreen('random')
    import random
    loadingScreen('sys')
    import sys
    loadingScreen('pickle')
    import pickle
    loadingScreen('time')
    import time
    loadingScreen('pyerror')
    import pyError
    loadingScreen('tkinter')
    from Tkinter import *
    from tkFileDialog import*
    loadingScreen('subprocess')
    import subprocess
except:
    os.chdir('html')
    os.startfile('missingModule.html')

try:
    loadingScreen('pyError')
    import pyError
except:
    os.chdir('html')
    os.startfile('missingPyError.html')

#colors
loadingScreen('color - white')
white = (255, 255, 255)
loadingScreen('color - black')
black = (0, 0, 0)
loadingScreen('color - blue')
blue = (0, 0, 255)
loadingScreen('color - blue2')
blue2 = (44, 157, 201)
loadingScreen('color - blue3')
blue3 = (8, 140, 196)
loadingScreen('color - blue4')
blue4 = (40, 181, 166)
loadingScreen('color - red')
red = (255, 0, 0)
loadingScreen('color - green')
green = (0, 255, 0)
loadingScreen('color - green2')
green2 = (0, 153, 0)
loadingScreen('color - green3')
green3 = (0,100,0)
loadingScreen('color - gray')
gray = (158, 156, 166)
loadingScreen('color - gray2')
gray2 = (69, 67, 68)
loadingScreen('color - gray3')
gray3 = (140, 138, 139)

#images
loadingScreen('Theme')
loadThemeClock = 0 
try:
    pickle_in = open('theme.sl', 'r+')
    loadThemeName = pickle.load(pickle_in)
except:
    pickle_out = open('theme.sl', 'w')
    pickle.dump('dark.txt', pickle_out)
    pickle_out.close()
    loadThemeName = 'dark.txt'

os.chdir('themes')
themes = os.listdir(os.getcwd())
themes.remove('temp.txt')
while True:
    try:
        if loadThemeName == themes[loadThemeClock]:
            themeNum = loadThemeClock
            break
        else:
            loadThemeClock = loadThemeClock + 1
    except:
        pyError.newError('Temp Error', 'There was an error on start', 'Error loading themes(none found)', 20, 20)   
theme = open(themes[themeNum],'r+')
themeLines = theme.read().splitlines()
themeFolder = themeLines[0]
backColor = themeLines[1]
os.chdir('..')
try:
    backColor = eval(backColor)
except:
    os.chdir('theme files')
    os.chdir(themeFolder)
    backImg = pygame.image.load(backColor)
    os.chdir('..')
    os.chdir('..')
sideColor = themeLines[2]
sideColor = eval(sideColor)
noteColor = themeLines[3]
noteColor = eval(noteColor)
textColor = themeLines[4]
textColor = eval(textColor)
os.chdir('theme files')
os.chdir(themeFolder)
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
os.chdir('..')


#setup
loadingScreen('var - clock')
clock = pygame.time.Clock()

#vars
loadingScreen('var - rendermode')
rendermode = 0
loadingScreen('var - shareMenu')
shareMenu = False
loadingScreen('var - lyricsMenu')
lyricsMenu = False
loadingScreen('var - gvWait')
gvWait = 29
loadingScreen('var - gvDebug')
gvDebug = False
loadingScreen('var - quit')
quit = False
loadingScreen('var - frames')
frames = 0
try:
    loadingScreen('var - favSongs')
    pickle_in = open('favSongs.sl', 'r+')
    favSongs = pickle.load(pickle_in)
except:
    favSongs = []
    pickle_out = open('favSongs.sl', 'w')
    pickle.dump(favSongs, pickle_out)
    pickle_out.close()

try:
    loadingScreen('var - banSongs')
    pickle_in = open('banSongs.sl', 'r')
    banSongs = pickle.load(pickle_in)
except:
    banSongs = []
    pickle_out = open('banSongs.sl', 'w')
    pickle.dump(banSongs, pickle_out)
    pickle_out.close()

#pygame start
loadingScreen('init sl')
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

#window settings
pygame.display.set_icon(logo)
pygame.display.set_caption("Spotify Layer")

#first time
loadingScreen('firststart.pcr')
try:
    pickle_in = open('firstStart.pcr', 'r')
    rendermode = 0
except:
    pickle_out = open('firstStart.pcr', 'w')
    pickle.dump(True, pickle_out)
    pickle_out.close()

def note(text):
    pygame.draw.rect(screen, noteColor, [sx - 400, sy - 300, 400, 200])
    screen.blit(hud_font.render(text, True, textColor), (sx - 400, sy - 300))
    display.update()

x1 = 0
x2 = sx - sx - sx
loadingScreen('starting...')
#program
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            Grid_Vertex.send(None, None)
            pygame.quit()
            sys.exit()
        elif event.type==VIDEORESIZE:
            loadingScreen('Resetting background')
            screen=pygame.display.set_mode(event.dict['size'], mode)
            sx, sy = screen.get_size()
            x1 = 0
            x2 = sx - sx - sx
            try:
                screen.fill(backColor)
            except:
                os.chdir('theme files')
                os.chdir(themeFolder)
                backImg = pygame.image.load(backColor)
                os.chdir('..')
                os.chdir('..')
            loadingScreen('resuming Spotify Layer')

    #settings
    try:
        screen.fill(backColor)
    except:
        screen.fill(white)
        backImg = transform.scale(backImg, (sx, sy))
        screen.blit(backImg, (0,0))
    clock.tick(200)
    mx, my = pygame.mouse.get_pos()

    if rendermode == 0:
        try:
            if spotilib.song() != 'There is noting playing at this moment':
                song = spotilib.song()
            else:
                song = song
            songText = big_font.render(song, True, textColor)
            songrect = songText.get_rect()
            songrect.centerx = screen.get_rect().centerx
            screen.blit(songText, (songrect))

            if spotilib.song() != 'There is noting playing at this moment':
                artist = spotilib.artist()
            else:
                artist = artist
            artistText = hud_font.render(artist, True, textColor)
            artistrect = artistText.get_rect()
            artistrect.centerx = screen.get_rect().centerx
            artistrect.centery = 150
            screen.blit(artistText, (artistrect))
        except:
            songText = big_font.render('An error occured', True, red)
            songrect = songText.get_rect()
            songrect.centerx = screen.get_rect().centerx
            screen.blit(songText, (songrect))

            artistText = hud_font.render('An error occured', True, red)
            artistrect = artistText.get_rect()
            artistrect.centerx = screen.get_rect().centerx
            artistrect.centery = 150
            screen.blit(artistText, (artistrect))

        pygame.draw.rect(screen, sideColor, [0,0,50,sy])
        #settings
        screen.blit(settings, (0,0))
        if mx > 0 and mx < 100 and my > 0 and my < 50:
           pygame.draw.rect(screen, sideColor, [50, 0 , 200, 50]) 
           screen.blit(hud_font.render('settings', True, textColor), (50, 0))
           if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 'settings'
                settingsFrame = frames
                pygame.time.wait(100)
        #share
        screen.blit(share, (0,60))
        if mx > 0 and mx < 100 and my > 60 and my < 110:
           pygame.draw.rect(screen, sideColor, [50, 60 , 600, 50]) 
           screen.blit(hud_font.render('View Favorite And Banned Songs', True, textColor), (50, 60))
           if event.type == MOUSEBUTTONDOWN and event.button == 1:
                shareMenu = True
                pygame.time.wait(100)
        #lyrics
        screen.blit(lyrics, (0,120))
        if mx > 0 and mx < 100 and my > 120 and my < 170:
           pygame.draw.rect(screen, sideColor, [50, 120 , 200, 50]) 
           screen.blit(hud_font.render('lyrics', True, textColor), (50, 120))
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

        screen.blit(menu_font.render('Grid Vertex:', True, black), (100, 10))
        
        if gvDebug == False:
            if mx > 100 and mx < 400 and my > 100 and my < 150:
                pygame.draw.rect(screen, noteColor, [100, 100, 300, 50])    
                screen.blit(hud_font.render('turn on gv debug', True, textColor), (100, 100))
                if event.type == MOUSEBUTTONDOWN and event.button == 1:      
                    gvDebug = True
                    pygame.time.delay(100)
            else:
                pygame.draw.rect(screen, sideColor, [100, 100, 300, 50])    
                screen.blit(hud_font.render('turn on gv debug', True, textColor), (100, 100))
        elif gvDebug == True:
            if mx > 100 and mx < 400 and my > 100 and my < 150:
                pygame.draw.rect(screen, noteColor, [100, 100, 300, 50])
                screen.blit(hud_font.render('turn off gv debug', True, textColor), (100, 100))
                if event.type == MOUSEBUTTONDOWN and event.button == 1:      
                    gvDebug = False
                    pygame.time.delay(100)
            else:
                pygame.draw.rect(screen, sideColor, [100, 100, 300, 50])
                screen.blit(hud_font.render('turn off gv debug', True, textColor), (100, 100))

        screen.blit(menu_font.render('Themes:', True, black), (100, 200))

        if frames == settingsFrame + 1:
            loadingScreen('Templates')
        themePickerClock = 0
        themePickerX = 100
        themePickerY = 300
        while True:
            try:
                if themes[themePickerClock] != '':
                    if mx > themePickerX and mx < themePickerX + 370 and my > themePickerY and my < themePickerY + 252:
                        pygame.draw.rect(screen, noteColor, [themePickerX, themePickerY, 370, 262])
                        screen.blit(hud_font.render(themes[themePickerClock], True, textColor), (themePickerX, themePickerY)) 
                        os.chdir('themes')
                        themesTemp = os.listdir(os.getcwd())
                        themesTemp.remove('temp.txt')
                        themeTemp = open(themes[themePickerClock], 'r+')
                        themeLinesTemp = themeTemp.read().splitlines()
                        os.chdir('..')
                        os.chdir('theme files')
                        os.chdir(themeLinesTemp[0])
                        tempImg = pygame.image.load('temp.jpg')
                        tempImg = transform.scale(tempImg, (320, 180))
                        screen.blit(tempImg, (themePickerX + 25, themePickerY + 50))
                        screen.blit(hud_font2.render('By: ' +str(themeLinesTemp[5]), True, textColor), (themePickerX, themePickerY + 240)) 
                        os.chdir('..')
                        os.chdir('..')
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:     
                            pickle_out = open('theme.sl', 'w')
                            pickle.dump(themes[themePickerClock], pickle_out)
                            pickle_out.close()
                            try:
                                os.startfile('Spotify_Layer.exe')
                            except:
                                os.startfile('Spotify_Layer.py')
                            quit = True
                    else:
                        pygame.draw.rect(screen, sideColor, [themePickerX, themePickerY, 370, 262])
                        screen.blit(hud_font.render(themes[themePickerClock], True, textColor), (themePickerX, themePickerY)) 
                        os.chdir('themes')
                        themesTemp = os.listdir(os.getcwd())
                        themesTemp.remove('temp.txt')
                        themeTemp = open(themes[themePickerClock], 'r+')
                        themeLinesTemp = themeTemp.read().splitlines()
                        os.chdir('..')
                        os.chdir('theme files')
                        os.chdir(themeLinesTemp[0])
                        tempImg = pygame.image.load('temp.jpg')
                        tempImg = transform.scale(tempImg, (320, 180))
                        screen.blit(tempImg, (themePickerX + 25, themePickerY + 50))
                        screen.blit(hud_font2.render('By: ' +str(themeLinesTemp[5]), True, textColor), (themePickerX, themePickerY + 240)) 
                        os.chdir('..')
                        os.chdir('..')
                    themePickerX = themePickerX + 400
                    themePickerClock = themePickerClock + 1
                    if themePickerX + 400 > sx:
                        themePickerX = 100
                        themePickerY = themePickerY + 275
                else:
                    break
            except:
                break

        if frames == settingsFrame + 1:
            loadingScreen('resuming Spotify Layer')
                
    if quit:
        sys.exit()

    if shareMenu == True:
        loadingScreen('Creating view Script - Preparing HTML')
        f = open('view.html', 'w')
        f.write('<script type="text/javascript" language="JavaScript">function HideContent(d) {document.getElementById(d).style.display = "none";}function ShowContent(d) {document.getElementById(d).style.display = "block";} function favButton() {HideContent("ban"); ShowContent("fav");} function banButton() {HideContent("fav"); ShowContent("ban");}</script>')
        f.write('''<html> <head><title>Favorite And Banned Songs</title></head> <style>#title{font-size: 30px; font-family: Arial; font-weight: bold; color: white; margin-left: 20px;} #text{font-size: 15px; font-family: Arial; color: white; margin: 20px;} #navbar{width: 100%; height: 80px; background-color: #333333;} #body{background-color: black; margin: 0px;} 
.button{background-color: #333333;
border: none;
color: white;
padding: 15px 32px;
text-align: center;
text-decoration: none;
display: inline-block;
font-size: 16px;
margin: 4px 2px;
cursor: pointer;
-webkit-transition-duration: 0.4s; /* Safari */
transition-duration: 0.4s;
font-family: Arial;
}
.button2:hover {
color: grey;
}
</style><body id=body onload="javascript: HideContent('ban')">''')
        f.write('<div id=navbar><h1 id=title>Favorite And Banned Songs</h1><h1 id=text>Favorite Songs: '+str(len(favSongs))+' | Banned Songs: ' +str(len(banSongs))+'</h1></div>')
        f.write('<div><a href="'+"javascript:favButton()"+'"'+"class='button button2'>Favorite Songs</a>")
        f.write('<a href="'+"javascript:banButton()"+'"'+"class='button button2'>Banned Songs</a></div>")
        songClock = 0
        f.write('<div id=fav>')
        while True:
            try:
                f.write('<h4 id=text>'+str(songClock + 1)+'. '+str(favSongs[songClock])+('</h4> \n'))
                loadingScreen('Creating view Script - Favorite Songs Added: ' +str(favSongs[songClock]))
                pygame.display.update()
                songClock = songClock + 1
            except:
                if songClock == 0:
                    f.write('<h3 id=text>You have no favorite songs</h3>')
                break
        f.write('</div>')
        songClock = 0
        f.write('<div id=ban>')
        while True:
            try:
                f.write('<h4 id=text>'+str(songClock + 1)+'. '+str(banSongs[songClock])+('</h4> \n'))
                loadingScreen('Creating view Script - Banned Songs Added: ' +str(banSongs[songClock]))
                pygame.display.update()
                songClock = songClock + 1
            except:
                if songClock == 0:
                    f.write('<h3 id=text>You have no banned songs</h3>')
                break
        f.write('</div>')
        loadingScreen('Creating view Script - finishing html')
        f.write('</body></html>')
        f.close()
        loadingScreen('Creating view Script - starting html')
        os.startfile('view.html')
        shareMenu = False
        loadingScreen('resuming Spotify Layer')

    if lyricsMenu == True:
        loadingScreen('Creating Lyrics Script')
        note('Generating lyric script')
        artistEmbed = artist.replace(' ', '-')
        artistEmbed = artistEmbed.replace("'", '-')
        songEmbed = song.replace(' ', '-')
        songEmbed = songEmbed.replace("'", '-')
        f = open('lyrics.html', 'w')
        f.write('<html> <head><title>Lyrics</title></head> <style>#title{font-size: 15px; font-family: Airial;}</style> <body>')
        f.write('<div><iframe src="http://www.musixmatch.com/lyrics/'+str(artistEmbed)+str('/')+str(songEmbed)+str('/embed?theme=dark" style="border:none;background:transparent;" width="100%" height="100%" border=0></iframe></div>'))
        f.write('</body></html>')
        f.close()
        os.startfile('lyrics.html')
        lyricsMenu = False
        loadingScreen('resuming Spotify Layer')

    if gvDebug == True:
        if gv == True:
            if gvWait > 100:
                note('gv updated')
            else:
                note('time until update ' +str(gvWait))

    if gv == True:
        try:
            if gvWait > 100:
                Grid_Vertex.send(song + ' - '+str(artist), 'Spotify Layer')
                gvWait = 0
            else:
                gvWait = gvWait + 1
        except:
            pass

    if frames == 0:
        loadingScreen('Resetting background')
        #screen=pygame.display.set_mode(event.dict['size'], mode)
        sx, sy = screen.get_size()
        x1 = 0
        x2 = sx - sx - sx
        try:
            screen.fill(backColor)
        except:
            os.chdir('theme files')
            os.chdir(themeFolder)
            backImg = pygame.image.load(backColor)
            os.chdir('..')
            os.chdir('..')
        loadingScreen('resuming Spotify Layer')
    frames = frames + 1
    display.update()