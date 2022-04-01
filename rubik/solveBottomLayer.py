'''
The purpose of this module is to solve
the bottom layer of the Rubik's cube

Created: 4/1/2022
Modified: 4/1/2022
@author: Cheyenne Ashou
'''

def _checkSolved(content):
    solved = True
    
    sideFaces = 4
    
    for face in range(sideFaces):
        bottomRow = [face[2][0],face[2][1], face[2][2]]
        expectedColor = face[1][1]
        if (bottomRow[0] != expectedColor or bottomRow[1] != expectedColor 
            or bottomRow[2] != expectedColor):
            solved = False
            break
        
    bottomLayer = 5
    bottomLayerColor = content[bottomLayer][1][1]  
        
    for piece in bottomLayer:
        if piece != bottomLayerColor:
            solved = False
            break
    
    return solved
        
