'''
Created on Apr 4, 2022

@author: cheyennea.
'''
import unittest
import rubik.cube as cube
import rubik.solve as solve

import rubik.solveBottomCross as bottomCross

class SolveBottomLayerTest(unittest.TestCase):
    def test_solve_130_ShouldReturnEmptySolutionForUnmixedValidCube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        
    
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedResult = ''
        actualResult = bottomCross._solveBottomCross(content)
        #actualResult = solve._bottomcross(myCube)
        
        self.assertEqual(expectedResult, actualResult)
    
    
    def test_solve_131_ShouldSolveBottomCrossForMixedValidCubeMissingRotation(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'brborgyboywgrggwowoogyowbywrwybbyoorwbyrygrbogygwwgbrr'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        bottomFaceColor = content[5][1][1]
        moves = bottomCross._solveBottomCross(content)
        
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        contentCopy = myCube2._getContent()
    
        actualContent = solve._movecontroller(contentCopy, moves)
      
        self.assertEqual(actualContent[5][1][1], bottomFaceColor)
        self.assertEqual(actualContent[5][0][1], bottomFaceColor)
        self.assertEqual(actualContent[5][1][0], bottomFaceColor)
        self.assertEqual(actualContent[5][1][2], bottomFaceColor)
        self.assertEqual(actualContent[5][2][1], bottomFaceColor)
        self.assertEqual(actualContent[0][1][1], actualContent[0][2][1])
        self.assertEqual(actualContent[1][1][1], actualContent[1][2][1])
        self.assertEqual(actualContent[2][1][1], actualContent[2][2][1])
        self.assertEqual(actualContent[3][1][1], actualContent[3][2][1])
     
    
    def test_solve_132_ShouldSolveBottomCrossForMixedValidCubeEmptyRotation(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'oowrboyyrowobygwrbywgygroywygbgwyrrbrbgoogwwgrobwrbgby'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        
        contentCopy = myCube2._getContent()
        bottomFaceColor = content[5][1][1]
        moves = bottomCross._solveBottomCross(content)
        
        actualContent = solve._movecontroller(contentCopy, moves)
      
        self.assertEqual(actualContent[5][1][1], bottomFaceColor)
        self.assertEqual(actualContent[5][0][1], bottomFaceColor)
        self.assertEqual(actualContent[5][1][0], bottomFaceColor)
        self.assertEqual(actualContent[5][1][2], bottomFaceColor)
        self.assertEqual(actualContent[5][2][1], bottomFaceColor)
        self.assertEqual(actualContent[0][1][1], actualContent[0][2][1])
        self.assertEqual(actualContent[1][1][1], actualContent[1][2][1])
        self.assertEqual(actualContent[2][1][1], actualContent[2][2][1])
        self.assertEqual(actualContent[3][1][1], actualContent[3][2][1])
    
    
    def test_solve_133_ShouldSolveBottomCrossForPartiallySolvedCrossValidCube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ggrrgwbooyroboowobwrrybgroywyyrrbgbygwbgyyowboggywwrbw'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        
        contentCopy = myCube2._getContent()
        bottomFaceColor = content[5][1][1]
        moves = bottomCross._solveBottomCross(content)
        
        actualContent = solve._movecontroller(contentCopy, moves)
      
        self.assertEqual(actualContent[5][1][1], bottomFaceColor)
        self.assertEqual(actualContent[5][0][1], bottomFaceColor)
        self.assertEqual(actualContent[5][1][0], bottomFaceColor)
        self.assertEqual(actualContent[5][1][2], bottomFaceColor)
        self.assertEqual(actualContent[5][2][1], bottomFaceColor)
        self.assertEqual(actualContent[0][1][1], actualContent[0][2][1])
        self.assertEqual(actualContent[1][1][1], actualContent[1][2][1])
        self.assertEqual(actualContent[2][1][1], actualContent[2][2][1])
        self.assertEqual(actualContent[3][1][1], actualContent[3][2][1])

    
    

    
    def test_170_formBottomCross_ShouldFormBottomCrossGivenCubeHasTopFlower(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'wrwrbboyygbborobbrrggygrwygooogoyrggywywywbwrwgoowrybb'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        bottomFaceColor = inputDict['cube'][49]
        
        moves = bottomCross._formBottomCross(content)
        inputDict['rotate'] = moves
        actualResult = solve._solve(inputDict)
        
    
        solve._solve(inputDict)
        
        self.assertEqual(actualResult['cube'][46], bottomFaceColor)
        self.assertEqual(actualResult['cube'][7], actualResult['cube'][4])
        self.assertEqual(actualResult['cube'][48], bottomFaceColor)
        self.assertEqual(actualResult['cube'][34], actualResult['cube'][31])
        self.assertEqual(actualResult['cube'][50], bottomFaceColor)
        self.assertEqual(actualResult['cube'][16], actualResult['cube'][13])
        self.assertEqual(actualResult['cube'][52], bottomFaceColor)
        self.assertEqual(actualResult['cube'][25], actualResult['cube'][22])
    
    
    def test_formBottomCross_171_ShouldDoNothingBecuaseCrossAlreadySolved(self):
        myCube = cube.Cube()
        myCube._load('rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww')
        content = myCube._getContent()
        expectedMoves = ''
        moves = bottomCross._formBottomCross(content)
        actualMoves = moves
        self.assertEqual(expectedMoves, actualMoves)
    
    
    def test_solvedFlower_180_ShouldReturnTrueIfTopLayerHasFlower(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gboyoooogwygybrwbrorwgrobyyogobgrbggbwywygywbwwrowroby'
        expectedResult = True
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        actualResult = bottomCross._solvedFlower(content)
        self.assertEqual(expectedResult, actualResult)
        
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        expectedResult = True
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        content2 = myCube2._getContent()
        actualResult = bottomCross._solvedFlower(content2)
        self.assertEqual(expectedResult, actualResult)
    
    def test_solvedFlower_181_ShouldReturnFalseBecauseTopFlowerNotSolved(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'wyyrrbgbyggrrgybowbowooboryorrwbgroygwwwywggoryobwgbyb'
        expectedResult = False
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        actualResult = bottomCross._solvedFlower(content)
        self.assertEqual(expectedResult, actualResult)
        

