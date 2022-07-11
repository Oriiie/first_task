import unittest


def equals(first: str, second: str) -> bool:
    left = [i for i in first]
    right = [i for i in second]
    left.sort()
    right.sort()
    return left == right


class TestSum(unittest.TestCase):

    def test_usual(self):
        self.assertEqual(equals('hello', 'olleh'), True, "Палиндром")

    def test_capital_letter(self):
        self.assertEqual(equals('apple', 'Apple'), False, "Не палиндром")

    def test_spaces(self):
        self.assertEqual(equals('hello friend', 'hellofriend'), False, "Не палиндром")

    def test_fullrandom(self):
        self.assertEqual(equals('abcdqwer', 'qdwcebra'), True, "Палиндром")


unittest.main()

