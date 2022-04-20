'''
Created on Apr 17, 2022

@author: cheyennea.
'''
import rubik.check as check
import rubik.solve as solve

NO_EDGE = 4

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
    totalMoves = ''
    face = 0
    solved = _checkSolved(content)
    while(solved == False):
        moves = _insertEdges(content)
        totalMoves += solve._movetranslator(face, moves)
        moves = _removeMisorientedEdges(content)
        totalMoves += solve._movetranslator(face, moves)
        solved = _checkSolved(content)
        if(solved == False):
            face = (face + 1) % 4
            content = solve._rotateCubeClockwise(content)
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
    
    if(_checkEdgePlaced(content, 'left') == False and 
       leftEdgeColors['frontFace'] != topFaceColor and 
       leftEdgeColors['leftFace'] != topFaceColor):
        edge = 'left'
    elif(_checkEdgePlaced(content, 'right') == False and 
         rightEdgeColors['frontFace'] != topFaceColor and
         rightEdgeColors['rightFace'] != topFaceColor):
        edge = 'right'
    else:
        edge = 'none'
    return edge

def _insertLeftEdge(content, leftEdgePlaced):
    moves = ''
    if(leftEdgePlaced == False):
        leftEdgeFace = _findEdge(content, 'left')
        if(leftEdgeFace != NO_EDGE):
            edge = 'left'
            moves = _rotateEdgeToAdjacentFace(content, leftEdgeFace, edge)
            moves += _movesToInsertEdge(edge)
            content = solve._movecontroller(content, moves)  
    return moves

def _insertRightEdge(content, rightEdgePlaced):
    moves = ''
    if(rightEdgePlaced == False):
        rightEdgeFace = _findEdge(content, 'right')
        if(rightEdgeFace != NO_EDGE):
            edge = 'right'
            moves = _rotateEdgeToAdjacentFace(content, rightEdgeFace, edge)
            moves += _movesToInsertEdge(edge)
            content = solve._movecontroller(content, moves)  
    return moves

def _removeMisorientedLeftEdge(content):
    misorientedEdge = _checkMisorientedEdge(content)
    moves = ''
    topFaceColor = content[4][1][1]
    if(misorientedEdge == 'left'):
        adjacentRightFaceEdgePiece = content[1][0][1]
        adjacentRightFaceUpperEdgePiece = content[4][1][2]
        if(adjacentRightFaceEdgePiece != topFaceColor
           and adjacentRightFaceUpperEdgePiece != topFaceColor):
            replacementEdgeFace = _findTopColorEdgePieceInTopLayer(content)
        else:
            replacementEdgeFace = 1
        moves = _rotateEdgeToAdjacentFace(content, replacementEdgeFace, misorientedEdge)
        moves += _movesToInsertEdge(misorientedEdge)
        content = solve._movecontroller(content, moves)

    return moves

def _removeMisorientedRightEdge(content):
    misorientedEdge = _checkMisorientedEdge(content)
    moves = ''
    topFaceColor = content[4][1][1]
    if(misorientedEdge == 'right'):
        adjacentRightFaceEdgePiece = content[3][0][1]
        adjacentRightFaceUpperEdgePiece = content[4][1][0]
        if(adjacentRightFaceEdgePiece != topFaceColor
           and adjacentRightFaceUpperEdgePiece != topFaceColor):
            replacementEdgeFace = _findTopColorEdgePieceInTopLayer(content)
        else:
            replacementEdgeFace = 3
        moves = _rotateEdgeToAdjacentFace(content, replacementEdgeFace, misorientedEdge)
        moves += _movesToInsertEdge(misorientedEdge)
        content = solve._movecontroller(content, moves)
    return moves

def _removeMisorientedEdges(content):
    moves = ''
    moves += _removeMisorientedLeftEdge(content)
    moves += _removeMisorientedRightEdge(content)
    return moves

def _insertEdges(content):
    leftEdgePlaced = _checkEdgePlaced(content, 'left')
    rightEdgePlaced = _checkEdgePlaced(content, 'right')
    moves = ''
    moves += _insertLeftEdge(content, leftEdgePlaced)
    moves += _insertRightEdge(content, rightEdgePlaced)
    return moves
