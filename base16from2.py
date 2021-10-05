def get_base_16_from_2(n: str) -> str:
    """Functia transforma un numar dat din baza 2 in baza 16. Mai intai din baza 2 in 10 apoi din 10 in 16.

    :param n: Numarul in baza 2 care va fi transformat
    :return: Numarul in baza 16 dupa transformare
    """
    if n == '0':
        return n

    # prima transformare este din baza 2 in baza 10
    var = 0
    for i in range(len(n)):
        var += int(n[len(n) - i - 1]) * (2 ** i)

    # transformarea finala din baza 10 in baza 16
    new_n = ""
    base = 16
    digits = '0123456789ABCDEF'
    while var:
        new_n += digits[var % base]
        var //= 16

    return new_n[::-1]


def test_get_base_16_from_2():
    """Testeaza functia get_base_16_from_2
    """
    assert get_base_16_from_2("10101") == "15"
    assert get_base_16_from_2("1") == "1"
    assert get_base_16_from_2("00011") == "3"
    assert get_base_16_from_2("11111") == "1F"
    assert get_base_16_from_2("110111") == "37"
    assert get_base_16_from_2("1000111111") == "23F"


test_get_base_16_from_2()
