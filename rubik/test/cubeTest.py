'''
This module tests all methods of the cubeT
Created: 2/24/2022
Modified: 4/1/2022
@author: Cheyenne Ashou
'''
import unittest
import rubik.cube as cube


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
        
    def test_load_020_ShouldLoadContentsIntoCube(self):
        inputDict = {}
        inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        content = inputDict.get('cube')
        expectedContent = [
                        [['b','g','g'],['w','b','y'],['b','y','r']],
                        [['w','o','g'],['o','r','r'],['y','b','w']],
                        [['o','g','r'],['b','g','o'],['o','g','g']],
                        [['b','w','o'],['w','o','r'],['w','o','r']],
                        [['w','w','y'],['b','y','g'],['y','y','o']],
                        [['y','r','g'],['b','w','y'],['r','r','b']]
                            ]
        expectedColContent = [
                        [['b','w','b'],['g','b','y'],['g','y','r']],
                        [['w','o','y'],['o','r','b'],['g','r','w']],
                        [['o','b','o'],['g','g','g'],['r','o','g']],
                        [['b','w','w'],['w','o','o'],['o','r','r']],
                        [['w','b','y'],['w','y','y'],['y','g','o']],
                        [['y','b','r'],['r','w','r'],['g','y','b']]
                            ]
        myCube = cube.Cube()
        myCube._load(content)
        self.assertEqual(expectedContent, myCube._content)
    
    
    def test_get_030_ShouldReturnContentsOfCubeAsString(self):
        inputDict = {}
        inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        content = inputDict.get('cube')
        expectedContent = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        myCube = cube.Cube()
        myCube._load(content)
        actualContent = myCube._get()
        self.assertEqual(expectedContent, actualContent)
        
    def test_getContent_040_ShouldReturn3DArrayOfCube(self):
        inputDict = {}
        inputDict['cube'] = 'bggwbybyrwogorrybwogrbgooggbwoworworwwybygyyoyrgbwyrrb'
        inputDict['op'] = 'solve'
        myCube = cube.Cube()
        content = inputDict['cube']
        myCube._load(content)
        expectedContent = [
                        [['b','g','g'],['w','b','y'],['b','y','r']],
                        [['w','o','g'],['o','r','r'],['y','b','w']],
                        [['o','g','r'],['b','g','o'],['o','g','g']],
                        [['b','w','o'],['w','o','r'],['w','o','r']],
                        [['w','w','y'],['b','y','g'],['y','y','o']],
                        [['y','r','g'],['b','w','y'],['r','r','b']]
                            ]
        actualContent = myCube._getContent()
        self.assertEqual(expectedContent, actualContent)
        
    def test_setContent_050_ShouldChangeValueOfContentToInputValue(self):
        myCube = cube.Cube()
        content = [
                   [['b','g','g'],['w','b','y'],['b','y','r']],
                    [['w','o','g'],['o','r','r'],['y','b','w']],
                    [['o','g','r'],['b','g','o'],['o','g','g']],
                    [['b','w','o'],['w','o','r'],['w','o','r']],
                    [['w','w','y'],['b','y','g'],['y','y','o']],
                    [['y','r','g'],['b','w','y'],['r','r','b']]
                        ]
        myCube._setContent(content)
        actualContent = myCube._getContent()
        self.assertEqual(content, actualContent)
    

