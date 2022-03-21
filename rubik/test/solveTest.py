'''
Created on Feb 24, 2022

@author: cheyennea.
'''
import unittest
import rubik.solve as solve
import rubik.cube as cube

class SolveTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

# Analysis:    solve
#
#    inputs:
#        parms:        dictionary; mandatory; arrives validated
#        parms['op']    string, "solve"; mandatory; arrives validated
#        parms['cube']    string; len=54, [azAZ09], ... , mandatory, arrives unvalidated -> defensive programming
#        parms['rotate']    string; len >= 0, [FfRrBbLlUuDd]; optional, default to F if missing; arrives unvalidated 
#
#    outputs:
#        side-effects: no state change, no external effects, nothing other than input or output 
#        returns: dictionary
#        nominal:
#            dictionary['cube']: string, len=54
#            dictionary['status']: 'ok'
#        abnormal:
#            dictionary['status']: 'error: xxx' where xxx is a dev selected message
#
#    confidence level: boundary level analysis
#
#    happy path:
#        test 010: nominal (any random) cube with F rotation
#        test 020: nominal cube with f rotation
#        test 030: nominal valid cube with missing rotation
#        test 040: nominal valid cube with "" as rotation
#        test 050: ...
#
#    sad path:
#        test 910: missing cube
#        test 920: valid cube, invalid rotation (i.e 'w')
#        test 930: all the other invalid inputs
    
    def test_solve_010_ShouldRotateValidNominalCubeF(self):
        inputDict = {}
        inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        inputDict['rotate'] = 'F'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'bwbybgrygyogyrrobwogrbgooggbwyworwogwwybygrroyowbwyrrb'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    
    
    #Show a test case for a string of rotations
    def test_solve_011_ShouldRotateValidNominalCubeWithPrimeMoves(self):
        inputDict = {}
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = 'FfRrLlUuDdBb'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    
    def test_solve_012_ShouldRotateValidNominalCubeB(self):
        inputDict = {}
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = 'B'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'rrrrrrrrrggwggwggwoooooooooybbybbybbgggyyyyyywwwwwwbbb'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    # def test_solve_013_shouldRotateFOnNominalCubeMissingRotation(self):
    #     inputDict={}
    #     inputDict['cube'] = 'IIIIIIIII666666666lllllllllOOOOOOOOObbbbbbbbbGGGGGGGGG'
    #     inputDict['op'] = 'solve'
    #
    #     epxectedResult = {}
    #     expectedResult['status'] = 'ok'
    #     expectedResult['cube'] = 'IIIIIIIIIb66b66b66'
    
    def test_solve_021_ShouldRotateValidNominalCubeR(self):
        inputDict = {}
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = 'R'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'rrwrrwrrwgggggggggyooyooyoobbbbbbbbbyyryyryyrwwowwowwo'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_022_ShouldRotateValidNominalCubeL(self):
        inputDict = {}
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = 'L'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'yrryrryrrgggggggggoowoowoowbbbbbbbbboyyoyyoyyrwwrwwrww'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_023_ShouldRotateValidNominalCubeU(self):
        inputDict = {}
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = 'U'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'gggrrrrrroooggggggbbboooooorrrbbbbbbyyyyyyyyywwwwwwwww'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_024_ShouldRotateValidNominalCubeD(self):
        inputDict = {}
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = 'D'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'rrrrrrbbbggggggrrroooooogggbbbbbboooyyyyyyyyywwwwwwwww'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    @unittest.skip("skip because test case is no longer valid")
    
    def test_movecontroller_030_ShouldReturnStringOfFaceNumbers(self):
        inputDict = {}
        inputDict['rotate'] = 'FfRrUuDdLlFBbRl'
        expectedResult = '001144553302213'
        content = [
                        [['b','g','g'],['w','b','y'],['b','y','r']],
                        [['w','o','g'],['o','r','r'],['y','b','w']],
                        [['o','g','r'],['b','g','o'],['o','g','g']],
                        [['b','w','o'],['w','o','r'],['w','o','r']],
                        [['w','w','y'],['b','y','g'],['y','y','o']],
                        [['y','r','g'],['b','w','y'],['r','r','b']]
                    ]
        actualResult = solve._movecontroller(content, inputDict['rotate'])
        self.assertEqual(expectedResult, actualResult)
        
    
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
        
#Iteration 2
#    inputs:
#        parms:        dictionary; mandatory; arrives validated
#        parms['op']    string, "solve"; mandatory; arrives validated
#        parms['cube']    string; len=54, [azAZ09], ... , mandatory, arrives unvalidated -> defensive programming
#        parms['rotate']    string; len >= 0, [FfRrBbLlUuDd]; optional, default to "solve" mode if missing; arrives unvalidated 
#
#    outputs:
#        side-effects: no state change, no external effects, nothing other than input or output 
#        returns: dictionary
#        nominal:
#            If the input cube is valid and rotate is present:
#                dictionary['cube']: string, len=54
#                dictionary['status']: 'ok'
#            If the input cube is valid and rotate is MISSING:
#                dictionary['solution']: string, len >= 0
#                dictionary['status']: 'ok'
#        abnormal:
#            dictionary['status']: 'error: xxx' where xxx is a dev selected message
#        
    @unittest.skip("skip due to change of requirements")
    def test_movecontroller_120_ShouldRotateFOnNominalCubeEmptyRotation(self):
        inputDict = {}
        inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'bwbybgrygyogyrrobwogrbgooggbwyworwogwwybygrroyowbwyrrb'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    @unittest.skip("skip due to change of requirements")
    def test_movecontroller_121_ShouldRotateFOnNominalCubeMissingRotation(self):
        inputDict = {}
        inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'bwbybgrygyogyrrobwogrbgooggbwyworwogwwybygrroyowbwyrrb'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
   # @unittest.skip("skip while working on solution method")
    def test_solve_130_ShouldReturnEmptySolutionForUnmixedValidCube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        
        expectedResult = {}
        expectedResult['solution'] = ''
        expectedResult['status'] = 'ok'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        
        actualResult = solve._solve(inputDict)
        #actualResult = solve._bottomcross(myCube)
        
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        self.assertEqual(expectedResult, actualResult)
    
    #@unittest.skip("skip while making formBottomCross method")    
    def test_solve_140_ShouldSolveBottomCrossForMixedValidCube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        #inputDict['cube'] = 'rgrwgoybogbrwowyboyyorbybgwgygorbbggwrbgyowryorbwwyrow'
        inputDict['cube'] = 'brborgyboywgrggwowoogyowbywrwybbyoorwbyrygrbogygwwgbrr'
        bottomFaceColor = inputDict['cube'][49]
        
        moves = solve._solve(inputDict).get('solution')
        
        inputDict['rotate'] = moves
        
        actualResult = solve._solve(inputDict)
        
        
        #self.assertEqual(moves, 'fFrrR')
        self.assertEqual(actualResult['cube'][46], bottomFaceColor)
        self.assertEqual(actualResult['cube'][7], actualResult['cube'][4])
        self.assertEqual(actualResult['cube'][48], bottomFaceColor)
        self.assertEqual(actualResult['cube'][34], actualResult['cube'][31])
        self.assertEqual(actualResult['cube'][50], bottomFaceColor)
        self.assertEqual(actualResult['cube'][16], actualResult['cube'][13])
        self.assertEqual(actualResult['cube'][52], bottomFaceColor)
        self.assertEqual(actualResult['cube'][25], actualResult['cube'][22])
        

        
    @unittest.skip("no longer needed")
    def test_150_ShouldRotateMiddleLayer(self):
        inputDict = {}
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        inputDict['op'] = 'solve'
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._content
        
   
        expectedResult = 'rrrgggrrrgggooogggooobbbooobbbrrrbbbyyyyyyyyywwwwwwwww'
        
        actualResult = solve._rotateMiddle(content)
        actualResult = myCube._get()
        
        self.assertEqual(expectedResult, actualResult)

    def test_160_ShouldRotateEntireCubeClockWise(self):
        inputDict = {}
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        inputDict['op'] = 'solve'
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        
   
        expectedResult = 'gggggggggooooooooobbbbbbbbbrrrrrrrrryyyyyyyyywwwwwwwww'
        
        actualResult = solve._rotateCubeClockwise(myCube)
        actualResult = myCube._get()
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_170_ShouldTranslateMovesBasedOnCurrentFace(self):
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

    def test_180_ShouldFormBottomCrossGivenCubeHasTopFlower(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'wrwrbboyygbborobbrrggygrwygooogoyrggywywywbwrwgoowrybb'
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        bottomFaceColor = inputDict['cube'][49]
        
        moves = solve._formBottomCross(myCube)
        inputDict['rotate'] = moves
        actualResult = solve._solve(inputDict)
        
        expectedMoves = 'UFFUURRUBBLL'
        actualMoves = moves
        solve._solve(inputDict)
        self.assertEqual(expectedMoves, actualMoves)
        self.assertEqual(actualResult['cube'][46], bottomFaceColor)
        self.assertEqual(actualResult['cube'][7], actualResult['cube'][4])
        self.assertEqual(actualResult['cube'][48], bottomFaceColor)
        self.assertEqual(actualResult['cube'][34], actualResult['cube'][31])
        self.assertEqual(actualResult['cube'][50], bottomFaceColor)
        self.assertEqual(actualResult['cube'][16], actualResult['cube'][13])
        self.assertEqual(actualResult['cube'][52], bottomFaceColor)
        self.assertEqual(actualResult['cube'][25], actualResult['cube'][22])
    
        
    

    
        