from unittest import TestCase
from Four_Squares import *
from kivy.tests import *
from kivy.tests.test_uix_gridlayout import GridLayoutTest
from kivy.tests.test_uix_widget import UIXWidgetTestCase
from kivy.tests.test_uix_boxlayout import UIXBoxLayoutTestcase


class test_fs(GridLayoutTest):
    def setUp(self) -> None:
        self.fs = Four_Sqaures()


if __name__ == '__main__':
    import unittest
    unittest.main()
