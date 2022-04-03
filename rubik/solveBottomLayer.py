'''
The purpose of this module is to solve
the bottom layer of the Rubik's cube

Created: 4/1/2022
Modified: 4/1/2022
@author: Cheyenne Ashou
'''
import rubik.solve as solve


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
        return (2,0, 'FUf')
    if(frontCorners['bottomRight'] == bottomFaceColor):
        return (2,2, 'fuF')
    if(adjacentLeftCorners['lower'] == bottomFaceColor
       and (frontCorners['bottomLeft'] != frontFaceColor
            or adjacentLeftCorners['bottomLeft'] != leftFaceColor)):
        return (2,0, 'luL')
    if(adjacentRightCorners['lower'] == bottomFaceColor
       and (frontCorners['bottomRight'] != frontFaceColor
            or adjacentRightCorners['right'] != rightFaceColor)):
        return (2,2, 'RUr')
    if(_checkPiecesOnTopLayer(content) == False and adjacentLeftCorners['upper'] == bottomFaceColor):
        return (0,0, 'lUUL')
    if(_checkPiecesOnTopLayer(content) == False and adjacentRightCorners['upper'] == bottomFaceColor):
        return (0,2, 'RUUr')
    
def _checkPiecesOnTopLayer(content):
    sideFaces = 4
    bottomFaceColor = content[5][1][1]
    piecesOnTopLayer = False
    
    for face in range(sideFaces):
        if(content[face][0][0] == bottomFaceColor 
           or content[face][0][2] == bottomFaceColor):
            piecesOnTopLayer = True
            break
        
    return piecesOnTopLayer
    
def _findOpenCorner(content):
    sideFaces = 4
    bottomFaceColor = content[5][1][1]
    
    for face in range(sideFaces):
        leftCorner = content[0][2][0]
        topLeftOfBottomFace = content[5][0][0]
        bottomRightOfLeftFace = content[3][2][2]
        if(topLeftOfBottomFace != bottomFaceColor
           or leftCorner == bottomFaceColor
           or bottomRightOfLeftFace == bottomFaceColor):
            return face
        content = solve._rotateCubeClockwise(content)
    return None

def _openCorner(content):
    leftCorner = content[0][2][0]
    topLeftOfBottomFace = content[5][0][0]
    bottomRightOfLeftFace = content[3][2][2]
    bottomFaceColor = content[5][1][1]
    frontFaceColor = content[0][1][1]
    leftFaceColor = content[3][2][2]
    
    openCorner = True
    
    if(topLeftOfBottomFace == bottomFaceColor and leftCorner == frontFaceColor
       and bottomRightOfLeftFace == leftFaceColor):
        openCorner = False
    else:
        openCorner = True
    
    return openCorner

