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
    @unittest.skip("skip while working on methods required for solve to work")
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
    
    def test_movecontroller_020_ShouldReturnStringOfFaceNumbers(self):
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
        
    
    def test_clockwise_030_ShouldReturn2DArrayClockwise(self):
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
    
    def test_counterclockwise_040_ShouldReturn2DArrayClockwise(self):
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
        
    def test_rotateedge_050_ShouldShiftEdgesF(self):
        cube = [
            [[1,2,3],
            [4,5,7],
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
            [[42,11,12],
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