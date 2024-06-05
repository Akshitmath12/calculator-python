# ********RoostGPT********
"""
Test generated by RoostGPT for test pushTest using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=calculator_32e48fed51
ROOST_METHOD_SIG_HASH=calculator_ad84dc0779

```
Scenario 1: Test calculator function with addition operation
Details:
  TestName: test_calculator_addition
  Description: This test is intended to verify the addition operation of the calculator function.
Execution:
  Arrange: Initialize two numbers num1 and num2 and operation as '+'.
  Act: Invoke the calculator function with num1, num2 and operation as parameters.
  Assert: Check if the returned value is the sum of num1 and num2.
Validation:
  This test is important to ensure that the calculator function correctly performs addition operation as per the business requirements.

Scenario 2: Test calculator function with subtraction operation
Details:
  TestName: test_calculator_subtraction
  Description: This test is intended to verify the subtraction operation of the calculator function.
Execution:
  Arrange: Initialize two numbers num1 and num2 and operation as '-'.
  Act: Invoke the calculator function with num1, num2 and operation as parameters.
  Assert: Check if the returned value is the difference of num1 and num2.
Validation:
  This test is important to ensure that the calculator function correctly performs subtraction operation as per the business requirements.

Scenario 3: Test calculator function with multiplication operation
Details:
  TestName: test_calculator_multiplication
  Description: This test is intended to verify the multiplication operation of the calculator function.
Execution:
  Arrange: Initialize two numbers num1 and num2 and operation as '*'.
  Act: Invoke the calculator function with num1, num2 and operation as parameters.
  Assert: Check if the returned value is the product of num1 and num2.
Validation:
  This test is important to ensure that the calculator function correctly performs multiplication operation as per the business requirements.

Scenario 4: Test calculator function with division operation
Details:
  TestName: test_calculator_division
  Description: This test is intended to verify the division operation of the calculator function.
Execution:
  Arrange: Initialize two numbers num1 and num2 and operation as '/'.
  Act: Invoke the calculator function with num1, num2 and operation as parameters.
  Assert: Check if the returned value is the quotient of num1 and num2.
Validation:
  This test is important to ensure that the calculator function correctly performs division operation as per the business requirements.

Scenario 5: Test calculator function with invalid operation
Details:
  TestName: test_calculator_invalid_operation
  Description: This test is intended to verify the behavior of the calculator function when an invalid operation is provided.
Execution:
  Arrange: Initialize two numbers num1 and num2 and operation as a string that is not '+', '-', '*' or '/'.
  Act: Invoke the calculator function with num1, num2 and operation as parameters.
  Assert: Check if the returned value is "Invalid operation".
Validation:
  This test is important to ensure that the calculator function correctly handles invalid operations as per the business requirements.
```
"""

# ********RoostGPT********
import pytest
from calc import calculator

class Test_Calculator:

    @pytest.mark.regression
    def test_calculator_addition(self):
        # Arrange
        num1, num2 = 10, 20
        operation = '+'

        # Act
        result = calculator(num1, num2, operation)

        # Assert
        assert result == 30, "Addition operation failed"

    @pytest.mark.regression
    def test_calculator_subtraction(self):
        # Arrange
        num1, num2 = 20, 10
        operation = '-'

        # Act
        result = calculator(num1, num2, operation)

        # Assert
        assert result == 10, "Subtraction operation failed"

    @pytest.mark.regression
    def test_calculator_multiplication(self):
        # Arrange
        num1, num2 = 10, 20
        operation = '*'

        # Act
        result = calculator(num1, num2, operation)

        # Assert
        assert result == 200, "Multiplication operation failed"

    @pytest.mark.regression
    def test_calculator_division(self):
        # Arrange
        num1, num2 = 20, 10
        operation = '/'

        # Act
        result = calculator(num1, num2, operation)

        # Assert
        assert result == 2, "Division operation failed"

    @pytest.mark.negative
    def test_calculator_invalid_operation(self):
        # Arrange
        num1, num2 = 10, 20
        operation = 'invalid'

        # Act
        result = calculator(num1, num2, operation)

        # Assert
        assert result == "Invalid operation", "Invalid operation handling failed"