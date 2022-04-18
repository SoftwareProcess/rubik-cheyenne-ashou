'''
The purpose of this project is to output the rotations
required to solve a given rubik cube. It also allows a user
to input rotations on a cube.

Modified: 3/21/2022
@author:  Cheyenne Ashou
'''


import rubik.cube as cube
import rubik.check as check
import rubik.solveBottomCross as bottomCross
import rubik.insertBottomCorners as bottomCorners
#Driver method to solve cube
def _solve(parms):
    
    result = check._check(parms)
    
    if(result.get('status') != 'ok'):
        return result
    
    content = parms['cube']
    
    myCube = cube.Cube()
    myCube._load(content)
    content = myCube._getContent()
    moves = parms.get('rotate',None)
    
    if(moves == '' or moves == None):
        result['solution'] = bottomCross._solveBottomCross(content)
        result['solution'] += bottomCorners._movesToPlaceCornerPieces(content)
    else:
        myCube._content = _movecontroller(content, moves)
        result['cube'] = myCube._get()
        
    result['status'] = 'ok'
    
    return result



#Shift the orientation of the cube to the original orientation
def _rotateToFrontFace(content, face):
    while(face != 0):
        content = _rotateCubeClockwise(content)
        face = (face + 1) % 4
    return content




def _rotateMiddle(content):
    for face in range(0,4):
        if(face == 0):
            temp = content[face][1]
        if(face == 3):
            content[face][1] = temp
        else:
            content[face][1] = content[face+1][1]
        
    return content

def _rotateCubeClockwise(content):
    content = _movecontroller(content, 'UMd')
    return content 


#Used to print all moves relative to face 0, rather than relative to the current face        
def _movetranslator(face, moves):
    translatedMoves = ''
    if face == 0:
        return moves
    else:
        for move in moves:
            if face == 1:
                translatedMoves += _translateFace1(move)
            elif face == 2:
                translatedMoves += _translateFace2(move)
            elif face == 3:
                translatedMoves += _translateFace3(move)
            elif face == 4:
                translatedMoves += _translateFace4(move)
            elif face == 5:
                translatedMoves += _translateFace5(move)
        return translatedMoves
                
def _translateFace1(move):
    if move == 'F':
        return 'R'
    elif move == 'f':
        return 'r'
    elif move == 'B':
        return 'L'
    elif move == 'b':
        return 'l'
    elif move == 'L':
        return 'F'
    elif move == 'l':
        return 'f'
    elif move == 'R':
        return 'B'
    elif move == 'r':
        return 'b'
    elif move == 'U':
        return 'U'
    elif move == 'u':
        return 'u'
    elif move == 'D':
        return 'D'
    elif move == 'd':
        return 'd'
    
def _translateFace2(move):
    if move == 'F':
        return 'B'
    elif move == 'f':
        return 'b'
    elif move == 'B':
        return 'F'
    elif move == 'b':
        return 'f'
    elif move == 'L':
        return 'R'
    elif move == 'l':
        return 'r'
    elif move == 'R':
        return 'L'
    elif move == 'r':
        return 'l'
    elif move == 'U':
        return 'U'
    elif move == 'u':
        return 'u'
    elif move == 'D':
        return 'D'
    elif move == 'd':
        return 'd'
    
def _translateFace3(move):
    if move == 'F':
        return 'L'
    elif move == 'f':
        return 'l'
    elif move == 'B':
        return 'R'
    elif move == 'b':
        return 'r'
    elif move == 'L':
        return 'B'
    elif move == 'l':
        return 'b'
    elif move == 'R':
        return 'F'
    elif move == 'r':
        return 'f'
    elif move == 'U':
        return 'U'
    elif move == 'u':
        return 'u'
    elif move == 'D':
        return 'D'
    elif move == 'd':
        return 'd'

def _translateFace4(move):
    if move == 'F':
        return 'U'
    elif move == 'f':
        return 'u'
    elif move == 'B':
        return 'D'
    elif move == 'b':
        return 'd'
    elif move == 'L':
        return 'L'
    elif move == 'l':
        return 'l'
    elif move == 'R':
        return 'R'
    elif move == 'r':
        return 'r'
    elif move == 'U':
        return 'B'
    elif move == 'u':
        return 'b'
    elif move == 'D':
        return 'F'
    elif move == 'd':
        return 'f'
    
def _translateFace5(move):
    if move == 'F':
        return 'D'
    elif move == 'f':
        return 'd'
    elif move == 'B':
        return 'U'
    elif move == 'b':
        return 'u'
    elif move == 'L':
        return 'L'
    elif move == 'l':
        return 'l'
    elif move == 'R':
        return 'R'
    elif move == 'r':
        return 'r'
    elif move == 'U':
        return 'F'
    elif move == 'u':
        return 'f'
    elif move == 'D':
        return 'B'
    elif move == 'd':
        return 'b'
    
#Rotate cube

def frontRotations(content, move):
    normalMoves = {'F': 0, 'R': 1, 'B': 2, 'L': 3, 'U': 4, 'D': 5 }
    primeMoves = {'f': 0, 'r': 1, 'b':2, 'l': 3, 'u': 4, 'd': 5}
    if move in normalMoves:
        face = normalMoves[move]
        content[face] = _clockwise(content[face])
        content = _switchedge(content, move)
    elif move in primeMoves:
        face = primeMoves[move]
        content[face] = _counterclockwise(content[face])
        content = _switchedge(content, move)
        content = _switchedge(content, move)
        content = _switchedge(content, move)
    return content

def _movecontroller(content, moves):
    for move in moves:
        content = frontRotations(content, move)
        if move == 'M':
            content = _rotateMiddle(content)
    return content
        

def _clockwise(face):
    rowlength = len(face)
    for row in range(0, int(rowlength / 2)):
        for col in range(row, rowlength-1-row):
            temp = face[row][col]
            face[row][col] = face[rowlength-1-col][row]
            face[rowlength-1-col][row] = face[rowlength-1-row][rowlength-1-col]
            face[rowlength-1-row][rowlength-1-col] = face[col][rowlength-1-row]
            face[col][rowlength-1-row] = temp
    return face


def _counterclockwise(face):
    rowlength = len(face[0])
    for row in range(0, int(rowlength / 2)):
        for col in range(row, rowlength-1-row):
            temp = face[row][col]
            face[row][col] = face[col][rowlength-1-row]
            face[col][rowlength-1-row] = face[rowlength-1-row][rowlength-1-col]
            face[rowlength-1-row][rowlength-1-col] = face[rowlength-1-col][row]
            face[rowlength-1-col][row] = temp
    return face


def switchFrontEdges(cube):
    firstEdge = cube[4][2]
    cube[4][2] = [cube[3][2][2], cube[3][1][2], cube[3][0][2]]
    cube[3][0][2] = cube[5][0][0]
    cube[3][1][2] = cube[5][0][1]
    cube[3][2][2] = cube[5][0][2]
    cube[5][0] = [cube[1][2][0], cube[1][1][0], cube[1][0][0]]
    cube[1][0][0] = firstEdge[0]
    cube[1][1][0] = firstEdge[1]
    cube[1][2][0] = firstEdge[2]
    return cube


def switchRightEdges(cube):
    firstEdge = [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
    cube[0][0][2] = cube[5][0][2]
    cube[0][1][2] = cube[5][1][2]
    cube[0][2][2] = cube[5][2][2]
    cube[5][0][2] = cube[2][2][0]
    cube[5][1][2] = cube[2][1][0]
    cube[5][2][2] = cube[2][0][0]
    cube[2][0][0] = cube[4][2][2]
    cube[2][1][0] = cube[4][1][2]
    cube[2][2][0] = cube[4][0][2]
    cube[4][0][2] = firstEdge[0]
    cube[4][1][2] = firstEdge[1]
    cube[4][2][2] = firstEdge[2]
    return cube


def switchLeftEdges(cube):
    firstEdge = [cube[0][0][0], cube[0][1][0], cube[0][2][0]]
    cube[0][0][0] = cube[4][0][0]
    cube[0][1][0] = cube[4][1][0]
    cube[0][2][0] = cube[4][2][0]
    cube[4][0][0] = cube[2][2][2]
    cube[4][1][0] = cube[2][1][2]
    cube[4][2][0] = cube[2][0][2]
    cube[2][0][2] = cube[5][2][0]
    cube[2][1][2] = cube[5][1][0]
    cube[2][2][2] = cube[5][0][0]
    cube[5][0][0] = firstEdge[0]
    cube[5][1][0] = firstEdge[1]
    cube[5][2][0] = firstEdge[2]
    return cube


def switchBackEdges(cube):
    firstEdge = cube[4][0]
    cube[4][0] = [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
    cube[1][0][2] = cube[5][2][2]
    cube[1][1][2] = cube[5][2][1]
    cube[1][2][2] = cube[5][2][0]
    cube[5][2] = [cube[3][0][0], cube[3][1][0], cube[3][2][0]]
    cube[3][0][0] = firstEdge[2]
    cube[3][1][0] = firstEdge[1]
    cube[3][2][0] = firstEdge[0]
    return cube


def siwthcUpperEdges(cube):
    firstEdge = cube[0][0]
    cube[0][0] = cube[1][0]
    cube[1][0] = cube[2][0]
    cube[2][0] = cube[3][0]
    cube[3][0] = firstEdge
    return cube


def switchDownwardsEdges(cube):
    firstEdge = cube[0][2]
    cube[0][2] = cube[3][2]
    cube[3][2] = cube[2][2]
    cube[2][2] = cube[1][2]
    cube[1][2] = firstEdge
    return cube

def _switchedge(cube, action):
    if (action == 'F' or action == 'f'):
        cube = switchFrontEdges(cube)
    elif(action == 'R' or action == 'r'):
        cube = switchRightEdges(cube)
    elif(action == 'L' or action == 'l'):
        cube = switchLeftEdges(cube)
    elif(action == 'B' or action == 'b'):
        cube = switchBackEdges(cube)
    elif(action == 'U' or action == 'u'):
        cube = siwthcUpperEdges(cube)
    elif(action == 'D' or action =='d'):
        cube = switchDownwardsEdges(cube)
    return cube

def optimalUpperRotation(content, startingFace, endingFace):
    difference = endingFace - startingFace
    if(abs(difference) == 2):
        rotations = 'UU'
    elif(difference <= -3):
        rotations = 'u'
    elif(difference >= 3):
        rotations = 'U'
    elif(difference == -1):
        rotations = 'U'
    elif(difference == 1):
        rotations = 'u'
    elif(difference == -3):
        rotations = 'u'
    return rotations
    
    
    

