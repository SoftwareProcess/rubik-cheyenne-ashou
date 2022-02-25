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

def _movecontroller():
    pass

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
