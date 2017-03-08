import os
import cx_Freeze

executables = [cx_Freeze.Executable('Spotify_Layer.py'), cx_Freeze.Executable('miniLayer.py')]

cx_Freeze.setup(name = 'Spotify Layer', version = '1.6.0', options = {'build_exe': {'packages':['spotilib', 'pygame', 'pygame.locals', 'pickle', 'pyError', 'tkFileDialog'], 'include_files':["images", 'backgrounds', 'backgroundImages', 'lyricBack.png']}}, executables = executables)
