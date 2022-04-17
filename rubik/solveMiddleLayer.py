'''
Created on Apr 17, 2022

@author: cheyennea.
'''

def _checkSolved(content):
    solved = True
    sideFaces = 4
    for face in range(sideFaces):
        middlePiece = content[face][1][1]
        leftPiece = content[face][1][0]
        rightPiece = content[face][1][2]
        if(leftPiece != middlePiece or rightPiece != middlePiece):
            solved = False
            exit
    return solved
