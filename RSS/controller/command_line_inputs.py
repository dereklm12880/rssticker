import argparse

class ProcessCommandLine:
    def help(self):
        locationsDict = {
            'top': 'top',
            'topright':'topright',
            'right':'right',
            'bottomright':'bottomright',
            'bottom':'bottom',
            'bottomleft':'bottomleft',
            'left':'left',
            'topleft':'topleft',
        }

        print('move_window <location>: Specify window location', 
            ' location values: ', sep='\n')
        
        for l in locationsDict:
            print('\t', l, '\n')

    def move_window(self, location):
        