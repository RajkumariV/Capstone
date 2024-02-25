import unittest
from creditcard_and_loan_application_etl import format_phone_number
class MyTestClass(unittest.TestCase):
    def test_format_phone_number(self):  # Add parentheses after the method name
        # Test case 1: Valid phone number
        phone_number = "1234567890"
        expected_output = "(123) 456-7890"
        assert format_phone_number(phone_number) == expected_output

        # Test case 2: Phone number with leading zeros
        phone_number = "0012345678"
        expected_output = "(001) 234-5678"
        assert format_phone_number(phone_number) == expected_output                

        # Test case 3: None phone number
        phone_number = None
        expected_output = None
        assert format_phone_number(phone_number) == expected_output

        print("All test cases pass")

if __name__ == '__main__':
    unittest.main()
