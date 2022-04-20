'''
Created on Feb 24, 2022

@author: cheyennea.
'''
import unittest
import rubik.solve as solve
import rubik.cube as cube
import rubik.check as check
import rubik.solveMiddleLayer as middleLayer

class SolveTest(unittest.TestCase):
    def test_solve_000_ShouldSolvedBottomAndMiddleLayer(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'wogwryybgrbrggrrbbbrggooyybwrowbgowgobwyyybgwowyrwoyor'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        solveResult = solve._solve(inputDict)
        rotations = solveResult['solution']
        
        solveDict = {}
        solveDict['op'] = 'solve'
        solveDict['cube'] = inputDict['cube']
        solveDict['rotate'] = rotations
         
        myCube2 = cube.Cube()     
        resultingCubeDict = solve._solve(solveDict)
        
        myCube2._load(resultingCubeDict['cube'])
        resultingCube = myCube2._getContent()
        
        bottomLayerResult = check.checkBottomLayerSolved(resultingCube)
        middleLayerResult = check.checkMiddleLayerSolved(resultingCube)
        
        expectedResult = True
        self.assertEqual(expectedResult, bottomLayerResult)
        self.assertEqual(expectedResult, middleLayerResult)
        
    def test_solve_001_ShouldSolvedBottomAndMiddleLayer(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gbbwrbywrroywgrgggobwyoboowbgyobgboroybyyyorygrwgwrrww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        solveResult = solve._solve(inputDict)
        rotations = solveResult['solution']
        print(rotations)
        solveDict = {}
        solveDict['op'] = 'solve'
        solveDict['cube'] = inputDict['cube']
        solveDict['rotate'] = rotations
         
        myCube2 = cube.Cube()     
        resultingCubeDict = solve._solve(solveDict)
        
        myCube2._load(resultingCubeDict['cube'])
        resultingCube = myCube2._getContent()
        
        bottomLayerResult = check.checkBottomLayerSolved(resultingCube)
        middleLayerResult = check.checkMiddleLayerSolved(resultingCube)
        
        expectedResult = True
        self.assertEqual(expectedResult, bottomLayerResult)
        print(resultingCube)
        self.assertEqual(expectedResult, middleLayerResult)
        
    def test_solve_002_NominalUnmixedCubeNoMovesRequired(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        solveResult = solve._solve(inputDict)
        rotations = solveResult['solution']
        print(rotations)
        solveDict = {}
        solveDict['op'] = 'solve'
        solveDict['cube'] = inputDict['cube']
        solveDict['rotate'] = rotations
        
        expectedRotations = ''
        self.assertEqual(expectedRotations, rotations)
        
        
    def test_movecontroller_010_ShouldRotateValidNominalCubeF(self):
        inputDict = {}
        inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        inputDict['rotate'] = 'F'
        inputDict['op'] = 'solve'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        move = 'F'
        rotatedCube = 'bwbybgrygyogyrrobwogrbgooggbwyworwogwwybygrroyowbwyrrb'
        myCube2 = cube.Cube()
        myCube2._load(rotatedCube)
        expectedContent = myCube2._getContent()
        actualContent = solve._movecontroller(content, move)
        
        self.assertEqual(expectedContent, actualContent)
        
    
    #Show a test case for a string of rotations
    def test_movecontroller_011_ShouldRotateValidNominalCubeWithPrimeMoves(self):
        inputDict = {}
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = 'FfRrLlUuDdBb'
        inputDict['op'] = 'solve'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        moves = inputDict['rotate']
        rotatedCube = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        myCube2 = cube.Cube()
        myCube2._load(rotatedCube)
        expectedContent = myCube2._getContent()
        actualContent = solve._movecontroller(content, moves)
        
        self.assertEqual(expectedContent, actualContent)
        
        
   
    def test_solve_012_ShouldRotateValidNominalCubeB(self):
        inputDict = {}
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = 'B'
        inputDict['op'] = 'solve'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        moves = inputDict['rotate']
        rotatedCube = 'rrrrrrrrrggwggwggwoooooooooybbybbybbgggyyyyyywwwwwwbbb'
        myCube2 = cube.Cube()
        myCube2._load(rotatedCube)
        expectedContent = myCube2._getContent()
        actualContent = solve._movecontroller(content, moves)
        
        self.assertEqual(expectedContent, actualContent)
  
 
    
    def test_solve_013_ShouldRotateValidNominalCubeR(self):
        inputDict = {}
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = 'R'
        inputDict['op'] = 'solve'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        moves = inputDict['rotate']
        rotatedCube = 'rrwrrwrrwgggggggggyooyooyoobbbbbbbbbyyryyryyrwwowwowwo'
        myCube2 = cube.Cube()
        myCube2._load(rotatedCube)
        expectedContent = myCube2._getContent()
        actualContent = solve._movecontroller(content, moves)
        
        self.assertEqual(expectedContent, actualContent)
  
        
 
    def test_solve_014_ShouldRotateValidNominalCubeL(self):
        inputDict = {}
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = 'L'
        inputDict['op'] = 'solve'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        moves = inputDict['rotate']
        rotatedCube = 'yrryrryrrgggggggggoowoowoowbbbbbbbbboyyoyyoyyrwwrwwrww'
        myCube2 = cube.Cube()
        myCube2._load(rotatedCube)
        expectedContent = myCube2._getContent()
        actualContent = solve._movecontroller(content, moves)
        
        self.assertEqual(expectedContent, actualContent)
        
    

    def test_solve_015_ShouldRotateValidNominalCubeU(self):
        inputDict = {}
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = 'U'
        inputDict['op'] = 'solve'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        moves = inputDict['rotate']
        rotatedCube = 'gggrrrrrroooggggggbbboooooorrrbbbbbbyyyyyyyyywwwwwwwww'
        myCube2 = cube.Cube()
        myCube2._load(rotatedCube)
        expectedContent = myCube2._getContent()
        actualContent = solve._movecontroller(content, moves)
        
        self.assertEqual(expectedContent, actualContent)
        
    
    def test_solve_016_ShouldRotateValidNominalCubeD(self):
        inputDict = {}
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = 'D'
        inputDict['op'] = 'solve'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        moves = inputDict['rotate']
        rotatedCube = 'rrrrrrbbbggggggrrroooooogggbbbbbboooyyyyyyyyywwwwwwwww'
        myCube2 = cube.Cube()
        myCube2._load(rotatedCube)
        expectedContent = myCube2._getContent()
        actualContent = solve._movecontroller(content, moves)
        
        self.assertEqual(expectedContent, actualContent)
        

    def test_clockwise_040_ShouldReturn2DArrayClockwise(self):
        face = [
            [0,1,2],
            [3,4,5],
            [6,7,8]
            ]
        expectedResult = [
            [6,3,0],
            [7,4,1],
            [8,5,2]
            ]
        actualResult = solve._clockwise(face)
        self.assertEqual(expectedResult, actualResult)
    
    
    def test_counterclockwise_050_ShouldReturn2DArrayClockwise(self):
        face = [
            [0,1,2],
            [3,4,5],
            [6,7,8]
            ]
        expectedResult = [
            [2,5,8],
            [1,4,7],
            [0,3,6]
            ]
        actualResult = solve._counterclockwise(face)
        self.assertEqual(expectedResult, actualResult)
        
    def test_rotateedge_060_ShouldShiftEdgesF(self):
        cube = [
            [[1,2,3],
            [4,5,6],
            [7,8,9]],
            
            [[10,11,12],
            [13,14,15],
            [16,17,18]],
            
            [[19,20,21],
            [22,23,24],
            [25,26,27]],
            
            [[28,29,30],
            [31,32,33],
            [34,35,36]],
            
            [[37,38,39],
            [40,41,42],
            [43,44,45]],
            
            [[46,47,48],
            [49,50,51],
            [52,53,54]]
            ]
        
        expectedResult = [
            [[1,2,3],
            [4,5,6],
            [7,8,9]],
            
            [[43,11,12],
            [44,14,15],
            [45,17,18]], 
            
            [[19,20,21],
            [22,23,24],
            [25,26,27]],
            
            [[28,29,46],
            [31,32,47],
            [34,35,48]],
            
            [[37,38,39],
            [40,41,42],
            [36,33,30]],
            
            [[16,13,10],
            [49,50,51],
            [52,53,54]]
            ]
        action = 'F'
        actualResult = solve._switchedge(cube, action)
        self.assertEqual(expectedResult, actualResult)
        
    def test_rotateedge_070_ShouldShiftEdgesR(self):
        cube = [
            [[1,2,3],
            [4,5,6],
            [7,8,9]],
            
            [[10,11,12],
            [13,14,15],
            [16,17,18]],
            
            [[19,20,21],
            [22,23,24],
            [25,26,27]],
            
            [[28,29,30],
            [31,32,33],
            [34,35,36]],
            
            [[37,38,39],
            [40,41,42],
            [43,44,45]],
            
            [[46,47,48],
            [49,50,51],
            [52,53,54]]
            ]
        
        expectedResult = [
            [[1,2,48],
            [4,5,51],
            [7,8,54]],
            
            [[10,11,12],
            [13,14,15],
            [16,17,18]],
            
            [[45,20,21],
            [42,23,24],
            [39,26,27]],
            
            [[28,29,30],
            [31,32,33],
            [34,35,36]],
            
            [[37,38,3],
            [40,41,6],
            [43,44,9]],
            
            [[46,47,25],
            [49,50,22],
            [52,53,19]]
            ]
        action = 'R'
        actualResult = solve._switchedge(cube, action)
        self.assertEqual(expectedResult, actualResult)
        
    def test_rotateedge_080_ShouldShiftEdgesL(self):
        cube = [
            [[1,2,3],
            [4,5,6],
            [7,8,9]],
            
            [[10,11,12],
            [13,14,15],
            [16,17,18]],
            
            [[19,20,21],
            [22,23,24],
            [25,26,27]],
            
            [[28,29,30],
            [31,32,33],
            [34,35,36]],
            
            [[37,38,39],
            [40,41,42],
            [43,44,45]],
            
            [[46,47,48],
            [49,50,51],
            [52,53,54]]
            ]
        
        expectedResult = [
            [[37,2,3],
            [40,5,6],
            [43,8,9]],
            
            [[10,11,12],
            [13,14,15],
            [16,17,18]],
            
            [[19,20,52],
            [22,23,49],
            [25,26,46]],
            
            [[28,29,30],
            [31,32,33],
            [34,35,36]],
            
            [[27,38,39],
            [24,41,42],
            [21,44,45]],
            
            [[1,47,48],
            [4,50,51],
            [7,53,54]]
            ]
        action = 'L'
        actualResult = solve._switchedge(cube, action)
        self.assertEqual(expectedResult, actualResult)
        
    def test_rotateedge_090_ShouldShiftEdgesB(self):
        cube = [
            [[1,2,3],
            [4,5,6],
            [7,8,9]],
            
            [[10,11,12],
            [13,14,15],
            [16,17,18]],
            
            [[19,20,21],
            [22,23,24],
            [25,26,27]],
            
            [[28,29,30],
            [31,32,33],
            [34,35,36]],
            
            [[37,38,39],
            [40,41,42],
            [43,44,45]],
            
            [[46,47,48],
            [49,50,51],
            [52,53,54]]
            ]
        
        expectedResult = [
            [[1,2,3],
            [4,5,6],
            [7,8,9]],
            
            [[10,11,54],
            [13,14,53],
            [16,17,52]],
            
            [[19,20,21],
            [22,23,24],
            [25,26,27]],
            
            [[39,29,30],
            [38,32,33],
            [37,35,36]],
            
            [[12,15,18],
            [40,41,42],
            [43,44,45]],
            
            [[46,47,48],
            [49,50,51],
            [28,31,34]]
            ]
        action = 'B'
        actualResult = solve._switchedge(cube, action)
        self.assertEqual(expectedResult, actualResult)
    
    def test_rotateedge_100_ShouldShiftEdgesU(self):
        cube = [
            [[1,2,3],
            [4,5,6],
            [7,8,9]],
            
            [[10,11,12],
            [13,14,15],
            [16,17,18]],
            
            [[19,20,21],
            [22,23,24],
            [25,26,27]],
            
            [[28,29,30],
            [31,32,33],
            [34,35,36]],
            
            [[37,38,39],
            [40,41,42],
            [43,44,45]],
            
            [[46,47,48],
            [49,50,51],
            [52,53,54]]
            ]
        
        expectedResult = [
            [[10,11,12],
            [4,5,6],
            [7,8,9]],
            
            [[19,20,21],
            [13,14,15],
            [16,17,18]],
            
            [[28,29,30],
            [22,23,24],
            [25,26,27]],
            
            [[1,2,3],
            [31,32,33],
            [34,35,36]],
            
            [[37,38,39],
            [40,41,42],
            [43,44,45]],
            
            [[46,47,48],
            [49,50,51],
            [52,53,54]]
            ]
        action = 'U'
        actualResult = solve._switchedge(cube, action)
        self.assertEqual(expectedResult, actualResult)
    
    def test_rotateedge_110_ShouldShiftEdgesD(self):
        cube = [
            [[1,2,3],
            [4,5,6],
            [7,8,9]],
            
            [[10,11,12],
            [13,14,15],
            [16,17,18]],
            
            [[19,20,21],
            [22,23,24],
            [25,26,27]],
            
            [[28,29,30],
            [31,32,33],
            [34,35,36]],
            
            [[37,38,39],
            [40,41,42],
            [43,44,45]],
            
            [[46,47,48],
            [49,50,51],
            [52,53,54]]
            ]
        
        expectedResult = [
            [[1,2,3],
            [4,5,6],
            [34,35,36]],
            
            [[10,11,12],
            [13,14,15],
            [7,8,9]],
            
            [[19,20,21],
            [22,23,24],
            [16,17,18]],
            
            [[28,29,30],
            [31,32,33],
            [25,26,27]],
            
            [[37,38,39],
            [40,41,42],
            [43,44,45]],
            
            [[46,47,48],
            [49,50,51],
            [52,53,54]]
            ]
        action = 'D'
        actualResult = solve._switchedge(cube, action)
        self.assertEqual(expectedResult, actualResult)
        
    def test_rotateMiddle_140_ShouldRotateMiddleLayer(self):
        inputDict = {}
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        inputDict['op'] = 'solve'
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
   
        expectedResult = 'rrrgggrrrgggooogggooobbbooobbbrrrbbbyyyyyyyyywwwwwwwww'
        
        myCube._content = solve._rotateMiddle(content)
        actualResult = myCube._get()
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_rotateCubeClockwise_150_ShouldRotateEntireCubeClockWise(self):
        inputDict = {}
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        inputDict['op'] = 'solve'
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedContent = 'gggggggggooooooooobbbbbbbbbrrrrrrrrryyyyyyyyywwwwwwwww'
        myCube2 = cube.Cube()
        myCube2._load(expectedContent)
        expectedContent = myCube2._getContent()
        
        actualContent = solve._rotateCubeClockwise(content)
 
        self.assertEqual(expectedContent, actualContent)
        
    def test_movetranslator_160_ShouldTranslateMovesBasedOnCurrentFace(self):
        inputMoves = 'FfBbLlRrUuDd'
        face = 1
        expectedMoves = 'RrLlFfBbUuDd'
        actualMoves = solve._movetranslator(face, inputMoves)
        self.assertEqual(expectedMoves, actualMoves)
        
        face = 2
        expectedMoves = 'BbFfRrLlUuDd'
        actualMoves = solve._movetranslator(face, inputMoves)
        self.assertEqual(expectedMoves, actualMoves)
        
        face = 3
        expectedMoves = 'LlRrBbFfUuDd'
        actualMoves = solve._movetranslator(face, inputMoves)
        self.assertEqual(expectedMoves, actualMoves)
        
        face = 4
        expectedMoves = 'UuDdLlRrBbFf'
        actualMoves = solve._movetranslator(face, inputMoves)
        self.assertEqual(expectedMoves, actualMoves)
        
        face = 5
        expectedMoves = 'DdUuLlRrFfBb'
        actualMoves = solve._movetranslator(face, inputMoves)
        self.assertEqual(expectedMoves, actualMoves)
        
    def test_optimalUpperRotation_170_uBecauseLessMovesThanUUU(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'royoryrrrgbyogygggrrygoyoooorbrbgbbbbggbyyybowwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedRotations = 'u'
        startingFace = 2
        endingFace = 3
        actualRotations = solve.optimalUpperRotation(content, startingFace, endingFace)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_optimalUpperRotation_171_UUBecauseSameAsuu(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'royoryrrrgbyogygggrrygoyoooorbrbgbbbbggbyyybowwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedRotations = 'UU'
        startingFace = 2
        endingFace = 0
        actualRotations = solve.optimalUpperRotation(content, startingFace, endingFace)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_optimalUpperRotation_172_UUBecauseSameAsuu(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'royoryrrrgbyogygggrrygoyoooorbrbgbbbbggbyyybowwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedRotations = 'U'
        startingFace = 2
        endingFace = 1
        actualRotations = solve.optimalUpperRotation(content, startingFace, endingFace)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_optimalUpperRotation_173_uBecauseSameAsUUU(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'royoryrrrgbyogygggrrygoyoooorbrbgbbbbggbyyybowwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedRotations = 'u'
        startingFace = 3
        endingFace = 0
        actualRotations = solve.optimalUpperRotation(content, startingFace, endingFace)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_optimalUpperRotation_174_UBecauseSameAsuuu(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'royoryrrrgbyogygggrrygoyoooorbrbgbbbbggbyyybowwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedRotations = 'U'
        startingFace = 0
        endingFace = 3
        actualRotations = solve.optimalUpperRotation(content, startingFace, endingFace)
        self.assertEqual(expectedRotations, actualRotations)
        
    
    

        
    