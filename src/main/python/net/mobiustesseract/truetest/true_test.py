

class TrueTest():
    def negate(self, value: bool) -> bool:
        return not value

    def _and(self, *args: bool) -> bool:
        return all(args)

    def reverse(self, string: str) -> str:
        return string[::-1]
