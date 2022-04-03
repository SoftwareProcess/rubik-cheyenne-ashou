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
        
    def test_020_getCornerPiece_shouldReturnTopLeftCornerPieceCoordinateBecauseCornerReadyToPlace(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rbgorybryygbggrrgrygwyoogogorwbbyybogrobyobyrwwbwwwoww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedCornerCoord = (0,0,'luL')
        actualCornerCoord = bottomLayer._getCornerPiece(content)
        
        self.assertEqual(expectedCornerCoord, actualCornerCoord)
        
    def test_021_getCornerPiece_shouldReturnTopRightCornerPieceCoordinateBecauseCornerReadyToPlace(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bbrgrggrbwborgowggyorgoyooobyyrbyybywygbyrrogrwowwwbww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedCornerCoord = (0,2, 'RUr') 
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
        
        expectedCornerCoord = (2,0, 'FUf') 
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
        
        expectedCornerCoord = (2,2, 'fuF') 
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
        
        expectedCornerCoord = (2,0,'luL') 
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
        
        expectedCornerCoord = (2,2, 'RUr') 
        actualCornerCoord = bottomLayer._getCornerPiece(content)
        
        self.assertEqual(expectedCornerCoord, actualCornerCoord)
    
    def test_026_getCornerPiece_shouldReturnTopLeftCornerPieceCoordinateBecauseMisoriented(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rgbgryyrbrybbgowggybogoroobyygbbrrbrgoooyrwyygwowwwwww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedCornerCoord = (0,0, 'lUUL') 
        actualCornerCoord = bottomLayer._getCornerPiece(content)
        
        self.assertEqual(expectedCornerCoord, actualCornerCoord)
        
    def test_027_getCornerPiece_shouldReturnTopRightCornerPieceCoordinateBecauseMisoriented(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yyggryyrbrgbbgowggrybgoroobybobbrrbroryoyygowgwowwwwww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedCornerCoord = (0,2, 'RUUr') 
        actualCornerCoord = bottomLayer._getCornerPiece(content)
        
        self.assertEqual(expectedCornerCoord, actualCornerCoord)
    
    def test_030_checkPiecesOnTopLayer_ReturnTrueBecauseWhiteOnFrontOnAtLeastOneSideOfTopLayer(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gbbrrobrrwoobgoyggbywgoyoogbrwbbgybrogyyyyrrrywgwwwoww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = True
        actualResult = bottomLayer._checkPiecesOnTopLayer(content)
        
        self.assertEqual(expectedResult, actualResult) 
        
    def test_031_checkPiecesOnTopLayer_ReturnFalseBecauseAllNeededCornerPiecesOnBottomLayer(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'byorrrrrgborygowggggogoyoowybyobbobbgryyybrgywwrwwwbww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = False
        actualResult = bottomLayer._checkPiecesOnTopLayer(content)
        
        self.assertEqual(expectedResult, actualResult)
      
      
    def test_040_findOpenCorner(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bogyrbyryryrygobggyybgoboogogrrbrybrwgbryowbwgwowwwoww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedFace = 0
        actualFace = bottomLayer._findOpenCorner(content)
        self.assertEqual(expectedFace, actualFace)
        
    def test_041_findOpenCorner(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rygbbgbbborrrrgrrygoyygobggbyggoyooorbyrybwoywwwwwwwwo'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedFace = 2
        actualFace = bottomLayer._findOpenCorner(content)
        self.assertEqual(expectedFace, actualFace)
    @unittest.skip("skip untilCheckOpenCorner is tested and created")   
    def test_042_findOpenCorner(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'orrbbgbbbgoyrrorrgoygggoogyrygyoyroowrbgybybywwwwwwbww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedFace = 2
        actualFace = bottomLayer._findOpenCorner(content)
        self.assertEqual(expectedFace, actualFace)
    
    def test_050_openCorner(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'oygggoogyrygybyrooorrbbgbbbgoyrrorrgybybygbrwwwbwwwwww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = True
        actualResult = bottomLayer._openCorner(content)
        self.assertEqual(expectedResult, actualResult)
    
    # def test_040_rotateToOpenCorner_NoRotationsBecuaseTopCornerAlreadyAtOpenCorner(self):
    #     inputDict= {}
    #     inputDict['op'] = 'so'
        
    
    
    
    