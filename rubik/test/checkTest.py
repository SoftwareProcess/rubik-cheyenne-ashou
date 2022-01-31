from unittest import TestCase
import rubik.check as check 

class CheckTest(TestCase):
    #Happy
    def test_check_010_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')

    def test_check_011_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'bbbbrbbbbrrrrbrrrrggggyggggoooowooooyyyygyyyywwwwowwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
    
    def test_check_012_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbBBBBBBBBBgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
    
    #Sad test paths
    def test_check_013_ShouldReturnErrorNoCube(self):
        parm = {'op':'check',
                'cube': None}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: No value for "cube"\n')
    
    def test_check_014_ShouldReturnErrorTooLong(self):
        parm = {'op':'check',
                'cube':'1113222rrr111bbb222ooo111222rrrbbbooorrrbbbooowwwwwwwwwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: Length for "cube" is too big\nThere must be 54 elements.')
    
    def test_check_015_ShouldReturnErrorTooSmall(self):
        parm = {'op':'check',
                'cube':'113222rrr111bbb222ooo111222rrrbbbooo'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: Length for "cube" is too small\nThere must be 54 elements.')
    
    def test_check_016_ShouldReturnErrorMiddlePieceConflict(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyywwwwwywwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: 2 or more middle pieces have the same color')
    
    def test_check_017_ShouldReturnErrorNotSixColors(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbxrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: There must be 6 colors')
    
    def test_check_018_ShouldReturnErrorNotNineOccurences(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbrrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: Each color must have 9 occurrences')
        
    def test_check_019_ShouldReturnErrorNonAlphaNumeric(self):
        parm = {'op':'check',
                'cube':'000000000rr@rrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: Non-alphanumber character used in the value for "cube"')

