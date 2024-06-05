# ********RoostGPT********
"""
Test generated by RoostGPT for test pushTest using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=division_51255ed47d
ROOST_METHOD_SIG_HASH=division_eae366bb2d

Scenario 1: Test for a successful division operation
Details:
  TestName: test_successful_division_operation
  Description: This test is intended to verify that the division function returns the correct result when two valid numbers are passed and the second number is not zero.
Execution:
  Arrange: Initialize two variables with valid numbers, where the second number is not zero.
  Act: Invoke the division function with the two initialized variables.
  Assert: Check that the result matches the expected division result.
Validation:
  This test validates that the division function correctly handles valid inputs and returns the expected result. This is crucial for the function's correctness as per its specifications.

Scenario 2: Test for division by zero
Details:
  TestName: test_division_by_zero
  Description: This test is intended to verify that the division function correctly handles the scenario when the second number is zero.
Execution:
  Arrange: Initialize two variables, where the second variable is zero.
  Act: Invoke the division function with the two initialized variables.
  Assert: Check that the result is the string "Cannot divide by zero".
Validation:
  This test validates that the division function correctly handles the edge case where the denominator is zero. This is crucial for the function's correctness and robustness, as division by zero is undefined in mathematics and should be handled as an error case.

Scenario 3: Test for division of zero by a number
Details:
  TestName: test_division_of_zero_by_number
  Description: This test is intended to verify that the division function correctly handles the scenario when the first number is zero.
Execution:
  Arrange: Initialize two variables, where the first variable is zero.
  Act: Invoke the division function with the two initialized variables.
  Assert: Check that the result is zero.
Validation:
  This test validates that the division function correctly handles the edge case where the numerator is zero. This is crucial for the function's correctness, as zero divided by any number should always be zero.

Scenario 4: Test for division of a negative number
Details:
  TestName: test_division_of_negative_number
  Description: This test is intended to verify that the division function correctly handles the scenario when one or both of the numbers are negative.
Execution:
  Arrange: Initialize two variables, where at least one variable is a negative number.
  Act: Invoke the division function with the two initialized variables.
  Assert: Check that the result matches the expected division result.
Validation:
  This test validates that the division function correctly handles scenarios with negative numbers. This is crucial for the function's correctness, as division should work correctly with negative numbers according to mathematical rules.
"""

# ********RoostGPT********
import pytest
from calc import division

class Test_Division:

    @pytest.mark.regression
    @pytest.mark.positive
    def test_successful_division_operation(self):
        num1 = 10
        num2 = 2
        result = division(num1, num2)
        assert result == 5, "Test failed: Expected 5 but got {}".format(result)

    @pytest.mark.regression
    @pytest.mark.negative
    def test_division_by_zero(self):
        num1 = 10
        num2 = 0
        result = division(num1, num2)
        assert result == "Cannot divide by zero", "Test failed: Expected 'Cannot divide by zero' but got {}".format(result)

    @pytest.mark.regression
    @pytest.mark.positive
    def test_division_of_zero_by_number(self):
        num1 = 0
        num2 = 10
        result = division(num1, num2)
        assert result == 0, "Test failed: Expected 0 but got {}".format(result)

    @pytest.mark.regression
    @pytest.mark.positive
    def test_division_of_negative_number(self):
        num1 = -10
        num2 = 2
        result = division(num1, num2)
        assert result == -5, "Test failed: Expected -5 but got {}".format(result)
