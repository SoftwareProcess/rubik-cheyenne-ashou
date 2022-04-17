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
    
    def test_030_checkLeftEdgePlaced_ShouldReturnTrueBecauseMiddleLayerAlreadySolved(self):
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
    