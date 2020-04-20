import argparse

class ProcessCommandLine:
    def help(self):
        locationsDict = {
            'top left': 'top left',
            'top right': 'top right',
            'bottom left': 'bottom left',
            'bottom right': 'bottom right'
        }

        print('move_window <location>: Specify window location', 
            ' location values: ', sep='\n')
        
        for l in locationsDict:
            print('\t', l, '\n')

    def move_window(self, location):
        if location == 'top left'
            window_placement('top left')
        elif location == 'top right'
            window_placement('top right')
        elif location == 'bottom left'
            window_placement('bottom left')
        elif location == 'bottom right'
            window_placement('bottom right')  