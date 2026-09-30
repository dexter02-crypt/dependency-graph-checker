import unittest
from core import analyze,dot
class Tests(unittest.TestCase):
    def test_order(self):
        r=analyze({'app':['db'],'db':[]}); self.assertLess(r['order'].index('db'),r['order'].index('app'))
    def test_cycle(self): self.assertTrue(analyze({'a':['b'],'b':['a']})['cycle'])
    def test_missing(self):
        with self.assertRaises(ValueError): analyze({'a':['x']})
    def test_depth(self): self.assertEqual(analyze({'a':['b'],'b':['c'],'c':[]})['max_depth'],2)
    def test_dot(self): self.assertIn('"db" -> "app"',dot({'app':['db'],'db':[]}))
