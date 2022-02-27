import rubik.cube as cube

def _solve(parms):
    content = parms['cube']
    result = {}
    if len(content) != 54:
        result['status'] = 'error xxx' 
        return result
    
    myCube = cube.Cube()
    content = myCube._load(content)
    moves = parms['rotate']
    
    
    if len(parms.get('cube')):
        pass
    result['cube'] = _movecontroller(content, moves)
    result['status'] = 'ok'
    return result


def _movecontroller(content, moves):
    movelist = ''
    face = 0
    for move in moves:
        if move == 'F':
            face = 0
            content[face] = _clockwise(content[face])
            content = _switchedge(content, move)
            movelist += '0'
        elif move == 'f':
            face = 0
            content[face] = _counterclockwise(content[face])
            content = _switchedge(content, move)
            movelist += '0'
        elif move == 'R':
            face = 1
            content[face] = _clockwise(content[face])
            content = _switchedge(content, move)
            movelist += '1'
        elif move == 'r':
            face = 1
            content[face] = _counterclockwise(content[face])
            content = _switchedge(content, move)
            movelist += '1'
        elif move == 'B':
            face = 2
            content[face] = _clockwise(content[face])
            content = _switchedge(content, move)
            movelist += '2'
        elif move == 'b':
            face = 2
            content[face] = _counterclockwise(content[face])
            content = _switchedge(content, move)
            movelist += '2'
        elif move == 'L':
            face = 3
            content[face] = _clockwise(content[face])
            content = _switchedge(content, move)
            movelist += '3'
        elif move == 'l':
            face = 3
            content[face] = _counterclockwise(content[face])
            content = _switchedge(content, move)
            movelist += '3'
        elif move == 'U':
            face = 4
            content[face] = _clockwise(content[face])
            content = _switchedge(content, move)
            movelist += '4'
        elif move == 'u':
            face = 4
            content[face] = _counterclockwise(content[face])
            content = _switchedge(content, move)
            movelist += '4'
        elif move == 'D':
            face = 5
            content[face] = _clockwise(content[face])
            content = _switchedge(content, move)
            movelist += '5'
        elif move == 'd':
            face = 5
            content[face] = _counterclockwise(content[face])
            content = _switchedge(content, move)
            movelist += '5'
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
    if (action == 'F'):
        temp = cube[4][2]
        cube[4][2] = [cube[3][2][2], cube[3][1][2], cube[3][0][2]]
        
        cube[3][0][2] = cube[5][0][0]
        cube[3][1][2] = cube[5][0][1]
        cube[3][2][2] = cube[5][0][2]      
        
        cube[5][0] = [cube[1][2][0], cube[1][1][0], cube[1][0][0]]
        
        cube[1][0][0] = temp[0]
        cube[1][1][0] = temp[1]
        cube[1][2][0] = temp[2]
    elif(action == 'R'):
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
    elif(action == 'L'):
        temp = [cube[0][0][0], cube[0][1][0], cube[0][2][0]]
        
        cube[0][0][0] = cube[5][0][0]
        cube[0][1][0] = cube[5][1][0]
        cube[0][2][0] = cube[5][2][0]
        
        cube[5][0][0] = cube[2][2][2]
        cube[5][1][0] = cube[2][1][2]
        cube[5][2][0] = cube[2][0][2]
        
        cube[2][0][2] = cube[4][2][0]
        cube[2][1][2] = cube[4][1][0]
        cube[2][2][2] = cube[4][0][0]
        
        cube[4][0][0] = temp[0]
        cube[4][1][0] = temp[1]
        cube[4][2][0] = temp[2]
    elif(action == 'B'):
        temp = cube[4][0]
        cube[4][0] = [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
        
        cube[1][0][2] = cube[5][2][2]
        cube[1][1][2] = cube[5][2][1]
        cube[1][2][2] = cube[5][2][0]      
        
        cube[5][2] = [cube[3][0][0], cube[3][1][0], cube[3][2][0]]
        
        cube[3][0][0] = temp[2]
        cube[3][1][0] = temp[1]
        cube[3][2][0] = temp[0]
    elif(action == 'U'):
        temp = cube[0][0]
        cube[0][0] = cube[1][0]
        cube[1][0] = cube[2][0]
        cube[2][0] = cube[3][0]
        cube[3][0] = temp
    elif(action == 'D'):
        temp = cube[0][2]
        cube[0][2] = cube[3][2]
        cube[3][2] = cube[2][2]
        cube[2][2] = cube[1][2]
        cube[1][2] = temp
    return cube
# dev strategy
#    validate parms
#    loads parms['cube'] into cube model
#    rotate cube in desired direction
#    serialize the cube model into a string
#    return the string + status of 'ok'
