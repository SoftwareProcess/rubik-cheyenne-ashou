'''
Created on Feb 24, 2022

@author: cheyennea.
'''
import unittest
import rubik.cube as cube
from certifi.core import contents

class CubeTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

# Analysis:    Cube    class
#                methods: instantiate
#                         load - takes a serialized string and loads it into the cube
#                         get - takes the contents of cube and returns it as a string
# Analysis:    Cube.__init__
#    inputs: no input parameter
#    outputs: 
#        side-effects:
#        nominal: empty instance of cube
#        abnormal: N/A


    def test_init_010_ShouldCreateEmptyCube(self):
        myCube = cube.Cube()
        self.assertIsInstance(myCube, cube.Cube)
        
    def test_load_020_(self):
        inputDict = {}
        inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        content = inputDict.get('cube')
        expectedContent = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        myCube = cube.Cube()
        myCube._load(content)
        self.assertEqual(expectedContent, myCube._content)

