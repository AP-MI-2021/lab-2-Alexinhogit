def is_antipalindrome(n) -> bool:
    """ Verifica daca un numar este antipalindrom(daca oricare 2 cifre egal departate de extremitati sunt diferite).

    :param n: Numarul ce va fi verificat
    :return: Daca este sau nu antipalindrom
    """

    n = str(n)

    for i in range(len(n)//2):
        if n[i] == n[-i-1]:
            return False

    return True


def test_is_antipalindrome():
    """Verifica is_antipalindrome
    """

    assert is_antipalindrome(2783) == True
    assert is_antipalindrome(2773) == False
    assert is_antipalindrome(2222) == False
    assert is_antipalindrome(1232) == True
    assert is_antipalindrome(77779) == False
    assert is_antipalindrome(3) == True


test_is_antipalindrome()
