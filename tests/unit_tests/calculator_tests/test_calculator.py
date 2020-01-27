from api.common.util import calculator
from tests.base import BaseTestCase


class AnotherTestSuite(BaseTestCase):
    def test_calculator(self):
        res = calculator(2, 4)
        self.assertEqual(res, 6)
