import rubik.cube as cube
import rubik.check as check
from pickle import FALSE
def _solve(parms):
    
    result = check._check(parms)
    
    if(result.get('status') != 'ok'):
        return result
    
    content = parms['cube']
    
    myCube = cube.Cube()
    myCube._load(content)
    moves = parms.get('rotate',None)
    
    if(moves == '' or moves == None):
        result['solution'] = _bottomFlower(myCube)   
    else:
        myCube._content = _movecontroller(myCube, moves)
        result['cube'] = myCube._get()
    
    result['status'] = 'ok'
    
    return result

def _bottomFlower(myCube):  
    moves = ''
    
    bottomFaceColor = myCube._content[5][1][1]
    
    flowerPiecesOnFace = True
    noFlowerPiecesOnFace = 0
    face = 0 
    solved = False
    
    while(solved == False):
        while(flowerPiecesOnFace == True):
            if(myCube._content[0][1][0] == bottomFaceColor): #piece left of the middle piece
                leftFlower = myCube._content[4][1][0]
                while(leftFlower == bottomFaceColor):
                    myCube._content = _movecontroller(myCube, 'U')
                    leftFlower = myCube._content[4][1][0]
                myCube._content = _movecontroller(myCube, 'l') #if leftflowwer != middle piece
                
            
            if(myCube._content[0][1][2] == bottomFaceColor): #piece right of the middle piece
                rightFlower = myCube._content[4][1][2]
                while(rightFlower == bottomFaceColor):
                    myCube._content = _movecontroller(myCube, 'U')
                    rightFlower = myCube._content[4][1][2]  
                myCube._content = _movecontroller(myCube, 'R') #if right flower != middle piece
                
            if(myCube._content[0][2][1] == bottomFaceColor): #piece under the middle piece
                bottomFlower = myCube._content[4][2][1]
                while(bottomFlower == bottomFaceColor):
                    myCube._content = _movecontroller(myCube, 'U')
                    bottomFlower = myCube._content[4][2][1]  
                myCube._content = _movecontroller(myCube, 'FUl') #if bottomflower != middle piece
                
            if(myCube._content[0][0][1] == bottomFaceColor):    
                bottomFlower = myCube._content[4][2][1]
                while(bottomFlower == bottomFaceColor):
                    myCube._content = _movecontroller(myCube, 'U')
                    bottomFlower = myCube._content[4][2][1]  
                myCube._content = _movecontroller(myCube, 'fUl')
                
            if(myCube._content[5][0][1] == bottomFaceColor): #Bring flower pieces that are on bottom layer to top layer
                bottomFlower = myCube._content[4][2][1]
                while(bottomFlower == bottomFaceColor):
                    myCube._content = _movecontroller(myCube, 'U')
                    bottomFlower = myCube._content[4][2][1] 
                myCube._content = _movecontroller(myCube, 'FF') 
                
            if(myCube._content[0][0][1] != bottomFaceColor): 
                if(myCube._content[0][1][0] != bottomFaceColor):
                    if(myCube._content[0][1][2] != bottomFaceColor): 
                        if(myCube._content[0][2][1] != bottomFaceColor):
                            if(myCube._content[5][0][1] != bottomFaceColor):
                                flowerPiecesOnFace = False
        
        if(myCube._content[4][0][1] == bottomFaceColor): 
            if(myCube._content[4][1][0] == bottomFaceColor):
                if(myCube._content[4][1][2] == bottomFaceColor): 
                    if(myCube._content[4][2][1] == bottomFaceColor): 
                        solved = True
        else:
            myCube._content = _rotateCubeClockwise(myCube)
            flowerPiecesOnFace = True
    
    matching = False
    for face in range(0,4):
        while(matching == False):
            if(face == 0):
                if(myCube._content[face][0][1] == myCube._content[face][1][1] and myCube._content[4][2][1] == bottomFaceColor):
                    myCube._content = _movecontroller(myCube, 'FF')
                    matching = True
                else:
                    myCube._content = _movecontroller(myCube, 'U')
            elif(face == 1):
                if(myCube._content[face][0][1] == myCube._content[face][1][1] and myCube._content[4][1][2] == bottomFaceColor):
                    myCube._content = _movecontroller(myCube, 'RR')
                    matching = True
                else:
                    myCube._content = _movecontroller(myCube, 'U')
            elif(face == 2):
                if(myCube._content[face][0][1] == myCube._content[face][1][1] and myCube._content[4][0][1] == bottomFaceColor):
                    myCube._content = _movecontroller(myCube, 'BB')
                    matching = True
                else:
                    myCube._content = _movecontroller(myCube, 'U')
            elif(face == 3):
                if(myCube._content[face][0][1] == myCube._content[face][1][1] and myCube._content[4][1][0] == bottomFaceColor):
                    myCube._content = _movecontroller(myCube, 'LL')
                    matching = True
                else:
                    myCube._content = _movecontroller(myCube, 'U')
            
       
            

    
     #Rotate flower to bottom layer after matching middle pieces
     
     
                
            
                
                
        
    #Add pieces to the top face flower for all faces except the bottom face
    # while(solved == False):  
    #     while(flowerPiecesOnFace == True):
    #         if(face != 0):
    #             myCube._content = _rotateCubeClockwise(myCube)
    #
    #         leftFlower = myCube._content[4][1][0] 
    #
    #         if(myCube._content[0][1][0] == bottomFaceColor):
    #             while(leftFlower == bottomFaceColor):
    #                 myCube._content = _movecontroller(myCube, 'U')
    #                 leftFlower = myCube._content[4][1][0]
    #                 moves += 'U'
    #             myCube._content = _movecontroller(myCube, 'l')
    #             moves += 'l'
    #
    #         rightFlower = myCube._content[4][1][2]
    #
    #         if(myCube._content[0][1][2] == bottomFaceColor):
    #             while(rightFlower == bottomFaceColor):
    #                 myCube._content = _movecontroller(myCube, 'U')
    #                 rightFlower = myCube._content[4][1][2]
    #                 moves += 'U'
    #             myCube._content = _movecontroller(myCube, 'R')
    #             moves += 'R'
    #
    #         bottomFlower = myCube._content[4][2][1] 
    #
    #         if(myCube._content[0][2][1] == bottomFaceColor):
    #             while(bottomFlower == bottomFaceColor):
    #                 myCube._content = _movecontroller(myCube, 'U')
    #                 bottomFlower = myCube._content[4][2][1] 
    #                 moves += 'U'
    #             myCube._content = _movecontroller(myCube, 'FUl')
    #             moves += 'FUl'
    #
    #         rightFlower = myCube._content[4][1][2]
    #
    #         if(myCube._content[0][0][1] == bottomFaceColor):
    #             myCube._content = _movecontroller(myCube, 'F')
    #             moves += 'F'
    #             while(rightFlower == bottomFaceColor):
    #                 myCube._content = _movecontroller(myCube, 'U')
    #                 rightFlower = myCube._content[4][1][2]
    #                 moves += 'U'
    #             myCube._content = _movecontroller(myCube, 'R')
    #             moves += 'R'
    #
    #
    #         topFrontFaceEdge = myCube._content[0][0][1]
    #         bottomFrontFaceEdge = myCube._content[0][2][1]
    #         leftFrontFaceEdge = myCube._content[0][1][0]
    #         rightFrontFaceEdge = myCube._content[0][1][2]
    #
    #         if(topFrontFaceEdge != bottomFaceColor):
    #             if(bottomFrontFaceEdge != bottomFaceColor): 
    #                 if(leftFrontFaceEdge != bottomFaceColor):
    #                     if(rightFrontFaceEdge != bottomFaceColor):
    #                         flowerPiecesOnFace = False
    #
    #
    #     face = (face + 1) % 4   
    #     noFlowerPiecesOnFace += 1          
    #     if(noFlowerPiecesOnFace == 7):
    #         solved = True                                 
    #
    #
    #
    # leftFlower = myCube._content[4][1][0]    
    #
    # #Add pieces on the bottom face to the top flower
    # if(myCube._content[5][1][0] == bottomFaceColor and myCube._content[3][2][1] != myCube._content[3][1][1]):
    #     while(leftFlower == bottomFaceColor):
    #         myCube._content = _movecontroller(myCube, 'U')
    #         moves += 'U'
    #         leftFlower = myCube._content[4][1][0]
    #     myCube._content = _movecontroller(myCube, 'LL')
    #     moves += 'LL'
    #
    #
    # rightFlower = myCube._content[4][1][2]
    #
    # if(myCube._content[5][1][2] == bottomFaceColor and myCube._content[1][2][1] != myCube._content[1][1][1]):
    #     while(rightFlower == bottomFaceColor):
    #         myCube._content = _movecontroller(myCube, 'U')
    #         moves += 'U'
    #         rightFlower = myCube._content[4][1][2]
    #     myCube._content = _movecontroller(myCube, 'RR')
    #     moves += 'RR'
    #
    #
    # topFlower = myCube._content[4][0][1]
    # if(myCube._content[5][2][1] == bottomFaceColor and myCube._content[2][2][1] != myCube._content[2][1][1]):
    #     while(topFlower == bottomFaceColor):
    #         myCube._content = _movecontroller(myCube, 'U')
    #         moves += 'U'
    #     myCube._content = _movecontroller(myCube, 'BB')
    #     moves += 'BB'
    #
    # bottomFlower = myCube._content[4][2][1] 
    #
    # if(myCube._content[5][0][1] == bottomFaceColor and myCube._content[0][2][1] != myCube._content[0][1][1]):
    #     while(bottomFlower == bottomFaceColor):
    #         myCube._content = _movecontroller(myCube, 'U')
    #         moves += 'U'
    #     myCube._content = _movecontroller(myCube, 'FF')
    #     moves += 'FF'
    # else: #Bottom cross is already solved
    #     return moves   
    #
    #
    # #Rotate flower pieces to bottom face to form bottom cross
    # for face in range(0,6):
    #     middleColor = myCube._content[face][1][1]
    #     while(myCube._content[face][0][1] != middleColor):
    #         myCube._content = _movecontroller(myCube, 'U')
    #         moves += 'U'
    #     myCube._content = _movecontroller(myCube, 'FF')
    #     moves += 'FF'
    
    return moves

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
    
def _movecontroller(myCube, moves=None, ):
    content = myCube._content
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

def _rotateMiddle(content):
    for face in range(0,4):
        if(face == 0):
            temp = content[face][1]
        if(face == 3):
            content[face][1] = temp
        else:
            content[face][1] = content[face+1][1]
        
    return content

def _rotateCubeClockwise(myCube):
    content = _movecontroller(myCube, 'UMd')
    return content 
# dev strategy
#    validate parms
#    loads parms['cube'] into cube model
#    rotate cube in desired direction
#    serialize the cube model into a string
#    return the string + status of 'ok'
