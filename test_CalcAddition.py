# ********RoostGPT********
"""
Test generated by RoostGPT for test pushTest using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=addition_9ccff787e3
ROOST_METHOD_SIG_HASH=addition_77ffd3333b

Scenario 1: Verify the addition of two positive numbers
Details:
  TestName: test_addition_positive_numbers
  Description: This test is intended to verify the addition of two positive numbers. 
Execution:
  Arrange: Initialize two positive numbers, num1 and num2.
  Act: Invoke the addition function with num1 and num2 as parameters.
  Assert: Verify that the result is the sum of num1 and num2.
Validation:
  This test is important to confirm that the function can correctly add two positive numbers, which is a basic requirement of the function's specifications.

Scenario 2: Verify the addition of two negative numbers
Details:
  TestName: test_addition_negative_numbers
  Description: This test is intended to verify the addition of two negative numbers.
Execution:
  Arrange: Initialize two negative numbers, num1 and num2.
  Act: Invoke the addition function with num1 and num2 as parameters.
  Assert: Verify that the result is the sum of num1 and num2.
Validation:
  This test is important to confirm that the function can correctly add two negative numbers, which is a basic requirement of the function's specifications.

Scenario 3: Verify the addition of a negative number and a positive number
Details:
  TestName: test_addition_negative_positive_numbers
  Description: This test is intended to verify the addition of a negative number and a positive number.
Execution:
  Arrange: Initialize a negative number as num1 and a positive number as num2.
  Act: Invoke the addition function with num1 and num2 as parameters.
  Assert: Verify that the result is the sum of num1 and num2.
Validation:
  This test is important to confirm that the function can correctly add a negative number and a positive number, which is a basic requirement of the function's specifications.

Scenario 4: Verify the addition of zero and a positive number
Details:
  TestName: test_addition_zero_positive_number
  Description: This test is intended to verify the addition of zero and a positive number.
Execution:
  Arrange: Initialize zero as num1 and a positive number as num2.
  Act: Invoke the addition function with num1 and num2 as parameters.
  Assert: Verify that the result is the same as num2.
Validation:
  This test is important to confirm that the function can correctly add zero and a positive number, which is a basic requirement of the function's specifications. 

Scenario 5: Verify the addition of zero and a negative number
Details:
  TestName: test_addition_zero_negative_number
  Description: This test is intended to verify the addition of zero and a negative number.
Execution:
  Arrange: Initialize zero as num1 and a negative number as num2.
  Act: Invoke the addition function with num1 and num2 as parameters.
  Assert: Verify that the result is the same as num2.
Validation:
  This test is important to confirm that the function can correctly add zero and a negative number, which is a basic requirement of the function's specifications.
"""

# ********RoostGPT********
import pytest
from calc import addition

class Test_CalcAddition:

    def test_addition_positive_numbers(self):
        # Arrange
        num1 = 10
        num2 = 20

        # Act
        result = addition(num1, num2)

        # Assert
        assert result == 30, "Addition of two positive numbers failed"

    def test_addition_negative_numbers(self):
        # Arrange
        num1 = -10
        num2 = -20

        # Act
        result = addition(num1, num2)

        # Assert
        assert result == -30, "Addition of two negative numbers failed"

    def test_addition_negative_positive_numbers(self):
        # Arrange
        num1 = -10
        num2 = 20

        # Act
        result = addition(num1, num2)

        # Assert
        assert result == 10, "Addition of a negative number and a positive number failed"

    def test_addition_zero_positive_number(self):
        # Arrange
        num1 = 0
        num2 = 20

        # Act
        result = addition(num1, num2)

        # Assert
        assert result == 20, "Addition of zero and a positive number failed"

    def test_addition_zero_negative_number(self):
        # Arrange
        num1 = 0
        num2 = -20

        # Act
        result = addition(num1, num2)

        # Assert
        assert result == -20, "Addition of zero and a negative number failed"
