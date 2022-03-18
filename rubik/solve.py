import rubik.cube as cube
import rubik.check as check
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
    
    # bottomFaceColor = myCube._content[5][1][1]
    #
    #
    # #Add pieces to the top face flower for all faces except the bottom face
    # for face in range(5):    
    #     leftFlower = myCube._content[4][1][0]
    #     rightFlower = myCube._content[4][1][2]
    #     bottomFlower = myCube._content[4][2][1] 
    #     if(myCube._content[face][1][0] == bottomFaceColor):
    #         while(leftFlower == bottomFaceColor):
    #             myCube._content = _movecontroller(myCube, 'U')
    #             moves += 'U'
    #         myCube._content = _movecontroller(myCube, 'l')
    #         moves += 'l'
    #     if(myCube._content[face][1][2] == bottomFaceColor):
    #         while(rightFlower == bottomFaceColor):
    #             myCube._content = _movecontroller(myCube, 'U')
    #             moves += 'U'
    #         myCube._content = _movecontroller(myCube, 'R')
    #         moves += 'R'
    #     if(myCube._content[face][2][1] == bottomFaceColor):
    #         while(bottomFlower == bottomFaceColor):
    #             myCube._content = _movecontroller(myCube, 'U')
    #             moves += 'U'
    #         myCube._content = _movecontroller(myCube, 'FUl')
    #         moves += 'FUl'
    #     if(myCube._content[face][0][1] == bottomFaceColor):
    #         myCube._content = _movecontroller(myCube, 'F')
    #         moves += 'F'
    #         while(rightFlower == bottomFaceColor):
    #             myCube._content = _movecontroller(myCube, 'U')
    #             moves += 'U'
    #         myCube._content = _movecontroller(myCube, 'R')
    #         moves += 'R'
        
    #
    #
    # topFlower = myCube._content[4][0][1]
    # leftFlower = myCube._content[4][1][0]
    # rightFlower = myCube._content[4][1][2]
    # bottomFlower = myCube._content[4][2][1] 
    #
    #
    # #Add pieces on the bottom face to the top flower
    # if(myCube._content[5][1][0] == bottomFaceColor and myCube._content[3][2][1] != myCube._content[3][1][1]):
    #     while(leftFlower == bottomFaceColor):
    #         myCube._content = _movecontroller(myCube, 'U')
    #         moves += 'U'
    #     myCube._content = _movecontroller(myCube, 'LL')
    #     moves += 'LL'
    #
    # if(myCube._content[5][1][2] == bottomFaceColor and myCube._content[1][2][1] != myCube._content[1][1][1]):
    #     while(rightFlower == bottomFaceColor):
    #         myCube._content = _movecontroller(myCube, 'U')
    #         moves += 'U'
    #     myCube._content = _movecontroller(myCube, 'RR')
    #     moves += 'RR'
    #
    # if(myCube._content[5][2][1] == bottomFaceColor and myCube._content[2][2][1] != myCube._content[2][1][1]):
    #     while(topFlower == bottomFaceColor):
    #         myCube._content = _movecontroller(myCube, 'U')
    #         moves += 'U'
    #     myCube._content = _movecontroller(myCube, 'BB')
    #     moves += 'BB'
    #
    # if(myCube._content[5][0][1] == bottomFaceColor and myCube._content[0][2][1] != myCube._content[0][1][1]):
    #     while(bottomFlower == bottomFaceColor):
    #         myCube._content = _movecontroller(myCube, 'U')
    #         moves += 'U'
    #     myCube._content = _movecontroller(myCube, 'FF')
    #     moves += 'FF'
    # else: #Bottom cross is already solved
    #     content = myCube._content
    #     return content   
    #
    #
    # #Rotate flower pieces to bottom face to form bottom cross
    # for face in range(0,6):
    #     middleColor = content[face][1][1]
    #     while(content[face][0][1] != middleColor):
    #         myCube._content = _movecontroller(myCube, 'U')
    #         moves += 'U'
    #     myCube._content = _movecontroller(myCube, 'FF')
    #     moves += 'FF'
    #
    # content = myCube._content
    return moves

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
# dev strategy
#    validate parms
#    loads parms['cube'] into cube model
#    rotate cube in desired direction
#    serialize the cube model into a string
#    return the string + status of 'ok'
