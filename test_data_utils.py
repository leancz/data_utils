import unittest
import data_utils

class DictCompareTest(unittest.TestCase):
    
    def test_empty(self):
        result = data_utils.dict_compare({}, {})
        expected = []
        self.assertEqual(result, expected)
    
    def test_non_dicts(self):
        """
        Instead of dicts we feed the function integers, strings, etc. This works as expected
        even though they are not dictionaries
        """
        self.assertEqual(data_utils.dict_compare(1, 1), [])
        self.assertEqual(data_utils.dict_compare(1, 2), [('Value difference', '', 1, 2)])
        self.assertEqual(data_utils.dict_compare(2, 'bob'), [('Value difference', '', 2, 'bob')])
        self.assertEqual(data_utils.dict_compare([2], set([2])), [('Value difference', '', [2], {2})])
    
    def test_complex(self):
        result = data_utils.dict_compare({99:{0:{'bob':1}, 1:1, 2:{'tipi':'hallo'}}}, {99:{0:{'bob':2}, 1:1, 2:2}})
        expected = [('Value difference', '[99][2]', {'tipi': 'hallo'}, 2), ('Value difference', '[99][0][bob]', 1, 2)]
        self.assertEqual(result, expected)

        

if __name__ == '__main__':
    unittest.main()
