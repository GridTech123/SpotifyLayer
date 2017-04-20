import os
import cx_Freeze

executables = [cx_Freeze.Executable('Spotify_Layer.py')]

cx_Freeze.setup(name = 'Spotify Layer', version = '2.1.0', options = {'build_exe': {'packages':['spotilib', 'pygame', 'pygame.locals', 'pickle', 'pyError', 'tkFileDialog', 'Grid_Vertex'], 'include_files':["images", 'html', 'themes', 'theme files']}}, executables = executables)
