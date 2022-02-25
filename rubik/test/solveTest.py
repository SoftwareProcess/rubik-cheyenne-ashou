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
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        expectedResult = {}
        expectedResult['cube'] = 'bwbybgrygyogyrrobwogrbgooggbwyworwogwwybygrroyowbwyrrb'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
