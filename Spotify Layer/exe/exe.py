import os
import cx_Freeze

executables = [cx_Freeze.Executable('Spotify_Layer.py'), cx_Freeze.Executable('miniLayer.py')]

cx_Freeze.setup(name = 'Spotify Layer', version = '1.4.0', options = {'build_exe': {'packages':['spotilib', 'pygame', 'pygame.locals', 'pickle', 'pyError', 'tkFileDialog'], 'include_files':["back.png",
"background.png",
"background2.png",
"check.png",
"close.png",
"cross.png",
"logo.png",
"menuBack.png",
"move.png",
"pause.png",
"settings.png",
"smallWindow.png",
"unpause.png"]}}, executables = executables)
