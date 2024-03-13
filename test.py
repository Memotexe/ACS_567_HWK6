# Chase Walters
import unittest
from HW6 import CSTV
from HW6 import CSTEHC

class UnitTestCases(unittest.TestCase):
    def test_average_for_CSTV(self):
        result = CSTV(1250)
        self.assertEqual(result, 208.33333333333334)

    def testing_total_effort_valuesLandH_for_CSTEHC(self):
        result = CSTEHC()
        self.assertEqual(result, "Teams Total Effort Hours Range: 140-197")

