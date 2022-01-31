import rubik.cube as rubik
from curses.ascii import isalnum

def _check(parms):
    result={}
    encodedCube = parms.get('cube',None)

    if(encodedCube == None):
        result['status'] = 'error: No value for "cube"\n'
        return result
    else:
        result['status'] = 'ok'
    
    if(len(encodedCube) < 54):
        result['status'] = 'error: Length for "cube" is too small\nThere must be 54 elements.'
        return result
    elif len(encodedCube) > 54:
        result['status'] = 'error: Length for "cube" is too big\nThere must be 54 elements.'
        return result
        
    if encodedCube.isalnum() == False:
        result['status'] = 'error: Non-alphanumber character used in the value for "cube"'
        return result
    
    colors = {}
    midColors = {}
    index = 0;
    # Count occurrences of each color
    for elementColor in encodedCube:
        if(index == 4 or (index > 4 and (index - 4) % 9 == 0)):
            if(elementColor in midColors):
                midColors[elementColor] += 1
            else: midColors[elementColor] = 0
        if(elementColor in colors):
            colors[elementColor] += 1
        else:
            colors[elementColor] = 1
        index += 1
    if len(colors) != 6:
        result['status'] = 'error: There must be 6 colors'
        return result
                
    # Check if any elementColor has more or less then 9
    for elementColor in colors:
        if colors[elementColor] != 9:
            result['status'] = 'error: Each color must have 9 occurrences'
            return result
        
    # Check if there are middle colors that are the same
    if len(midColors) != 6:
        result['status'] = 'error: 2 or more middle pieces have the same color'
        return result
    
    return result