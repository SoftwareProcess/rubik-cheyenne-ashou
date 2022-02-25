class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, content=None):
        self._content = content

    def _load(self, content):
        self._content = content
    
    def _get(self):
        pass