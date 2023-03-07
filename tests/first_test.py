import  pytest
from  app.calculator import Calculator
class TestCalc:
    def setup(self):
        self.calc = Calculator
    def test_multiply_calculator_correctly(self):
        assert self.calc.multiply(self, 10, 2) == 20

    def test_division_calculator_correctly(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction_calculator_correctly(self):
        assert self.calc.subtraction(self, 10, 2) == 8

    def test_adding_calculator_correctly(self):
        assert self.calc.adding(self, 10, 2) == 12