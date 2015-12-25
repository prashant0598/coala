import sys
import unittest

sys.path.insert(0, ".")
from bears.tests.BearTestHelper import generate_skip_test
from bears.tests.LocalBearTestHelper import generate_local_bear_test
from bears.natural_language.MarkdownBear import MarkdownBear


MarkdownBearTest = generate_local_bear_test(
    MarkdownBear,
    (["```\n", "some code\n", "```\n"],),
    (['    some code'],))


skip_test = generate_skip_test(MarkdownBear)


if __name__ == '__main__':
    unittest.main(verbosity=2)
