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
        sideFaceEdgeColor = content[1][1][0]
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

def _findTopColorEdgePieceInTopLayer(content):
    #it is okay when there is atleast 1 yellow edge available
    #if no yellow edges available, take edge misplaced edge out
    sideFaces = 4
    
    topFaceColor = content[4][1][1]
    for face in range(sideFaces):
        topFaceLowerEdgePiece = content[4][2][1]
        frontFaceUpperEdgePiece = content[0][0][1]
        if(frontFaceUpperEdgePiece == topFaceColor or topFaceLowerEdgePiece == topFaceColor):
            content = solve._rotateToFrontFace(content, face)
            return face
        else:
            content = solve._rotateCubeClockwise(content)
    return sideFaces

def _movesToInsertEdge(edge):
    if(edge == 'right'):
        moves = 'RurufUF'
    elif(edge == 'left'):
        moves = 'lULUFuf'
    else:
        moves = ''
        print('error: 601 Check _movesToInsertEdge edge input')
    return moves

def _solve(content):
    NO_EDGE = 4
    totalMoves = ''
    face = 0
    solved = _checkSolved(content)
    while(solved == False):
        leftEdgePlaced = _checkEdgePlaced(content, 'left')
        rightEdgePlaced = _checkEdgePlaced(content, 'right')
        if(leftEdgePlaced == True and rightEdgePlaced == True):
            solved = _checkSolved(content)
            content = solve._rotateCubeClockwise(content)
            face = (face + 1) % 4
            continue
        if(leftEdgePlaced == False):
            leftEdgeFace = _findEdge(content, 'left')
            if(leftEdgeFace != NO_EDGE):
                edge = 'left'
                move = _rotateEdgeToAdjacentFace(content, leftEdgeFace, edge)
                move += _movesToInsertEdge(edge)
                content = solve._movecontroller(content, move)  
                totalMoves += solve._movetranslator(face, move)       
        if(rightEdgePlaced == False):
            rightEdgeFace = _findEdge(content, 'right')
            if(rightEdgeFace != NO_EDGE):
                edge = 'right'
                move = _rotateEdgeToAdjacentFace(content, rightEdgeFace, edge)
                move += _movesToInsertEdge(edge)
                content = solve._movecontroller(content, move)
                totalMoves += solve._movetranslator(face, move)
        
        #if piece is valid edge piece, remove it, but make sure you switch it with yellow edge or correct edge
        # make sure to do checkEdgePlaced first so you don't remove the edge you just placed
        
        
        # if(_checkEdgePlaced(content, 'left') == False):
        #     topLayerEdgePieceFace = _findTopColorEdgePieceInTopLayer(content)
        #     if(topLayerEdgePieceFace != NO_EDGE):
        #         move = _rotateEdgeToAdjacentFace(content, topLayerEdgePieceFace, edge)
        #         move += _movesToInsertEdge(edge)
        #     else:
        #         move = _rotateEdgeToAdjacentFace(content, startingFace, edge)
        solved = _checkSolved(content)
        face = (face + 1) % 4
    content = solve._rotateToFrontFace(content, face)
    return totalMoves

def _checkMisorientedEdge(content):
    topFaceColor = content[4][1][1]
    leftEdgeColors = {'frontFace': content[0][1][0],
                      'leftFace': content[3][1][2]
                    }
    rightEdgeColors = {'frontFace': content[0][1][2],
                    'rightFace': content[1][1][0]
                    } 
    
    if(leftEdgeColors['frontFace'] != topFaceColor and 
       leftEdgeColors['leftFace'] != topFaceColor):
        edge = 'left'
    elif(rightEdgeColors['frontFace'] != topFaceColor and
         rightEdgeColors['rightFace'] != topFaceColor):
        edge = 'right'
    else:
        edge = 'none'
    return edge

def _checkGoToNextFace(content):
    leftEdgePlaced = _checkEdgePlaced(content, 'left')
    rightEdgePlaced = _checkEdgePlaced(content, 'right')
    goToNextFace = False
    
    if(leftEdgePlaced == True and rightEdgePlaced == True):
        goToNextFace = True
    
    return goToNextFace
