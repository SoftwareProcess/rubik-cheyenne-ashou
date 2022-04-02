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
        
        expectedCornerCoord = (0,0)
        actualCornerCoord = bottomLayer._getCornerPiece(content)
        
        self.assertEqual(expectedCornerCoord, actualCornerCoord)
        
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
        
        expectedCornerCoord = (0,2) 
        actualCornerCoord = bottomLayer._getCornerPiece(content)
        
        self.assertEqual(expectedCornerCoord, actualCornerCoord)
        
    def test_022_getCornerPiece_shouldReturnBottomLeftCornerPieceCoordinateBecauseWrongOrientation(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rooyrgwrbyyyrgowggbbrgoyooowbyrboybrgrryyggbgbwowwwbww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedCornerCoord = (2,0) 
        actualCornerCoord = bottomLayer._getCornerPiece(content)
        
        self.assertEqual(expectedCornerCoord, actualCornerCoord)
        
    def test_023_getCornerPiece_shouldReturnBottomRightCornerPieceCoordinateBecauseWrongOrientation(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rowrrbrrwggbygobggooogoyoooyybrbbybggbwgyryyrywrwwwbww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedCornerCoord = (2,2) 
        actualCornerCoord = bottomLayer._getCornerPiece(content)
        
        self.assertEqual(expectedCornerCoord, actualCornerCoord)
        
    def test_024_getCornerPiece_shouldReturnBottomLeftCornerPieceCoordinateBecauseMisplacedCorner(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ybgorgbrgygrygoyggbyggoyoooryrrbbybowbwoyrbrrwwowwwbww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedCornerCoord = (2,0) 
        actualCornerCoord = bottomLayer._getCornerPiece(content)
        
        self.assertEqual(expectedCornerCoord, actualCornerCoord)
    
    def test_025_getCornerPiece_shouldReturnBottomRightCornerPieceCoordinateBecauseMisplacedCorner(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yywbrryrogbgggobggyybgoyooowborbyybbroroyrggrrwwwwwbww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedCornerCoord = (2,2) 
        actualCornerCoord = bottomLayer._getCornerPiece(content)
        
        self.assertEqual(expectedCornerCoord, actualCornerCoord)
    
    
    
    