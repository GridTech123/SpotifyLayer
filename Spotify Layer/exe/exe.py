import cx_Freeze

executables = [cx_Freeze.Executable('Spotify_Layer.pyw')]

cx_Freeze.setup(name = 'Spotify Layer', version = '1.2.0', options = {'build_exe': {'packages':['spotilib', 'pygame', 'pygame.locals', 'pickle', 'pyError', 'tkFileDialog'], 'include_files':['back.png',
                                                                                                                                                                                              'background.png',
                                                                                                                                                                                              'check.png',
                                                                                                                                                                                              'cross.png',
                                                                                                                                                                                              'pause.png',
                                                                                                                                                                                              'settings.png',
                                                                                                                                                                                              'unpause.png']}}, executables = executables)
