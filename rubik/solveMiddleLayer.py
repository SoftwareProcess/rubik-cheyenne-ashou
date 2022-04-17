'''
Created on Apr 17, 2022

@author: cheyennea.
'''
import rubik.check as check

def _checkSolved(content):
    solved = True
    bottomSolved = check.checkBottomLayerSolved(content)
    middleSolved = check.checkMiddleLayerSolved(content)
    
    if(bottomSolved == False or middleSolved == False):
        solved = False
    
    return solved

def _checkLeftEdgePlaced(content):
    placed = True
    frontFaceEdgeColor = content[0][1][0]
    leftFaceEdgeColor = content[3][1][2]
    frontFaceColor = content[0][1][1]
    leftFaceColor = content[3][1][1]
    
    if(frontFaceEdgeColor != frontFaceColor or leftFaceEdgeColor != leftFaceColor):
        placed = False
    return placed