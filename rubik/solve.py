import rubik.cube as rubik

def _solve(parms):
    result = {}
    encodedCube = parms.get('cube',None)       #get "cube" parameter if present
    result['solution'] = 'FfRrBbLlUuDd'        #example rotations
    result['status'] = 'ok'                     
    return result

# dev strategy
#    validate parms
#    loads parms['cube'] into cube model
#    rotate cube in desired direction
#    serialize the cube model into a string
#    return the string + status of 'ok'
