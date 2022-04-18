'''
Created: Apr 17, 2022
Modified: Apr 17, 2022
@author: Cheyenne Ashou
'''
import unittest
import rubik.cube as cube
import rubik.check as check
import rubik.solveMiddleLayer as middleLayer
class SolveMiddleLayerTest(unittest.TestCase):
    
    def test_010_checkSolvedTest_ShouldReturnTrueForFullySolvedCube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = True
        actualResult = middleLayer._checkSolved(content)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_011_checkMiddleLayerSolvedTest_ShouldReturnFalseBecauseMisorientedPiece(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rggbrrrrryobggggggyboooooooyybbbrbbbgyoryyyyrwwwwwwwww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = False
        actualResult = middleLayer._checkSolved(content)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_012_checkMiddleLayerSolvedTest_ShouldReturnFalseBecauseMisorientedPiece(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'byyrrrgrbrgggggrggorrooooooyyobbbbbrbyyoyyybgwwwwwwwww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = False
        actualResult = middleLayer._checkSolved(content)
        
        self.assertEqual(expectedResult, actualResult)
    
    def test_020_checkLeftEdgePlaced_ShouldReturnTrueBecauseMiddleLayerAlreadySolved(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'byyrrrgrbrgggggrggorrooooooyyobbbbbrbyyoyyybgwwwwwwwww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = True
        actualResult = middleLayer._checkLeftEdgePlaced(content)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_021_checkLeftEdgePlaced_ShouldReturnFalseBecauseMisorientedLeftEdge(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rrygrrgrbobogggrggybrooooooyyybbybbrbrgoyygybwwwwwwwww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = False
        actualResult = middleLayer._checkLeftEdgePlaced(content)
        
        self.assertEqual(expectedResult, actualResult)
    
    def test_030_checkRightEdgePlaced_ShouldReturnTrueBecauseMiddleLayerAlreadySolved(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'byyrrrgrbrgggggrggorrooooooyyobbbbbrbyyoyyybgwwwwwwwww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = True
        actualResult = middleLayer._checkRightEdgePlaced(content)
        
        self.assertEqual(expectedResult, actualResult)
        
        
        
    def test_031_checkRightEdgePlaced_ShouldReturnFalseBecauseMisorientedEdge(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ryyrrgrrroyrrgggggyooooooooyyybbbbbbgybryggbbwwwwwwwww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = False
        actualResult = middleLayer._checkRightEdgePlaced(content)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_040_findEdge_ReturnFace4BecauseLeftEdgeAlreadyPlaced(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ryyrrgrrroyrrgggggyooooooooyyybbbbbbgybryggbbwwwwwwwww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = 4
        actualResult = middleLayer._findEdge(content, 'left')
        self.assertEqual(expectedResult, actualResult)
        
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        expectedContent = myCube2._getContent()
        self.assertEqual(expectedContent, content)
        
    def test_041_findEdge_Left(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'royoryrrrgbyogygggrrygoyoooorbrbgbbbbggbyyybowwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
    
        expectedResult = 3
        actualResult = middleLayer._findEdge(content, 'left')
    
        self.assertEqual(expectedResult, actualResult)
        
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        expectedContent = myCube2._getContent()
        self.assertEqual(expectedContent, content)
        
    def test_050_findEdge_ReturnFace4BecauseRightEdgeAlreadyPlaced(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
    
        expectedResult = 4
        actualResult = middleLayer._findEdge(content, 'right')
        self.assertEqual(expectedResult, actualResult)
        
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        expectedContent = myCube2._getContent()
        self.assertEqual(expectedContent, content)
           
    def test_051_findEdge_Right(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'royoryrrrgbyogygggrrygoyoooorbrbgbbbbggbyyybowwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
    
        expectedResult = 2
        actualResult = middleLayer._findEdge(content, 'right')
    
        self.assertEqual(expectedResult, actualResult)
        
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        expectedContent = myCube2._getContent()
        self.assertEqual(expectedContent, content)
    
    @unittest.skip('skip while making optimalUpperRotation method')
    def test_060_rotateEdgeToFace(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'royoryrrrgbyogygggrrygoyoooorbrbgbbbbggbyyybowwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
    
        expectedMoves = 'u'
        actualMoves = middleLayer._rotateEdgeToFace(content, 'right')
        
        self.assertEqual(expectedMoves, actualMoves)
        
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        expectedContent = myCube2._getContent()
        self.assertEqual(expectedContent, content)
        
  
    
    