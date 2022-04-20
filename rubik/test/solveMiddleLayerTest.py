'''
Created: Apr 17, 2022
Modified: Apr 17, 2022
@author: Cheyenne Ashou
'''
import unittest
import rubik.cube as cube
import rubik.check as check
import rubik.solveMiddleLayer as middleLayer
import rubik.solve as solve
from rubik.solveMiddleLayer import _checkGoToNextFace, _checkMisorientedEdge
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
        #inputDict['cube'] = 'byyrrrgrbrgggggrggorrooooooyyobbbbbrbyyoyyybgwwwwwwwww'
        inputDict['cube'] = 'ogbrrrrrryorggbgggyygyoooooyogybbbbbrrbgybyyowwwwwwwww'
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = True
        actualResult = middleLayer._checkEdgePlaced(content, 'left')
        
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
        actualResult = middleLayer._checkEdgePlaced(content, 'left')
        
        self.assertEqual(expectedResult, actualResult)
    
    def test_022_checkRightEdgePlaced_ShouldReturnTrueBecauseMiddleLayerAlreadySolved(self):
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
        actualResult = middleLayer._checkEdgePlaced(content, 'right')
        
        self.assertEqual(expectedResult, actualResult)
        
        
        
    def test_023_checkRightEdgePlaced_ShouldReturnFalseBecauseMisorientedEdge(self):
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
        actualResult = middleLayer._checkEdgePlaced(content, 'right')
        
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
    
    
    def test_060_rotateEdgeToAdjacentFace_rightEdge(self):
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
        startingFace = middleLayer._findEdge(content, 'right')
        actualMoves = middleLayer._rotateEdgeToAdjacentFace(content, startingFace, 'right')
        
        self.assertEqual(expectedMoves, actualMoves)
        
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        expectedContent = myCube2._getContent()
        self.assertEqual(expectedContent, content)
        
    def test_061_rotateEdgeToAdjacentFace_leftEdge(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'royoryrrrgbyogygggrrygoyoooorbrbgbbbbggbyyybowwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
    
        expectedMoves = 'UU'
        startingFace = middleLayer._findEdge(content, 'left')
        actualMoves = middleLayer._rotateEdgeToAdjacentFace(content, startingFace, 'left')
        
        self.assertEqual(expectedMoves, actualMoves)
        
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        expectedContent = myCube2._getContent()
        self.assertEqual(expectedContent, content)
        
    def test_070_findTopColorEdgePieceInTopLayer_NoEdgePiecesOnTopFace(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rbryrbrrryggygrgggoooyoyooobgyobgbbbybyryogrbwwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = 4
        actualResult = middleLayer._findTopColorEdgePieceInTopLayer(content)
        
        self.assertEqual(expectedResult, actualResult)
        
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        expectedContent = myCube2._getContent()
        self.assertEqual(expectedContent, content)
        
    def test_071_findTopColorEdgePieceInTopLayer_OneEdgePiecesOnTopFace(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'boyyrgrrrrggrgrgggoyyyoyooooryobgbbbbbybyorbgwwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = 2
        actualResult = middleLayer._findTopColorEdgePieceInTopLayer(content)
        
        self.assertEqual(expectedResult, actualResult)
        
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        expectedContent = myCube2._getContent()
        self.assertEqual(expectedContent, content)
        
    def test_080_movesToInsertEdge_rightEdge(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'boyyrgrrrrggrgrgggoyyyoyooooryobgbbbbbybyorbgwwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = 'RurufUF'
        actualResult = middleLayer._movesToInsertEdge('right')
        
        self.assertEqual(expectedResult, actualResult)
        
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        expectedContent = myCube2._getContent()
        self.assertEqual(expectedContent, content)
        
    def test_081_movesToInsertEdge_leftEdge(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'boyyrgrrrrggrgrgggoyyyoyooooryobgbbbbbybyorbgwwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = 'lULUFuf'
        actualResult = middleLayer._movesToInsertEdge('left')
        
        self.assertEqual(expectedResult, actualResult)
        
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        expectedContent = myCube2._getContent()
        self.assertEqual(expectedContent, content)
    @unittest.skip('skip while making methods for misplaced edges')    
    def test_090_solve_NominalUnmixedCube(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedRotations = ''
        actualRotations = middleLayer._solve(content)
        
        self.assertEqual(expectedRotations, actualRotations)
        
    @unittest.skip('skip while making methods for misplaced edges')    
    def test_091_solve_NominalMixedCubeWithBottomLayerSolved(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yrooryrrryroggbgggbygyoooooygrybbbbbrryoybbggwwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        content2 = myCube2._getContent()
        
        rotations = middleLayer._solve(content)
        resultingCube = solve._movecontroller(content2, rotations)
        expectedResult = True
        actualResult = check.checkMiddleLayerSolved(resultingCube)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_100_checkMisoriented_noMisorientedEdgePieceOnFrontFace(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'broyryrrryoyggbgggbgryooooogooybrbbbyrrgybybgwwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = 'none'
        actualResult = middleLayer._checkMisorientedEdge(content)
        
        self.assertEqual(expectedResult, actualResult)
        
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        expectedContent = myCube2._getContent()
        self.assertEqual(expectedContent, content)
        
    def test_101_checkMisoriented_misorientedLedgeEdgePieceOnFrontFace(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ygyoryrrrobbggbgggrrryooooogooybbbbbyyygyrgrbwwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = 'left'
        actualResult = middleLayer._checkMisorientedEdge(content)
        
        self.assertEqual(expectedResult, actualResult)
        
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        expectedContent = myCube2._getContent()
        self.assertEqual(expectedContent, content)
        
    def test_102_checkMisoriented_misorientedRightEdgePieceOnFrontFace(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'brbrrgrrrroyogbggggggyoooooyroybybbbryobybygywwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = 'right'
        actualResult = middleLayer._checkMisorientedEdge(content)
        
        self.assertEqual(expectedResult, actualResult)
        
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        expectedContent = myCube2._getContent()
        self.assertEqual(expectedContent, content)
        
    
    def test_110_checkGoToNextFace_StayOnFaceEdgesNotPlaced(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'brbrrgrrrroyogbggggggyoooooyroybybbbryobybygywwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = {'face': False, 'leftEdge': False, 'rightEdge': False}
        actualResult = middleLayer._checkGoToNextFace(content)
        
        self.assertEqual(expectedResult, actualResult)
        
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        expectedContent = myCube2._getContent()
        self.assertEqual(expectedContent, content)
    
    def test_111_checkGoToNextFace_FaceAlreadySolved(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ogbrrrrrryorggbgggyygyoooooyogybbbbbrrbgybyyowwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = {'face': True, 'leftEdge': True, 'rightEdge': True}
        actualResult = middleLayer._checkGoToNextFace(content)
        
        self.assertEqual(expectedResult, actualResult)
        
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        expectedContent = myCube2._getContent()
        self.assertEqual(expectedContent, content)
        
    def test_120_insertLeftEdge_LeftEdgeAlreadyPlaced(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ogbrrrrrryorggbgggyygyoooooyogybbbbbrrbgybyyowwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = ''
        edgesPlaced = _checkGoToNextFace(content)
        leftEdgePlaced = edgesPlaced['leftEdge']
        self.assertEqual(leftEdgePlaced, True)
        actualResult = middleLayer._insertLeftEdge(content, leftEdgePlaced)
        
        self.assertEqual(expectedResult, actualResult)
    
    
    def test_121_insertLeftEdge_LeftEdgeNotPlaced(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gyyyooooobbgybbbbbyoborrrrryyyggbgggogrryrogrwwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = 'UlULUFuf'
        edgesPlaced = _checkGoToNextFace(content)
        leftEdgePlaced = edgesPlaced['leftEdge']
        self.assertEqual(leftEdgePlaced, False)
        actualResult = middleLayer._insertLeftEdge(content, leftEdgePlaced)
        self.assertEqual(expectedResult, actualResult)
        
    def test_130_insertRightEdge_RightEdgeAlreadyPlaced(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yoborrrrryyyggbggggyyyooooobbgybbbbbrgoryrrgowwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = ''
        edgesPlaced = _checkGoToNextFace(content)
        rightEdgePlaced = edgesPlaced['rightEdge']
        self.assertEqual(rightEdgePlaced, True)
        actualResult = middleLayer._insertRightEdge(content, rightEdgePlaced)
        self.assertEqual(expectedResult, actualResult)
        
    def test_131_insertRightEdge_RightEdgeNotPlacedYet(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gyyybbbbbbbgorrrrryobggbgggyyyyoooooogrryrogrwwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = 'UURurufUF'
        edgesPlaced = _checkGoToNextFace(content)
        rightEdgePlaced = edgesPlaced['rightEdge']
        self.assertEqual(rightEdgePlaced, False)
        actualResult = middleLayer._insertRightEdge(content, rightEdgePlaced)
        self.assertEqual(expectedResult, actualResult)
        
    def test_140_removeMisorientedLeftEdge_noMisorientedEdge(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yobggbgggyyyyooooogyyybbbbbbbgorrrrrrgoryrrgowwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        actualMisorientedEdge = _checkMisorientedEdge(content)
        expectedMisorientedEdge = 'none'
        self.assertEqual(expectedMisorientedEdge, actualMisorientedEdge)
        expectedResult = ''
        actualResult = middleLayer._removeMisorientedLeftEdge(content)
        self.assertEqual(expectedResult, actualResult)

    
    def test_141_removeMisorientedLeftEdge_actualMisorientedEdge(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'bbgorrrrryobggbgggyyyyooooogyyybbbbborogygrrrwwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        actualMisorientedEdge = _checkMisorientedEdge(content)
        expectedMisorientedEdge = 'left'
        self.assertEqual(expectedMisorientedEdge, actualMisorientedEdge)
        expectedResult = 'UlULUFuf'
        actualResult = middleLayer._removeMisorientedLeftEdge(content)
        self.assertEqual(expectedResult, actualResult)
        
    def test_150_removeMisorientedRightEdge_noMisorientedEdge(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yobggbgggyyyyooooogyyybbbbbbbgorrrrrrgoryrrgowwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        actualMisorientedEdge = _checkMisorientedEdge(content)
        expectedMisorientedEdge = 'none'
        self.assertEqual(expectedMisorientedEdge, actualMisorientedEdge)
        expectedResult = ''
        actualResult = middleLayer._removeMisorientedRightEdge(content)
        self.assertEqual(expectedResult, actualResult)
        
    def test_151_removeMisorientedRightEdge_actualMisorientedEdge(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'gyyybbbbbbbgorrrrryobggbgggyyyyoooooogrryrogrwwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        actualMisorientedEdge = _checkMisorientedEdge(content)
        expectedMisorientedEdge = 'right'
        self.assertEqual(expectedMisorientedEdge, actualMisorientedEdge)
        expectedResult = 'RurufUF'
        actualResult = middleLayer._removeMisorientedRightEdge(content)
        self.assertEqual(expectedResult, actualResult)
        
    def test_160_removeMisorientedEdge_noMisorientedLeftOrRightEdge(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yobggbgggyyyyooooogyyybbbbbbbgorrrrrrgoryrrgowwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        actualMisorientedEdge = _checkMisorientedEdge(content)
        expectedMisorientedEdge = 'none'
        self.assertEqual(expectedMisorientedEdge, actualMisorientedEdge)
        expectedResult = ''
        actualResult = middleLayer._removeMisorientedEdge(content)
        self.assertEqual(expectedResult, actualResult)
        
    def test_161_removeMisorientedEdge_misorientedLeftAndRightEdge(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'oygorbrrryyyrgbgggggryoooooygyybbbbbbrooyrbgrwwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = 'lULUFufUURurufUF'
        actualResult = middleLayer._removeMisorientedEdge(content)
        self.assertEqual(expectedResult, actualResult)
    
    
    
        
    
    
        
    
    