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
    facecount = 0
    for move in moves:
        if move == 'F':
            facecount = 0
            _clockwise(content[facecount])
            movelist += '0'
        elif move == 'f':
            facecount = 0
            _counterclockwise(content[facecount])
            movelist += '0'
        elif move == 'R':
            facecount = 1
            _clockwise(content[facecount])
            movelist += '1'
        elif move == 'r':
            facecount = 1
            _counterclockwise(content[facecount])
            movelist += '1'
        elif move == 'B':
            facecount = 2
            _clockwise(facecount)
            movelist += '2'
        elif move == 'b':
            facecount = 2
            _counterclockwise(content[facecount])
            movelist += '2'
        elif move == 'L':
            facecount = 3
            _clockwise(content[facecount])
            movelist += '3'
        elif move == 'l':
            facecount = 3
            _counterclockwise(content[facecount])
            movelist += '3'
        elif move == 'U':
            facecount = 4
            _clockwise(content[facecount])
            movelist += '4'
        elif move == 'u':
            facecount = 4
            _counterclockwise(content[facecount])
            movelist += '4'
        elif move == 'D':
            facecount = 5
            _clockwise(content[facecount])
            movelist += '5'
        elif move == 'd':
            facecount = 5
            _counterclockwise(content[facecount])
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
