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

def _movecontroller(moves):
    movelist = ''
    face = 0
    for move in moves:
        if move == 'F':
            _clockwise(face)
            face = 0
            movelist += '0'
        elif move == 'f':
            face = 0
            _counterclockwise(face)
            movelist += '0'
        elif move == 'R':
            face = 1
            _clockwise(face)
            movelist += '1'
        elif move == 'r':
            face = 1
            _counterclockwise(face)
            movelist += '1'
        elif move == 'B':
            face = 2
            _clockwise(face)
            movelist += '2'
        elif move == 'b':
            face = 2
            _counterclockwise(face)
            movelist += '2'
        elif move == 'L':
            face = 3
            _clockwise(face)
            movelist += '3'
        elif move == 'l':
            face = 3
            _counterclockwise(face)
            movelist += '3'
        elif move == 'U':
            face = 4
            _clockwise(face)
            movelist += '4'
        elif move == 'u':
            face = 4
            _counterclockwise(face)
            movelist += '4'
        elif move == 'D':
            face = 5
            _clockwise(face)
            movelist += '5'
        elif move == 'd':
            face = 5
            _counterclockwise(face)
            movelist += '5'
        return movelist
        

def _clockwise(face):
    pass

def _counterclockwise(face):
    pass
# dev strategy
#    validate parms
#    loads parms['cube'] into cube model
#    rotate cube in desired direction
#    serialize the cube model into a string
#    return the string + status of 'ok'
