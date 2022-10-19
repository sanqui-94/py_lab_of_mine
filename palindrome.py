import unittest

def digits(x):
    """Convert an integer into a list of digits.

    Args:
        x: The number whose digits we want.

    Returns: A list of the digits, in order, of ``x``.
    """
    digs = []
    while x != 0:
        div, mod = divmod(x, 10)
        digs.append(mod)
        x = div
    return digs

def is_palindrome(x):
    """Determine if an integer is palindrome.

    Args:
        x: The number to check for palindromicity.

    Returns: True if the digits of ``x`` are a palindrome, False otherwise.
    """
    digs = digits(x)
    for f, r in zip(digs, reversed(digs)):
        if f != r:
            return False
    return True


class Tests(unittest.TestCase):
    """Tests for the ``is_palindrome()`` function."""
    def test_negative(self):
        """Check that it returns false correctly."""
        self.assertFalse(is_palindrome(1234))

    def test_positive(self):
        """Check that it returns true correctly."""
        self.assertTrue(is_palindrome(1234321))

    def test_single_digits(self):
        """Check that it works for single digit numbers."""
        for i in range(10):
            self.assertTrue(is_palindrome(i))


if __name__ == '__main__':
    unittest.main()