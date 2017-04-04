import os
import cx_Freeze

executables = [cx_Freeze.Executable('Spotify_Layer.py'), cx_Freeze.Executable('miniLayer.py'), cx_Freeze.Executable('welcome.py')]

cx_Freeze.setup(name = 'Spotify Layer', version = '1.8.1', options = {'build_exe': {'packages':['spotilib', 'pygame', 'pygame.locals', 'pickle', 'pyError', 'tkFileDialog', 'Grid_Vertex'], 'include_files':["images", 'backgrounds', 'backgroundImages', 'lyricBack.png', 'html']}}, executables = executables)
