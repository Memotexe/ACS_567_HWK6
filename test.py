# Chase Walters
import unittest
from HW6 import CSTV
from HW6 import CSTEHC


class UnitTestCases(unittest.TestCase):

    def test_exception(self):
        with self.assertRaises(TypeError):
            CSTV(1250.1)

    def test_averageForCSTV(self):
        result = CSTV(1250)
        self.assertEqual(result, 208.33333333333334)

    def test_totalEffortValuesLandHforCSTEHC(self):
        result = CSTEHC()
        self.assertEqual(result, "Teams Total Effort Hours Range: 140-197")

# ACCEPTANCE TESTS SHOULD BE WRITTEN NOT CODED!
