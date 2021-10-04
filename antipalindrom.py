def is_antipalindrome(n) -> bool:

    n = str(n)

    for i in range(len(n)//2):
        if n[i] == n[-i-1]:
            return False

    return True


def test_is_antipalindrome():

    assert is_antipalindrome(2783) == True
    assert is_antipalindrome(2773) == False
    assert is_antipalindrome(2222) == True
    assert is_antipalindrome(1232) == True
    assert is_antipalindrome(77779) == False

test_is_antipalindrome()
