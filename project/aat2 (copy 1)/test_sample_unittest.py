import unittest


def generator(test_class, a, b):
    def test(self):
        self.assertEqual(a, b)
    return test


def _add_test_methods(test_class):
    """#First element of list is variable "a", then variable "b",
    then name of test case that will be used as suffix."""
    test_list = [[2, 3, 'one'], [5, 5, 'two'], [0, 0, 'three']]
    for case in test_list:
        test = generator(test_class, case[0], case[1])
        setattr(test_class, "test_%s" % case[2], test)


class TestAuto(unittest.TestCase):
    def setUp(self):
        print('Setup')
        pass

    def tearDown(self):
        print('TearDown')
        pass


_add_test_methods(TestAuto)
"""It's better to start with underscore so it is not
detected as a test itself"""

if __name__ == '__main__':
    unittest.main(verbosity=1)