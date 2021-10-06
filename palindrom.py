def is_palindrome(n) -> bool:
    """Verifica daca un numar este palindrom.

    :param n: Numarul ce va fi verificat.
    :return: Daca este sau nu palindrom
    """

    return str(n) == str(n)[::-1]


def test_is_palindrome():
    """Verifica functia is_palindrome
    """

    assert is_palindrome("12345") == False
    assert is_palindrome("10101") == True
    assert is_palindrome("1") == True
    assert is_palindrome("421525") == False
    assert is_palindrome("555555") == True


test_is_palindrome()
