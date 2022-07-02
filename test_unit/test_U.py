<<<<<<< HEAD

=======
>>>>>>> 3688bfbd7b211582b05c22a0d0ec27307753374f
# -*- coding: UTF-8 -*-
import unittest
import os
import sys
root_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)

from app.xiangqi_app import xiang_qi


class test_app(unittest.TestCase):
    def setUp(self):
        print("开始")
    def test_ma(self):
        a = xiang_qi.ma(self)
        self.assertEqual(a,"马走日")
    def test_xiang(self):
        b = xiang_qi.xiang(self)
        self.assertEqual(b,"象走")
    def tearDown(self):
        print("结束")

if __name__ == '__main__':
    unittest.main()
