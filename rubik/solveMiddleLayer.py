'''
Created on Apr 17, 2022

@author: cheyennea.
'''
import rubik.check as check
import rubik.solve as solve
def _checkSolved(content):
    solved = True
    bottomSolved = check.checkBottomLayerSolved(content)
    middleSolved = check.checkMiddleLayerSolved(content)
    
    if(bottomSolved == False or middleSolved == False):
        solved = False
    
    return solved

def _checkLeftEdgePlaced(content):
    placed = True
    frontFaceEdgeColor = content[0][1][0]
    leftFaceEdgeColor = content[3][1][2]
    frontFaceColor = content[0][1][1]
    leftFaceColor = content[3][1][1]
    
    if(frontFaceEdgeColor != frontFaceColor or leftFaceEdgeColor != leftFaceColor):
        placed = False
    return placed

def _checkRightEdgePlaced(content):
    placed = True
    frontFaceEdgeColor = content[0][1][2]
    rightFaceEdgeColor = content[1][1][2]
    frontFaceColor = content[0][1][1]
    rightFaceColor = content[1][1][1]
    
    if(frontFaceEdgeColor != frontFaceColor or rightFaceEdgeColor != rightFaceColor):
        placed = False
    return placed

def _findLeftEdge(content):
    frontFaceColor = content[0][1][1]
    leftFaceColor = content[3][1][1]
    sideFaces = 4
    for face in range(sideFaces):
        frontEdgeColor = content[0][0][1]
        leftEdgeColor = content[4][2][1]
        if(frontEdgeColor == frontFaceColor and leftEdgeColor == leftFaceColor):
            solve._rotateToFrontFace(content, face)
            return face
        else:
            solve._rotateCubeClockwise(content)
    return sideFaces
    
        
        