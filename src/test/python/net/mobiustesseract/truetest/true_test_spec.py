from hypothesis import given, settings
from hypothesis.strategies import text
from itertools import permutations
from nimoy.specification import Specification
from random import randint, choices
import string

from net.mobiustesseract.truetest import TrueTest


class TrueTestSpec(Specification):
    def __init__(self, *args):
        super().__init__(*args)
        self.true_test = TrueTest()

    # spec example using a data table
    def should_negate_parameter(self, parameter):
        with when:
            result = self.true_test.negate(parameter)
        with then:
            result == expected
        with where:
            parameter   |   expected
            True        |   False
            False       |   True

    # spec example using list of random properies 
    def should_reverse_parameter(self, parameter):
        
        with expect:
            self.true_test.reverse(parameter) == parameter[::-1]

        with where:
                parameter = [''.join(choices(string.ascii_letters, k=randint(1, 100))) for i in range(10)]

    # spec example using hypothesis
    @given(parameter=text(alphabet=string.ascii_letters,min_size=1,max_size=100))
    @settings(max_examples=10)
    def should_reverse_parameter_hypothesis_style(self, parameter):
        
        with expect:
            self.true_test.reverse(parameter) == parameter[::-1]

    def should_and_parameters(self, parameters):

        with expect:
            self.true_test._and(*parameters) == True

        with where:
            parameters = [[True] * randint(2, 10)]

    # spec example with permutations
    def should_not_and_parameters(self, parameters):

        with expect:
            self.true_test._and(*parameters) == False

        with where:
            parameters = permutations([True] * randint(1, 9) + [False])
