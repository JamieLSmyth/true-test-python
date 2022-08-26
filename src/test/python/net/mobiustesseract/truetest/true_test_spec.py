from nimoy.specification import Specification
from net.mobiustesseract.truetest import TrueTest
from random import randint, choices
from itertools import permutations
import string

class TrueTestSpec(Specification):
    def __init__(self, *args):
        super().__init__(*args)
        self.true_test = TrueTest()

    def should_negate_parameter(self, parameter):
        with when:
            result = self.true_test.negate(parameter)
        with then:
            result == expected
        with where:
            parameter   |   expected
            True        |   False
            False       |   True

    def should_reverse_parameter(self, parameter):

        with expect:
            self.true_test.reverse(parameter) == parameter[::-1]

        with where:
            parameter = [str(''.join(choices(string.ascii_letters, k = randint(1, 100))))]

    def should_and_parameters(self, parameters):

        with expect:
            self.true_test._and(*parameters) == True

        with where:
            parameters = [[True] * randint(2, 10)]



    def should_not_and_parameters(self, parameters):

        with expect:
            self.true_test._and(*parameters) == False

        with where:
            parameters = permutations([True] * randint(1, 9) + [False])
