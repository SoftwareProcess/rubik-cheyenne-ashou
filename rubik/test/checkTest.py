from unittest import TestCase
import rubik.check as check 
import rubik.solve as solve
import rubik.cube as cube
class CheckTest(TestCase):
    #Happy
    def test_check_010_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')

    def test_check_020_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'bbbbrbbbbrrrrbrrrrggggyggggoooowooooyyyygyyyywwwwowwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
    
    def test_check_030_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbBBBBBBBBBgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
    
    #Sad test paths
    def test_check_040_ShouldReturnErrorNoCube(self):
        parm = {'op':'check',
                'cube': None}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: 100 No cube input')
    
    def test_check_050_ShouldReturnErrorTooLong(self):
        parm = {'op':'check',
                'cube':'1113222rrr111bbb222ooo111222rrrbbbooorrrbbbooowwwwwwwwwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: 102 Cube length is greater than 54')
    
    def test_check_060_ShouldReturnErrorTooSmall(self):
        parm = {'op':'check',
                'cube':'113222rrr111bbb222ooo111222rrrbbbooo'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: 102 Cube length is less than 54')
    
    def test_check_070_ShouldReturnErrorMiddlePieceConflict(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyywwwwwywwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: 103 Some middle pieces have the same color')
    
    def test_check_080_ShouldReturnErrorNotSixColors(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbxrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: 104 Invalid amount of colors')
    
    def test_check_090_ShouldReturnErrorNotNineOccurences(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbrrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: 105 Each color must have 9 occurrences')
        
    def test_check_100_ShouldReturnErrorNonAlphaNumeric(self):
        parm = {'op':'check',
                'cube':'000000000rr@rrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: 106 Non-alphanumeric character used in cube')
    
    def test_solve_110_ValidCubeInvalidRotation(self):
        inputDict = {}
        inputDict['rotate'] = 'FfwrLlUuDdBb'
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'
        expectedResult = {}
        expectedResult['status'] = 'error: 101 Invalid rotation'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult['status'], actualResult['status'])
        
    def test_120_checkMiddleLayerSolvedTest_ShouldReturnTrueForFullySolvedCube(self):
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
        actualResult = check.checkMiddleLayerSolved(content)
        
        self.assertEqual(expectedResult, actualResult) 
        
    def test_121_checkMiddleLayerSolvedTest_ShouldReturnFalseBecauseMisorientedPiece(self):
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
        actualResult = check.checkMiddleLayerSolved(content)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_130_checkBottomLayerSolvedTest_ShouldReturnTrueForFullySolvedCube(self):
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
        actualResult = check.checkBottomLayerSolved(content)
        
        self.assertEqual(expectedResult, actualResult) 
        
    def test_131_checkBottomLayerSolvedTest_ShouldReturnFalseBecauseMisplacedCorner(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'rboorryrrbggggggggyboooooooyywbbybbbgyrryybryrwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
    
        expectedResult = False
        actualResult = check.checkMiddleLayerSolved(content)
    
        self.assertEqual(expectedResult, actualResult)
        
    def test_132_checkBottomLayerSolvedTest_FalseBecauseCorrectBottomFaceButSwitchedCorners(self):
        inputDict = {}
        inputDict['op'] = 'solve'
        inputDict['cube'] = 'yggrrrgrbyggbggrggoybooooooybrbbybbrooyyyrbyrwwwwwwwww'
    
        myCube = cube.Cube()
        myCube._load(inputDict['cube'])
        content = myCube._getContent()
    
        expectedCheck = {'status': 'ok'}
        actualCheck = check._check(inputDict)
        self.assertEqual(expectedCheck, actualCheck)
    
        expectedResult = False
        actualResult = check.checkMiddleLayerSolved(content)
    
        self.assertEqual(expectedResult, actualResult)    
    
    
    
    

    
