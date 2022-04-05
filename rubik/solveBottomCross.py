'''
Created on Apr 4, 2022

@author: cheyennea.
'''
import rubik.solve as solve
#Rotate the cube to get a 'flower' at the top face
def _solveBottomCross(content):  
    moves = ''

    flowerPiecesOnFace = True
    face = 0 
    flowerSolved = False
    
    while(flowerSolved == False):
        while(flowerPiecesOnFace == True):
            moves = _solveTopFlower(content, face, moves)
            
            flowerPiecesOnFace = _checkFlowerPieces(content)    

        flowerSolved = _solvedFlower(content)
        
        if(flowerSolved == False):
            content = solve._rotateCubeClockwise(content)
            flowerPiecesOnFace = True
            face = (face + 1) % 4
            
    content = solve._rotateToFrontFace(content, face)
    
    moves += _formBottomCross(content)
    
    return moves

def _solveTopFlower(content, face, moves):
    leftFrontLayer = content[0][1][0] 
    move = _placePieceIntoFlower(content, leftFrontLayer, 'l')
    moves += solve._movetranslator(face, move)          
    
    rightFrontLayer = content[0][1][2]
    move = _placePieceIntoFlower(content, rightFrontLayer, 'R')
    moves += solve._movetranslator(face, move)          
    
    bottomFrontLayer = content[0][2][1]
    move = _placePieceIntoFlower(content, bottomFrontLayer, 'FUl')
    moves += solve._movetranslator(face, move)          
    
    topFrontLayer = content[0][0][1]
    move = _placePieceIntoFlower(content, topFrontLayer, 'fUl')
    moves += solve._movetranslator(face, move)          
    

    move = _rotateFlowerPiece180ToTopFace(content, 'FF')
    moves += solve._movetranslator(face, move)
    return moves

def _placePieceIntoFlower(content, frontLayerPiece, move):
    bottomFaceColor = content[5][1][1]
    moves = ''
    if(frontLayerPiece == bottomFaceColor):
        leftFlower = content[4][1][0]
        while(leftFlower == bottomFaceColor):
            content = solve._movecontroller(content, 'U')
            leftFlower = content[4][1][0]
            moves += 'U'
        content = solve._movecontroller(content, move) 
        moves += move
    return moves

def _rotateFlowerPiece180ToTopFace(content, move):
    moves = ''
    topBottomLayer = content[5][0][1]    
    middleFrontLayer = content[0][1][1]
    bottomFaceColor = content[5][1][1]
    bottomFrontLayer = content[0][2][1]
    if(topBottomLayer == bottomFaceColor and bottomFrontLayer != middleFrontLayer): #Bring flower pieces that are on bottom layer to top layer
        bottomFlower = content[4][2][1]
        while(bottomFlower == bottomFaceColor):
            content = solve._movecontroller(content, 'U')
            bottomFlower = content[4][2][1] 
            moves += 'U'
        content = solve._movecontroller(content, move) 
        moves += move
    return moves
#Checks if more moves are required on the current face
def _checkFlowerPieces(content):
    bottomFaceColor = content[5][1][1]
    flowerPiecesOnFace = True
    if(content[0][0][1] != bottomFaceColor): 
        if(content[0][1][0] != bottomFaceColor):
            if(content[0][1][2] != bottomFaceColor): 
                if(content[0][2][1] != bottomFaceColor):
                    if(content[5][0][1] != bottomFaceColor or 
                       (content[5][0][1] == bottomFaceColor and 
                        content[0][2][1] == content[0][1][1])):
                        flowerPiecesOnFace = False
    return flowerPiecesOnFace

#Forms a bottom cross after the flower has been made
def _formBottomCross(content):
    bottomFaceColor = content[5][1][1]
    matching = False
    moves = ''
    for face in range(0,4):
        matching = False
        while(matching == False):
            move = solve._movetranslator(face, 'FF')
            translatedU = solve._movetranslator(face, 'U')
            topPiece = content[face][0][1]
            middlePiece = content[face][1][1]
            bottomPiece = content[face][2][1]
            if(face == 0):
                adjacentFlowerPiece = content[4][2][1]
                adjacentCrossPiece = content[5][0][1]
                if(topPiece == middlePiece and  adjacentFlowerPiece == bottomFaceColor):
                    content = solve._movecontroller(content, move)
                    moves += move
                    matching = True
                elif(bottomPiece == middlePiece and adjacentCrossPiece == bottomFaceColor):
                    matching = True
                else:
                    content = solve._movecontroller(content, translatedU)
                    moves += translatedU
            elif(face == 1):
                adjacentFlowerPiece = content[4][1][2]
                adjacentCrossPiece = content[5][1][2]
                if(topPiece == middlePiece and adjacentFlowerPiece == bottomFaceColor):
                    content = solve._movecontroller(content, move)
                    moves += move
                    matching = True
                elif(bottomPiece == middlePiece and adjacentCrossPiece == bottomFaceColor):
                    matching = True
                else:
                    content = solve._movecontroller(content, translatedU)
                    moves += translatedU
            elif(face == 2):
                adjacentFlowerPiece = content[4][0][1]
                adjacentCrossPiece = content[5][2][1]
                if(topPiece == middlePiece and adjacentFlowerPiece == bottomFaceColor):
                    content = solve._movecontroller(content, move)
                    moves += move
                    matching = True
                elif(bottomPiece == middlePiece and adjacentCrossPiece == bottomFaceColor):
                    matching = True
                else:
                    content = solve._movecontroller(content, translatedU)
                    moves += translatedU
            elif(face == 3):
                adjacentFlowerPiece = content[4][1][0]
                adjacentCrossPiece = content[5][1][0]
                if(topPiece == middlePiece and adjacentFlowerPiece == bottomFaceColor):
                    content = solve._movecontroller(content, move)
                    moves += move
                    matching = True
                elif(bottomPiece == middlePiece and adjacentCrossPiece == bottomFaceColor):
                    matching = True
                else:
                    content = solve._movecontroller(content, translatedU)
                    moves += translatedU
    return moves

#Determines if flower is solved
def _solvedFlower(content):
    bottomFaceColor = content[5][1][1]
    flowerCount = 0
    for face in range(0,4):
        if(face == 0):
            if(content[4][2][1] == bottomFaceColor):
                flowerCount += 1
            if(content[5][0][1] == bottomFaceColor and content[face][1][1] == content[face][2][1]):
                flowerCount += 1
        if(face == 1):
            if(content[4][1][2] == bottomFaceColor):
                flowerCount += 1
            if(content[5][1][2] == bottomFaceColor and content[face][1][1] == content[face][2][1]):
                flowerCount += 1
        if(face == 2):
            if(content[4][0][1] == bottomFaceColor): 
                flowerCount += 1
            if(content[5][2][1] == bottomFaceColor and content[face][1][1] == content[face][2][1]):
                flowerCount += 1
        if(face == 3):
            if(content[4][1][0] == bottomFaceColor):
                flowerCount += 1
            if(content[5][1][0] == bottomFaceColor and content[face][1][1] == content[face][2][1]):
                flowerCount += 1
        
    if(flowerCount == 4):
        return True
    else:
        return False
    