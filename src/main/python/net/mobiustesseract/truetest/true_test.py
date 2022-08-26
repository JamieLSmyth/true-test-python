

class TrueTest():
    def negate(self, value: bool) -> bool:
        return not value

    def _and(self, *bools: bool) -> bool:
        return all(b is True for b in bools)

    def reverse(self, string: str) -> str:
        reversed = [None] * len(string)

        x = len(reversed)
        for c in string:
            x -= 1
            reversed[x] = c

        return ''.join(reversed)
