import rubik.cube as rubik
from curses.ascii import isalnum

def _check(parms):
    result={}
    encodedCube = parms.get('cube',None)
    
    result['status'] = 'ok'
    
    if(encodedCube == None):
        result['status'] = 'error: 100 No cube input'
        return result
    
    if(len(encodedCube) < 54):
        result['status'] = 'error: 102 Cube length is less than 54'
        return result
    elif len(encodedCube) > 54:
        result['status'] = 'error: 102 Cube length is greater than 54'
        return result
        
    if encodedCube.isalnum() == False:
        result['status'] = 'error: 106 Non-alphanumeric character used in cube'
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
        result['status'] = 'error: 104 Invalid amount of colors'
        return result
                
    # Check if any elementColor has more or less then 9
    for elementColor in colors:
        if colors[elementColor] != 9:
            result['status'] = 'error: 105 Each color must have 9 occurrences'
            return result
        
    # Check if there are middle colors that are the same
    if len(midColors) != 6:
        result['status'] = 'error: 103 Some middle pieces have the same color'
        return result
    
    validRotations = 'FfBbRrLlUuDd'
    for action in parms.get('rotate'):
        if action not in validRotations:
            result['status'] = 'error 101: Invalid rotation'
    
    return result