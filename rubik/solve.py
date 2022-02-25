import rubik.cube as cube

def _solve(parms):
    content = parms['cube']
    result = {}
    if len(content) != 54:
        result['status'] = 'error xxx' 
    result['cube'] = None       
    if len(parms.get('cube')):
        pass
    result['status'] = 'ok'
    return result

def _movecontroller(content, moves):
    movelist = ''
    face = 0
    for move in moves:
        if move == 'F':
            face = 0
            _clockwise(content[face])
            movelist += '0'
        elif move == 'f':
            face = 0
            _counterclockwise(content[face])
            movelist += '0'
        elif move == 'R':
            face = 1
            _clockwise(content[face])
            movelist += '1'
        elif move == 'r':
            face = 1
            _counterclockwise(content[face])
            movelist += '1'
        elif move == 'B':
            face = 2
            _clockwise(face)
            movelist += '2'
        elif move == 'b':
            face = 2
            _counterclockwise(content[face])
            movelist += '2'
        elif move == 'L':
            face = 3
            _clockwise(content[face])
            movelist += '3'
        elif move == 'l':
            face = 3
            _counterclockwise(content[face])
            movelist += '3'
        elif move == 'U':
            face = 4
            _clockwise(content[face])
            movelist += '4'
        elif move == 'u':
            face = 4
            _counterclockwise(content[face])
            movelist += '4'
        elif move == 'D':
            face = 5
            _clockwise(content[face])
            movelist += '5'
        elif move == 'd':
            face = 5
            _counterclockwise(content[face])
            movelist += '5'
    return movelist
        

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
# dev strategy
#    validate parms
#    loads parms['cube'] into cube model
#    rotate cube in desired direction
#    serialize the cube model into a string
#    return the string + status of 'ok'
