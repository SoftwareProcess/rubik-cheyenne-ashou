'''
The purpose of this module is to test all methods
associated with solving the first (bottom) layer
of the rubik cube

Created: 4/1/2022
Modified: 4/1/2022
@author:  Cheyenne Ashou
'''
import unittest
import rubik.solveBottomLayer as bottomLayer
import rubik.cube as cube
import rubik.check as check
from tkinter.constants import BOTTOM

class BottomLayerTest(unittest.TestCase):
    def test_checkSolved_010_ShouldReturnTrueForSolvedBottomLayer(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'roygrrrrrgorbgbgggyybyogoooygyobrbbborbyyygbowwwwwwwww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = True
        actualResult = bottomLayer._checkSolved(content)
        
        self.assertEqual(expectedResult, actualResult) 
    
    def test_checkSolved_011_ShouldReturnFalseBecauseMisplacedCorner(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bgyorrbrrrorbgbgggyygyoroobooogbgrboyrbyybyygwwwwwwwww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = False
        actualResult = bottomLayer._checkSolved(content)
        
        self.assertEqual(expectedResult, actualResult) 
        
    