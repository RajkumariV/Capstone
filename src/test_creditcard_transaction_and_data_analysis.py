import unittest
from Creditcard_transaction_and_Data_analysis import is_valid_date,validate_ssn,validate_credit_card_number

class MyTestClass(unittest.TestCase):
    def test_validate_credit_card_number(self):
        # Test case 1: Valid credit card number
        card_number = "1234567890123456"
        self.assertTrue(validate_credit_card_number(card_number))

        # Test case 2: Invalid credit card number (less than 16 digits)
        card_number = "12345678901234"
        self.assertFalse(validate_credit_card_number(card_number))

        # Test case 3: Invalid credit card number (more than 16 digits)
        card_number = "12345678901234567890"
        self.assertFalse(validate_credit_card_number(card_number))

        # Test case 4: Invalid credit card number (contains non-numeric characters)
        card_number = "1234567890a23456"
        self.assertFalse(validate_credit_card_number(card_number))

        # Test case 5: Invalid credit card number (empty string)
        card_number = ""
        self.assertFalse(validate_credit_card_number(card_number))

        print("All test cases pass")

    def test_validate_ssn(self):
        # Test case 1: Valid SSN
        ssn = "123456789"
        self.assertTrue(validate_ssn(ssn))

        # Test case 2: Invalid SSN (less than 9 digits)
        ssn = "12345678"
        self.assertFalse(validate_ssn(ssn))       

        # Test case 3: Invalid SSN (contains non-numeric characters)
        ssn = "12345678a"
        self.assertFalse(validate_ssn(ssn))

        # Test case 4: Invalid SSN (empty string)
        ssn = ""
        self.assertFalse(validate_ssn(ssn))

        print("All test cases pass")

    def test_is_valid_date(self):
        # Test case 1: Valid date
        date_string = "2022-12-31"
        self.assertTrue(is_valid_date(date_string))

        # Test case 2: Invalid date (day exceeds maximum)
        date_string = "2022-02-30"
        self.assertFalse(is_valid_date(date_string))

        # Test case 3: Invalid date (month exceeds maximum)
        date_string = "2022-13-01"
        self.assertFalse(is_valid_date(date_string))

        # Test case 4: Invalid date (year is not a leap year)
        date_string = "2021-02-29"
        self.assertFalse(is_valid_date(date_string))

        # Test case 5: Invalid date (invalid format)
        date_string = "2022/12/31"
        self.assertFalse(is_valid_date(date_string))

        # Test case 6: Invalid date (empty string)
        date_string = ""
        self.assertFalse(is_valid_date(date_string))

        # Test case 7: Invalid date (non-numeric characters)
        date_string = "2022-12-3a"
        self.assertFalse(is_valid_date(date_string))

        print("All test cases pass")

if __name__ == '__main__':
    unittest.main()