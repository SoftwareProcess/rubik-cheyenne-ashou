'''
The purpose of this project is to output the rotations
required to solve a given rubik cube. It also allows a user
to input rotations on a cube.

Modified: 3/21/2022
@author:  Cheyenne Ashou
'''


import rubik.cube as cube
import rubik.check as check
import rubik.solveBottomLayer as bottomLayer
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
        result['solution'] = _topFlower(content)    
    else:
        myCube._content = _movecontroller(content, moves)
        result['cube'] = myCube._get()
    
    result['status'] = 'ok'
    
    return result

#Rotate the cube to get a 'flower' at the top face
def _topFlower(content):  
    moves = ''
    
    bottomFaceColor = content[5][1][1]
    
    flowerPiecesOnFace = True
    face = 0 
    flowerSolved = False
    
    while(flowerSolved == False):
        while(flowerPiecesOnFace == True):
            leftFrontLayer = content[0][1][0] 
            if(leftFrontLayer == bottomFaceColor):
                leftFlower = content[4][1][0]
                while(leftFlower == bottomFaceColor):
                    content = _movecontroller(content, 'U')
                    leftFlower = content[4][1][0]
                    moves += _movetranslator(face, 'U')
                content = _movecontroller(content, 'l') 
                moves += _movetranslator(face, 'l')
            
            rightFrontLayer = content[0][1][2]
            
            if(rightFrontLayer == bottomFaceColor): 
                rightFlower = content[4][1][2]
                while(rightFlower == bottomFaceColor):
                    content = _movecontroller(content, 'U')
                    rightFlower = content[4][1][2]
                    moves += _movetranslator(face, 'U')
                content = _movecontroller(content, 'R') 
                moves += _movetranslator(face, 'R')
            
            bottomFrontLayer = content[0][2][1]
            if(bottomFrontLayer == bottomFaceColor): 
                bottomFlower = content[4][2][1]
                while(bottomFlower == bottomFaceColor):
                    content = _movecontroller(content, 'U')
                    bottomFlower = content[4][2][1]  
                    moves += _movetranslator(face, 'U')
                content = _movecontroller(content, 'FUl') 
                moves += _movetranslator(face, 'FUl')
            
            topFrontLayer = content[0][0][1]
            if(topFrontLayer == bottomFaceColor):    
                bottomFlower = content[4][2][1]
                while(bottomFlower == bottomFaceColor):
                    content = _movecontroller(content, 'U')
                    bottomFlower = content[4][2][1]
                    moves += _movetranslator(face, 'U')  
                content = _movecontroller(content, 'fUl')
                moves += _movetranslator(face, 'fUl')
            
            topBottomLayer = content[5][0][1]    
            middleFrontLayer = content[0][1][1]
            if(topBottomLayer == bottomFaceColor and bottomFrontLayer != middleFrontLayer): #Bring flower pieces that are on bottom layer to top layer
                bottomFlower = content[4][2][1]
                while(bottomFlower == bottomFaceColor):
                    content = _movecontroller(content, 'U')
                    bottomFlower = content[4][2][1] 
                    moves += _movetranslator(face, 'U')
                content = _movecontroller(content, 'FF') 
                moves += _movetranslator(face, 'FF')
            
            flowerPiecesOnFace = _checkFlowerPieces(content)    

        flowerSolved = _solvedFlower(content)
        
        if(flowerSolved == False):
            content = _rotateCubeClockwise(content)
            flowerPiecesOnFace = True
            face = (face + 1) % 4
            
    content = _rotateToFrontFace(content, face)
    
    moves += _formBottomCross(content)
    
    return moves

#Shift the orientation of the cube to the original orientation
def _rotateToFrontFace(content, face):
    while(face != 0):
        content = _rotateCubeClockwise(content)
        face = (face + 1) % 4
    return content

#Checks if more moves are required on the current face
def _checkFlowerPieces(content):
    bottomFaceColor = content[5][1][1]
    flowerPiecesOnFace = True
    if(content[0][0][1] != bottomFaceColor): 
        if(content[0][1][0] != bottomFaceColor):
            if(content[0][1][2] != bottomFaceColor): 
                if(content[0][2][1] != bottomFaceColor):
                    if(content[5][0][1] != bottomFaceColor or 
                       (content[5][0][1] == bottomFaceColor and 
                        content[0][2][1] == content[0][1][1])):
                        flowerPiecesOnFace = False
    return flowerPiecesOnFace

#Forms a bottom cross after the flower has been made
def _formBottomCross(content):
    bottomFaceColor = content[5][1][1]
    matching = False
    moves = ''
    for face in range(0,4):
        matching = False
        while(matching == False):
            move = _movetranslator(face, 'FF')
            translatedU = _movetranslator(face, 'U')
            topPiece = content[face][0][1]
            middlePiece = content[face][1][1]
            bottomPiece = content[face][2][1]
            if(face == 0):
                adjacentFlowerPiece = content[4][2][1]
                adjacentCrossPiece = content[5][0][1]
                if(topPiece == middlePiece and  adjacentFlowerPiece == bottomFaceColor):
                    content = _movecontroller(content, move)
                    moves += move
                    matching = True
                elif(bottomPiece == middlePiece and adjacentCrossPiece == bottomFaceColor):
                    matching = True
                else:
                    content = _movecontroller(content, translatedU)
                    moves += translatedU
            elif(face == 1):
                adjacentFlowerPiece = content[4][1][2]
                adjacentCrossPiece = content[5][1][2]
                if(topPiece == middlePiece and adjacentFlowerPiece == bottomFaceColor):
                    content = _movecontroller(content, move)
                    moves += move
                    matching = True
                elif(bottomPiece == middlePiece and adjacentCrossPiece == bottomFaceColor):
                    matching = True
                else:
                    content = _movecontroller(content, translatedU)
                    moves += translatedU
            elif(face == 2):
                adjacentFlowerPiece = content[4][0][1]
                adjacentCrossPiece = content[5][2][1]
                if(topPiece == middlePiece and adjacentFlowerPiece == bottomFaceColor):
                    content = _movecontroller(content, move)
                    moves += move
                    matching = True
                elif(bottomPiece == middlePiece and adjacentCrossPiece == bottomFaceColor):
                    matching = True
                else:
                    content = _movecontroller(content, translatedU)
                    moves += translatedU
            elif(face == 3):
                adjacentFlowerPiece = content[4][1][0]
                adjacentCrossPiece = content[5][1][0]
                if(topPiece == middlePiece and adjacentFlowerPiece == bottomFaceColor):
                    content = _movecontroller(content, move)
                    moves += move
                    matching = True
                elif(bottomPiece == middlePiece and adjacentCrossPiece == bottomFaceColor):
                    matching = True
                else:
                    content = _movecontroller(content, translatedU)
                    moves += translatedU
    return moves

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

#Determines if flower is solved
def _solvedFlower(content):
    bottomFaceColor = content[5][1][1]
    flowerCount = 0
    for face in range(0,4):
        if(face == 0):
            if(content[4][2][1] == bottomFaceColor):
                flowerCount += 1
            if(content[5][0][1] == bottomFaceColor and content[face][1][1] == content[face][2][1]):
                flowerCount += 1
        if(face == 1):
            if(content[4][1][2] == bottomFaceColor):
                flowerCount += 1
            if(content[5][1][2] == bottomFaceColor and content[face][1][1] == content[face][2][1]):
                flowerCount += 1
        if(face == 2):
            if(content[4][0][1] == bottomFaceColor): 
                flowerCount += 1
            if(content[5][2][1] == bottomFaceColor and content[face][1][1] == content[face][2][1]):
                flowerCount += 1
        if(face == 3):
            if(content[4][1][0] == bottomFaceColor):
                flowerCount += 1
            if(content[5][1][0] == bottomFaceColor and content[face][1][1] == content[face][2][1]):
                flowerCount += 1
        
    if(flowerCount == 4):
        return True
    else:
        return False
    
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
def _movecontroller(content, moves):
    for move in moves:
        if move == 'F':
            face = 0
            content[face] = _clockwise(content[face])
            content = _switchedge(content, move)
        elif move == 'f':
            face = 0
            content[face] = _counterclockwise(content[face])
            content = _switchedge(content, move)
            content = _switchedge(content, move)
            content = _switchedge(content, move)
        elif move == 'R':
            face = 1
            content[face] = _clockwise(content[face])
            content = _switchedge(content, move)
        elif move == 'r':
            face = 1
            content[face] = _counterclockwise(content[face])
            content = _switchedge(content, move)
            content = _switchedge(content, move)
            content = _switchedge(content, move)
        elif move == 'B':
            face = 2
            content[face] = _clockwise(content[face])
            content = _switchedge(content, move)
        elif move == 'b':
            face = 2
            content[face] = _counterclockwise(content[face])
            content = _switchedge(content, move)
            content = _switchedge(content, move)
            content = _switchedge(content, move)
        elif move == 'L':
            face = 3
            content[face] = _clockwise(content[face])
            content = _switchedge(content, move)
        elif move == 'l':
            face = 3
            content[face] = _counterclockwise(content[face])
            content = _switchedge(content, move)
            content = _switchedge(content, move)
            content = _switchedge(content, move)
        elif move == 'U':
            face = 4
            content[face] = _clockwise(content[face])
            content = _switchedge(content, move)
        elif move == 'u':
            face = 4
            content[face] = _counterclockwise(content[face])
            content = _switchedge(content, move)
            content = _switchedge(content, move)
            content = _switchedge(content, move)
        elif move == 'D':
            face = 5
            content[face] = _clockwise(content[face])
            content = _switchedge(content, move)
        elif move == 'd':
            face = 5
            content[face] = _counterclockwise(content[face])
            content = _switchedge(content, move)
            content = _switchedge(content, move)
            content = _switchedge(content, move)
        elif move == 'M':
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

def _switchedge(cube, action):
    if (action == 'F' or action == 'f'):
        temp = cube[4][2]
        cube[4][2] = [cube[3][2][2], cube[3][1][2], cube[3][0][2]]
        
        cube[3][0][2] = cube[5][0][0]
        cube[3][1][2] = cube[5][0][1]
        cube[3][2][2] = cube[5][0][2]      
        
        cube[5][0] = [cube[1][2][0], cube[1][1][0], cube[1][0][0]]
        
        cube[1][0][0] = temp[0]
        cube[1][1][0] = temp[1]
        cube[1][2][0] = temp[2]
    elif(action == 'R' or action == 'r'):
        temp = [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
        
        cube[0][0][2] = cube[5][0][2]
        cube[0][1][2] = cube[5][1][2]
        cube[0][2][2] = cube[5][2][2]
        
        cube[5][0][2] = cube[2][2][0]
        cube[5][1][2] = cube[2][1][0]
        cube[5][2][2] = cube[2][0][0]
        
        cube[2][0][0] = cube[4][2][2]
        cube[2][1][0] = cube[4][1][2]
        cube[2][2][0] = cube[4][0][2]
        
        cube[4][0][2] = temp[0]
        cube[4][1][2] = temp[1]
        cube[4][2][2] = temp[2]
    elif(action == 'L' or action == 'l'):
        temp = [cube[0][0][0], cube[0][1][0], cube[0][2][0]]
        
        cube[0][0][0] = cube[4][0][0]
        cube[0][1][0] = cube[4][1][0]
        cube[0][2][0] = cube[4][2][0]
        
        cube[4][0][0] = cube[2][2][2]
        cube[4][1][0] = cube[2][1][2]
        cube[4][2][0] = cube[2][0][2]
        
        cube[2][0][2] = cube[5][2][0]
        cube[2][1][2] = cube[5][1][0]
        cube[2][2][2] = cube[5][0][0]
        
        cube[5][0][0] = temp[0]
        cube[5][1][0] = temp[1]
        cube[5][2][0] = temp[2]
    elif(action == 'B' or action == 'b'):
        temp = cube[4][0]
        cube[4][0] = [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
        
        cube[1][0][2] = cube[5][2][2]
        cube[1][1][2] = cube[5][2][1]
        cube[1][2][2] = cube[5][2][0]      
        
        cube[5][2] = [cube[3][0][0], cube[3][1][0], cube[3][2][0]]
        
        cube[3][0][0] = temp[2]
        cube[3][1][0] = temp[1]
        cube[3][2][0] = temp[0]
    elif(action == 'U' or action == 'u'):
        temp = cube[0][0]
        cube[0][0] = cube[1][0]
        cube[1][0] = cube[2][0]
        cube[2][0] = cube[3][0]
        cube[3][0] = temp
    elif(action == 'D' or action =='d'):
        temp = cube[0][2]
        cube[0][2] = cube[3][2]
        cube[3][2] = cube[2][2]
        cube[2][2] = cube[1][2]
        cube[1][2] = temp
    return cube

