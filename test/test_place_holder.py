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
        self.assertEqual(_(0)(1), 1)
        self.assertEqual(_(1)(1, 2), 2)

    def test_call_error(self):
        with self.assertRaises(IndexError):
            _(1)(1)

    def test_call_kw(self):
        self.assertEqual(_('first')(first=1), 1)

    def test_call_kw_error(self):
        with self.assertRaises(KeyError):
            _('first')(second='yes')

    def test_add_to_int(self):
        self.assertEqual((_(0) + 10)(2), 12)

    def test_add_from_int(self):
        self.assertEqual((10 + _(0))(2), 12)

    def test_add_to_place_holder(self):
        self.assertEqual((_(0) + _(1))(2, 3), 5)

    def test_sub_to_int(self):
        self.assertEqual((_(0) - 10)(2), -8)

    def test_sub_from_int(self):
        self.assertEqual((10 - _(0))(2), 8)

    def test_sub_to_place_holder(self):
        self.assertEqual((_(0) - _(1))(2, 3), -1)

    def test_mul_to_int(self):
        self.assertEqual((_(0) * 10)(2), 20)

    def test_mul_from_int(self):
        self.assertEqual((10 * _(0))(2), 20)

    def test_mul_to_place_holder(self):
        self.assertEqual((_(0) * _(1))(2, 3), 6)

    def test_div_to_int(self):
        self.assertEqual((_(0) / 10)(2), 0.2)

    def test_div_from_int(self):
        self.assertEqual((10 / _(0))(2), 5)

    def test_div_to_place_holder(self):
        self.assertEqual((_(0) / _(1))(6, 3), 2)

    def test_fdiv_to_int(self):
        self.assertEqual((_(0) // 10)(2), 0)

    def test_fdiv_from_int(self):
        self.assertEqual((10 // _(0))(3), 3)

    def test_fdiv_to_place_holder(self):
        self.assertEqual((_(0) // _(1))(7, 2), 3)

    def test_mod_to_int(self):
        self.assertEqual((_(0) % 10)(2), 2)

    def test_mod_from_int(self):
        self.assertEqual((10 % _(0))(3), 1)

    def test_mod_to_place_holder(self):
        self.assertEqual((_(0) % _(1))(7, 2), 1)

    def test_pow_to_int(self):
        self.assertEqual((_(0) ** 10)(2), 1024)

    def test_pow_from_int(self):
        self.assertEqual((10 ** _(0))(3), 1000)

    def test_pow_to_place_holder(self):
        self.assertEqual((_(0) ** _(1))(7, 2), 49)

    def test_getitem_to_place_holder(self):
        self.assertEqual(_(0)[2](['a', 'b', 'c', 'd']), 'c')

        self.assertEqual(_(1)[_(0)](2, ['a', 'b', 'c', 'd']), 'c')

        self.assertEqual(_(0)['a']({'a': 'b', 'c': 'd'}), 'b')

        self.assertEqual(_(1)[_(0)]('a', {'a': 'b', 'c': 'd'}), 'b')

        self.assertEqual(_(['a', 'b', 'c'])[_(0)](1), 'b')

        self.assertEqual(_({'a': 'b', 'c': 1})[_(0)]('c'), 1)


    def test_equal(self):
        self.assertTrue((_(0) == 5)(5))
        self.assertFalse((_(0) == 5)(6))
        self.assertTrue((5 == _(0))(5))

    def test_not_equal(self):
        self.assertFalse((_(0) != 5)(5))
        self.assertTrue((_(0) != 5)(6))

    def test_less_than_or_equal(self):
        self.assertTrue((_(0) <= 5)(5))
        self.assertFalse((_(0) <= 5)(6))

    def test_less_than(self):
        self.assertFalse((_(0) < 5)(5))
        self.assertTrue((_(0) < 5)(4))

    def test_greater_than_or_equal(self):
        self.assertTrue((_(0) >= 5)(5))
        self.assertFalse((_(0) >= 6)(5))

    def test_greater_than(self):
        self.assertFalse((_(0) > 5)(5))
        self.assertTrue((_(0) > 4)(5))

    def test_function_from_place_holder(self):
        def plus_one(x):
            return x + 1

        self.assertEqual(_(plus_one)(_(0))(5), 6)

        def plus(x, y):
            return x + y

        self.assertEqual(_(plus)(_(0), 5)(4), 9)
        self.assertEqual(_(plus)(_(0), _(1))(4, 5), 9)

    def test_abs(self):
        self.assertEqual((abs(_(0)))(-1), 1)

    def test_and(self):
        self.assertEqual((_(0) & _(1))({'1'}, {'1', '2'}), {'1'})

    def test_lshift(self):
        self.assertEqual((_(0) << 1)(2), 4)

    def test_rshift(self):
        self.assertEqual((_(0) >> 1)(4), 2)

    def test_inv(self):
        self.assertEqual( (~_(0))(4), -5)
