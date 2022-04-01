class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, content=None):
        self._content = content
    def _load(self, content):
        cubearray=[
            [[], [], []],
            [[], [], []],
            [[], [], []],
            [[], [], []],
            [[], [], []],
            [[], [], []]
            ]

        faceindex = 0
        pieceindex = 0
        row = 0
        col = 0
   
        
        # Populate a 2d array with each piece of the cube
        for piece in content:
            cubearray[faceindex][row].append(piece)
            pieceindex += 1
            col += 1
            if(col % 3 == 0):
                col = 0
                row += 1
            if (row % 3 == 0):
                row = 0
            if(pieceindex % 9 == 0):
                faceindex += 1
                pieceindex = 0
            
        self._content = cubearray
    def _get(self):
        content = self._content
        copyofcontent = ''
        for face in content:
            for row in face:
                copyofcontent += ''.join(row)
        return copyofcontent
    
    def _getContent(self):
        return self._content