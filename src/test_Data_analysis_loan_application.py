import unittest
from Data_analysis_loan_application import connect_to_database

class MyTestClass(unittest.TestCase):
    def test_connect_to_database(self):
        # Test case 1: Valid connection
        engine = connect_to_database()
        self.assertIsNotNone(engine)               

        print("All test cases pass")

if __name__ == '__main__':
    unittest.main()