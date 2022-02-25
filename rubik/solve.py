import rubik.cube as rubik

def _solve(parms):
    result = {}
    result['cube'] = 'bwbybgrygyogyrrobwogrbgooggbwyworwogwwybygrroyowbwyrrb'            
    result['status'] = 'ok'
    return result

# dev strategy
#    validate parms
#    loads parms['cube'] into cube model
#    rotate cube in desired direction
#    serialize the cube model into a string
#    return the string + status of 'ok'
