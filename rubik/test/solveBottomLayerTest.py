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
import rubik.solve as solve

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
     
    @unittest.skip('no longer need this test because change in functionality of method')   
    def test_027_getCornerPiece_shouldReturnTopCornerPieceCoordinateBecauseMisoriented(self):
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
    
    def test_050_openCorner_OpenCornerBecauseMisplacedCorner(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'oygggoogyrygyoyrooorrbbgbbbgoyrrorrgybybygbrwwwbwwwwww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = True
        actualResult = bottomLayer._openCorner(content)
        self.assertEqual(expectedResult, actualResult)
    
    def test_051_openCorner_ReturnFalseBecauseBottomLayerSolvedForFrontFace(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rrgrrorrroowbggggbbbgoobooywyyrbgrbboyogyygyywwwwwwbwy'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = False
        actualResult = bottomLayer._openCorner(content)
        self.assertEqual(expectedResult, actualResult)
        
    @unittest.skip('skip because change in functionality')
    def test_060_rotateToOpenCorner_NoRotationsBecuaseTopCornerAlreadyAtOpenCorner(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'oyyrobroygbgrbgrbbwoyrrorrroobbgygggbyogyywgoywbwwwwww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = ''
        actualResult = bottomLayer._rotateToOpenCorner(content)
        self.assertEqual(expectedResult, actualResult)
       
    @unittest.skip('skip because change in functionality') 
    def test_061_rotateToOpenCorner_BecuaseTopCornerAlreadyAtOpenCorner(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'oyyrrorrrgbgbgygggwoyrobroyoobrbgrbbbyogyywgowwwwwwbwy'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedResult = 'uu'
        actualResult = bottomLayer._rotateToOpenCorner(content)
        self.assertEqual(expectedResult, actualResult)
     
    def test_070_findMatchingRightCornerPiece(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yowbgyggbbyyboyyoyorgobggbbwrorrorrroybbygggowwrwwwwwr'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedFace = 2
        actualFace = bottomLayer._findMatchingCornerPiece(content)
        self.assertEqual(expectedFace, actualFace)
        
    def test_071_findMatchingCornerPiece_Left(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'orgobggbbwrorrorrryowbgyggbbyyboyyoyogggybbyorwwwwwrww'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
        
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
        
        expectedFace = 3
        actualFace = bottomLayer._findMatchingCornerPiece(content)
        self.assertEqual(expectedFace, actualFace)
        
    
    def test_080_rotateMatchingCornerPieceToFace_Right(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yowbgyggbbyyboyyoyorgobggbbwrorrorrroybbygggowwrwwwwwr'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
    
        expectedRotations = 'UU'
        actualRotations = bottomLayer._rotateMatchingCornerPieceToFace(content)
        self.assertEqual(expectedRotations, actualRotations)
        
        myCube2 = cube.Cube()
        myCube2._load(inputDict['cube'])
        expectedContent = myCube2._getContent()
        self.assertEqual(expectedContent, content)
        
    def test_081_rotateMatchingCornerPieceToFace_Left(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'orgobggbbwrorrorrryowbgyggbbyyboyyoyogggybbyorwwwwwrww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
    
        expectedRotations = 'UUU'
        actualRotations = bottomLayer._rotateMatchingCornerPieceToFace(content)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_082_rotateMatchingCornerPieceToFace_NoRotationsBecauseMatchingLeftCornerPieceAlreadyPresent(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'byyobggbborgrrorrrwrobgyggbyowboyyoygbogyyogbrwwwwwrww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
    
        expectedRotations = ''
        actualRotations = bottomLayer._rotateMatchingCornerPieceToFace(content)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_082_rotateMatchingCornerPieceToFace_NoRotationsBecauseMatchingRightCornerPieceAlreadyPresent(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yorrryrrgworrgyyggyoggoroooyybbbgbbbrybbygobgwwowwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
    
        expectedRotations = ''
        actualRotations = bottomLayer._rotateMatchingCornerPieceToFace(content)
        self.assertEqual(expectedRotations, actualRotations)
        
    def test_083_rotateMatchingCornerPieceToFace_NoRotationsBecauseCornerPieceAlreadyPlacedInBottomLayer(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
    
        expectedRotations = 'UUUU'
        actualRotations = bottomLayer._rotateMatchingCornerPieceToFace(content)
        self.assertEqual(expectedRotations, actualRotations)
        
    @unittest.skip('skip while observing output moves of this function')
    def test_090_movesToPlaceCornerPieces_noMovesRequiredBecauseBottomCubeSolvedAlready(self):
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
        actualRotations = bottomLayer._movesToPlaceCornerPieces(content)
        self.assertEqual(expectedRotations, actualRotations)
    #@unittest.skip('skip while observing output moves of function')    
    def test_091_movesToPlaceCornerPieces_noMovesRequiredBecauseBottomCubeSolvedAlready(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ggyrryrrbogoogbrgywyrroboogwroobgrbygbbyyywobbwwwwwywg'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
    
        moves = bottomLayer._movesToPlaceCornerPieces(content)
        inputDict['rotate'] = moves
    
        content = solve._solve(inputDict)
        myCube2 = cube.Cube()
        myCube2._load(content['cube'])
        expectedResult = True
        print(content)
        actualResult = bottomLayer._checkSolved(myCube2._getContent())
        
        self.assertEqual(expectedResult, actualResult)
       
    # def test_092_movesToPlaceCornerPieces_thisfunctionisonlyusedtoseeoutput(self):
    #     inputDict = {}
    #     inputDict['op'] = 'solve'
    #     inputDict['cube'] = 'ggyrryrrbogoogbrgywyrroboogwroobgrbygbbyyywobbwwwwwywg'
    #
    #     myCube = cube.Cube()
    #     myCube._load(inputDict['cube'])
    #     content = myCube._getContent()
    #
    #     expectedCheck = {'status': 'ok'}
    #     actualCheck = check._check(inputDict)
    #     self.assertEqual(expectedCheck, actualCheck)
    #
    #     expectedMoves = 'UURur'
    #     actualMoves = bottomLayer._movesToPlaceCornerPieces(content)
    #
    #     self.assertEqual(expectedMoves, actualMoves)
    #

    
    def test_100_rotateToFace_rotateCube180Degrees(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'ggyrryrrbogoogbrgywyrroboogwroobgrbygbbyyywobbwwwwwywg'
        
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
    
        myCube2 = cube.Cube()
        myCube2._load('wyrroboogwroobgrbyggyrryrrbogoogbrgybowyyybbggwywwwwwb')
        face = 2
        expectedCube = myCube2._getContent()
        actualCube = bottomLayer._rotateToFace(face, content)
        
        self.assertEqual(expectedCube, actualCube)


    
        
    
        
    
    
    
    