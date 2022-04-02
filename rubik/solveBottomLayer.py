'''
The purpose of this module is to solve
the bottom layer of the Rubik's cube

Created: 4/1/2022
Modified: 4/1/2022
@author: Cheyenne Ashou
'''
from tkinter.constants import BOTTOM

def _checkSolved(content):
    solved = True
    
    sideFaces = 4
    
    for face in range(sideFaces):
        bottomRow = [content[face][2][0],content[face][2][1], content[face][2][2]]
        expectedColor = content[face][1][1]
        if (bottomRow[0] != expectedColor or bottomRow[1] != expectedColor 
            or bottomRow[2] != expectedColor):
            solved = False
            break
        
    bottomLayer = content[5]
    bottomLayerColor = content[5][1][1]  
        
    for row in bottomLayer:
        for piece in row:
            if piece != bottomLayerColor:
                solved = False
                break

    return solved

def _getCornerPiece(content):
    
    frontCorners = {
            'topLeft': content[0][0][0]
            , 'topRight': content[0][0][2]
            , 'bottomLeft': content[0][2][0]
            , 'bottomRight': content[0][2][2]
            }
    
    adjacentLeftCorners = {'upper': content[4][2][0], 'left': content[3][0][2],
                           'bottomLeft': content[3][2][2], 'lower': content[5][0][0]}
    adjacentRightCorners = {'upper': content[4][2][2], 'right': content[1][0][0],
                            'bottomRight': content[1][2][0], 'lower': content[5][0][2]}
    
    bottomFaceColor = content[5][1][1]
    frontFaceColor = content[0][1][1]
    leftFaceColor = content[3][1][1]
    rightFaceColor = content[1][1][1]
    
    if(frontCorners['topLeft'] == frontFaceColor 
       and adjacentLeftCorners['upper'] == leftFaceColor
       and adjacentLeftCorners['left'] == bottomFaceColor):
        return (0,0, 'luL')
    if(frontCorners['topRight'] == frontFaceColor
       and adjacentRightCorners['upper'] == rightFaceColor
       and adjacentRightCorners['right'] == bottomFaceColor):
        return (0,2, 'RUr')
    if(frontCorners['bottomLeft'] == bottomFaceColor):
        return (2,0, 'luL')
    if(frontCorners['bottomRight'] == bottomFaceColor):
        return (2,2, 'RUr')
    if(adjacentLeftCorners['lower'] == bottomFaceColor
       and (frontCorners['bottomLeft'] != frontFaceColor
            or adjacentLeftCorners['bottomLeft'] != leftFaceColor)):
        return (2,0)
    if(adjacentRightCorners['lower'] == bottomFaceColor
       and (frontCorners['bottomRight'] != frontFaceColor
            or adjacentRightCorners['right'] != rightFaceColor)):
        return (2,2)
    if(adjacentLeftCorners['upper'] == bottomFaceColor):
        return (0,0)
    if(adjacentRightCorners['upper'] == bottomFaceColor):
        return (0,2)
    
    
        
