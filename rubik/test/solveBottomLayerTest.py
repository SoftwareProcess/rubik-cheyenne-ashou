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

@unittest.skip('skip until getContent method for cube is created and tested')
class BottomLayerTest(unittest.TestCase):
    pass
    # def test_checkSolved_010_ShouldReturnTrueForSolvedBottomLayer(self):
    #     inputDict = {}
    #     inputDict['op'] = 'solve'
    #     inputDict['cube'] = 'wyyrrbgbyggrrgybowbowooboryorrwbgroygwwwywggoryobwgbyb'
    #     expectedResult = True
    #     myCube = cube.Cube()
    #     myCube._load(inputDict['cube'])
    #     content = myCube._content
    #     actualResult = bottomLayer.checkSolved(content)
    #     self.assertEqual(expectedResult, actualResult)