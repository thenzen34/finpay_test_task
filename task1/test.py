import unittest

from .task1 import task1_use_regular, task1_use_foreach


class TestTask1UseRegular(unittest.TestCase):
    def test_from_task(self):
        self.assertEqual(task1_use_regular('esdfd((esdf)(esdf'), 'esdfd((esdf)')

    def test_empty(self):
        self.assertEqual(task1_use_regular(''), '')

    def test_t1(self):
        self.assertEqual(task1_use_regular('('), '')

    def test_t2(self):
        self.assertEqual(task1_use_regular('(()'), '(()')

    def test_t3(self):
        self.assertEqual(task1_use_regular('()'), '()')

    def test_t4(self):
        self.assertEqual(task1_use_regular('()))'), '()))')

    def test_t5(self):
        self.assertEqual(task1_use_regular('(a)b)c)d(e(f(g)h(i(j(k'), '(a)b)c)d(e(f(g)h')

    def test_t6(self):
        self.assertEqual(task1_use_regular('(((z)(a(b(c'), '(((z)')


class TestTask1UseForeach(unittest.TestCase):
    def test_from_task(self):
        self.assertEqual(task1_use_foreach('esdfd((esdf)(esdf'), 'esdfd((esdf)')

    def test_empty(self):
        self.assertEqual(task1_use_foreach(''), '')

    def test_t1(self):
        self.assertEqual(task1_use_foreach('('), '')

    def test_t2(self):
        self.assertEqual(task1_use_foreach('(()'), '(()')

    def test_t3(self):
        self.assertEqual(task1_use_foreach('()'), '()')

    def test_t4(self):
        self.assertEqual(task1_use_foreach('()))'), '()))')

    def test_t5(self):
        self.assertEqual(task1_use_foreach('(a)b)c)d(e(f(g)h(i(j(k'), '(a)b)c)d(e(f(g)h')

    def test_t6(self):
        self.assertEqual(task1_use_foreach('(((z)(a(b(c'), '(((z)')


if __name__ == '__main__':
    unittest.main()
