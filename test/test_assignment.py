import unittest

from app.service.assignment_service import Assignment, INSERTED, APPENDED

assignment = Assignment()


class MyTestCase(unittest.TestCase):

    def test_case1(self):
        data = {
            "poolId": 123546,
            "poolValues": [1, 2, 6, 7]
        }
        self.assertEqual(assignment.add_pool(data), INSERTED)

    def test_case2(self):
        data = {
            "poolId": 123546,
            "percentile": 50
        }
        self.assertEqual(assignment.query(data), (4, 4))

    def test_case3(self):
        data = {
            "poolId": 123546,
            "poolValues": [3, 4, 5]
        }
        self.assertEqual(assignment.add_pool(data), APPENDED)

    def test_case4(self):
        data = {
            "poolId": 654321,
            "poolValues": [3, 4, 5]
        }
        self.assertEqual(assignment.add_pool(data), INSERTED)

    def test_case5(self):
        data = {
            "poolId": 123546,
            "percentile": 50
        }
        self.assertEqual(assignment.query(data), (4, 7))


if __name__ == '__main__':
    unittest.main()
