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

def _checkEdgePlaced(content, edge):
    if(edge == 'left'):
        frontFaceEdgeColor = content[0][1][0]
        sideFaceEdgeColor = content[3][1][2]
        frontFaceColor = content[0][1][1]
        sideFaceColor = content[3][1][1]
    elif(edge == 'right'):
        frontFaceEdgeColor = content[0][1][2]
        sideFaceEdgeColor = content[1][1][2]
        frontFaceColor = content[0][1][1]
        sideFaceColor = content[1][1][1]
    else:
        print('Check edge input for _checkEdgePlaced')
    placed = True
    if(frontFaceEdgeColor != frontFaceColor or sideFaceEdgeColor != sideFaceColor):
        placed = False
    return placed

def _findEdge(content, edge):
    frontFaceColor = content[0][1][1]
    if(edge == 'left'):
        sideFaceColor = content[3][1][1]
    elif(edge == 'right'):
        sideFaceColor = content[1][1][1]
    sideFaces = 4
    for face in range(sideFaces):
        frontEdgeColor = content[0][0][1]
        sideEdgeColor = content[4][2][1]
        if(frontEdgeColor == frontFaceColor and sideEdgeColor == sideFaceColor):
            content = solve._rotateToFrontFace(content, face)
            return face
        else:
            content = solve._rotateCubeClockwise(content)
    return sideFaces

def _rotateEdgeToAdjacentFace(content, startingFace, edge):
    if(edge == 'left'):
        endingFace = 1
        moves = solve.optimalUpperRotation(content, startingFace, endingFace)
    elif(edge == 'right'):
        endingFace = 3
        moves = solve.optimalUpperRotation(content, startingFace, endingFace)
    else:
        print('error: 600 Check _rotateEdgeToAdjacentFace edge input')
        moves = ''
    return moves

def _checkTopColorEdgePieceInTopLayer(content):
    #it is okay when there is atleast 1 yellow edge available
    #if no yellow edges available, take edge misplaced edge out
    sideFaces = 4
    
    topFaceColor = content[4][1][1]
    okay = True
    for face in range(sideFaces):
        topFaceEdgePiece = content[4][2][1]
        print('topFaceEdgePiece ', topFaceEdgePiece)
        print('edgepiece: ',content[face][0][1])
        if(content[face][0][1] == topFaceColor or topFaceEdgePiece == topFaceColor):
            content = solve._rotateToFrontFace(content, face)
            return face
        else:
            content = solve._rotateCubeClockwise(content)
    okay = False
    return sideFaces
