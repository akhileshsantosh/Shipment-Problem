import unittest
from src.shortest_path import ShortestPathCalculator
from src.util_functions import Constants


# This class implements unit test cases for the graph given in assignment
class ShortestPathTestSuite(unittest.TestCase):

    calculator = ShortestPathCalculator()

    def test_self_path(self):
        self.assertEqual((0, 'a', 0), self. __test_for_path('a', 'a'))
        self.assertEqual((0, 'b', 0), self.__test_for_path('b', 'b'))
        self.assertEqual((0, 'c', 0), self.__test_for_path('c', 'c'))
        self.assertEqual((0, 'd', 0), self. __test_for_path('d', 'd'))
        self.assertEqual((0, 'e', 0), self.__test_for_path('e', 'e'))
        self.assertEqual((0, 'f', 0), self.__test_for_path('f', 'f'))
        self.assertEqual((0, 'g', 0), self.__test_for_path('g', 'g'))
        self.assertEqual((0, 'h', 0), self.__test_for_path('h', 'h'))
        self.assertEqual((0, 'i', 0), self.__test_for_path('i', 'i'))
        self.assertEqual((0, 'j', 0), self.__test_for_path('j', 'j'))
        self.assertEqual((0, 'k', 0), self.__test_for_path('k', 'k'))

    def test_all_paths_from_DC(self):
        self.assertEqual((3, 'a,b', 1.5*3), self.__test_for_path('a', 'b'))
        self.assertEqual((5, 'a,c', 1.5*5), self.__test_for_path('a', 'c'))
        self.assertEqual((2, 'a,d', 1.5*2), self.__test_for_path('a', 'd'))
        self.assertEqual((13, 'a,d,f,e', 1.5*13), self.__test_for_path('a', 'e'))
        self.assertEqual((10, 'a,d,f', 1.5*10), self.__test_for_path('a', 'f'))
        self.assertEqual((7, 'a,d,g', 7*1.5), self.__test_for_path('a', 'g'))
        self.assertEqual((16, 'a,d,f,e,h', 16*1.5), self.__test_for_path('a', 'h'))
        self.assertEqual((15, 'a,d,f,i', 15*1.5), self.__test_for_path('a', 'i'))
        self.assertEqual((18, 'a,d,g,k,j', 18*1.5), self.__test_for_path('a', 'j'))
        self.assertEqual((12, 'a,d,g,k', 12*1.5), self.__test_for_path('a', 'k'))

    def test_non_existing_path(self):
        # Path not found
        self.assertEqual((Constants.MAX_INFINITY.value, None, None), self.__test_for_path('a', 'l'))
        self.assertEqual((Constants.MAX_INFINITY.value, None, None), self.__test_for_path('m', 'j'))

    @classmethod
    def __test_for_path(cls, source, destination):
        cls.calculator.source = source
        cls.calculator.destination = destination
        return cls.calculator.run()


if __name__ == '__main__':
    unittest.main()
