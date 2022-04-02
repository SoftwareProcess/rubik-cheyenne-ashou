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
    def test_010_checkSolved_ShouldReturnTrueForSolvedBottomLayer(self):
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
    
    def test_011_checkSolved_ShouldReturnFalseBecauseMisplacedCorner(self):
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
        
    def test_012_checkSolved_ShouldReturnFalseBecauseWrongColorOnBottomFace(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rrgorryrryyobgbgggybwyogooorgbobybbobogyyrygrbwwwwwwww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = False
        actualResult = bottomLayer._checkSolved(content)
        
        self.assertEqual(expectedResult, actualResult) 
        
    def test_020_getCornerPiece_shouldReturnTopLeftCornerPieceCoordinate(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rbgorybryygbggrrgrygwyoogogorwbbyybogrobyobyrwwbwwwoww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = (0,0)
        actualResult = bottomLayer._getCornerPiece(content)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_021_getCornerPiece_shouldReturnTopRightCornerPieceCoordinate(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bbrgrggrbwborgowggyorgoyooobyyrbyybywygbyrrogrwowwwbww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = (0,2) 
        actualResult = bottomLayer._getCornerPiece(content)
        
        self.assertEqual(expectedResult, actualResult)
    
    