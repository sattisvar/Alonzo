import unittest
from place_holder import PlaceHolder, _

class PlaceHolderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._0 = PlaceHolder()
        cls._first = PlaceHolder('first')
        cls._1 = PlaceHolder()

    @classmethod
    def tearDownClass(cls):
        PlaceHolder.reset()
        
    def test_call(self):
        self.assertEqual(self._0(1), 1)
        self.assertEqual(self._1(1, 2), 2)

    def test_call_error(self):
        with self.assertRaises(IndexError):
            self._1(1)
            
    def test_call_kw(self):
        self.assertEqual(self._first(first=1), 1)

    def test_call_kw_error(self):
        with self.assertRaises(KeyError):
            self._first(second='yes')

    def test_add_to_int(self):
        self.assertEqual((self._0 + 10)(2), 12)

    def test_add_from_int(self):
        self.assertEqual((10 + self._0)(2), 12)

    def test_add_to_place_holder(self):
        self.assertEqual((self._0 + self._1)(2, 3), 5)

    def test_sub_to_int(self):
        self.assertEqual((self._0 - 10)(2), -8)

    def test_sub_from_int(self):
        self.assertEqual((10 - self._0)(2), 8)

    def test_sub_to_place_holder(self):
        self.assertEqual((self._0 - self._1)(2, 3), -1)

    def test_sub_to_same(self):
        self.assertEqual((self._0 - self._0)(4), 0)

class PlaceHolderBuilderTest(unittest.TestCase):
    def test_call(self):
        self.assertEqual(_[0](1), 1)
        self.assertEqual(_[1](1, 2), 2)

    def test_call_error(self):
        with self.assertRaises(IndexError):
            _[1](1)
            
    def test_call_kw(self):
        self.assertEqual(_['first'](first=1), 1)

    def test_call_kw_error(self):
        with self.assertRaises(KeyError):
            _['first'](second='yes')

    def test_add_to_int(self):
        self.assertEqual((_[0] + 10)(2), 12)

    def test_add_from_int(self):
        self.assertEqual((10 + _[0])(2), 12)

    def test_add_to_place_holder(self):
        self.assertEqual((_[0] + _[1])(2, 3), 5)

    def test_sub_to_int(self):
        self.assertEqual((_[0] - 10)(2), -8)

    def test_sub_from_int(self):
        self.assertEqual((10 - _[0])(2), 8)

    def test_sub_to_place_holder(self):
        self.assertEqual((_[0] - _[1])(2, 3), -1)

    def test_mul_to_int(self):
        self.assertEqual((_[0] * 10)(2), 20)

    def test_mul_from_int(self):
        self.assertEqual((10 * _[0])(2), 20)

    def test_mul_to_place_holder(self):
        self.assertEqual((_[0] * _[1])(2, 3), 6)

    def test_div_to_int(self):
        self.assertEqual((_[0] / 10)(2), 0.2)

    def test_div_from_int(self):
        self.assertEqual((10 / _[0])(2), 5)

    def test_div_to_place_holder(self):
        self.assertEqual((_[0] / _[1])(6, 3), 2)
