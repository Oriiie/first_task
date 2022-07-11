import unittest


def numeration(word: str) -> str:
    result_string = []

    for i in range(len(word)):
        if not result_string:
            result_string.append(word[i])
            result_string.append(1)
            continue
        if word and result_string:
            if result_string[len(result_string) - 2] == word[i]:
                result_string[len(result_string) - 1] += 1
            else:
                result_string.append(word[i])
                result_string.append(1)

    if len("".join([str(i) for i in result_string])) > len(word):
        return word

    return "".join([str(i) for i in result_string])


class TestSum(unittest.TestCase):

    def test_usual(self):
        self.assertEqual(numeration('hello'), 'hello')

    def test_multiple_nums(self):
        self.assertEqual(numeration('aaaaaaaaaaaa'), 'a12')

    def test_standart(self):
        self.assertEqual(numeration('aaaabbbb'), 'a4b4')


unittest.main()

