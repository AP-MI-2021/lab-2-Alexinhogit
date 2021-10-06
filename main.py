from antipalindrom import is_antipalindrome
from base16from2 import get_base_16_from_2
from palindrom import is_palindrome

def main():
    option = "?"
    while True:
        print("Ce functie doriti sa folositi?")
        print("(1) - Verificati daca un numar este antipalindrom.")
        print("(2) - Transformati un numar din baza 2 in baza 16.")
        print("(3) - Verificati daca un numar este palindrom.")
        print("(x) - Opriti aplicatia")
        option = input()

        if option == "1":
            numar = int(input("Ce numar doresti sa verifici? "))
            if is_antipalindrome(numar):
                print(numar, "este antipalindrom.")
            else:
                print(numar, "nu este antipalindrom.")
        elif option == "2":
            numar = input("Ce numar doresti sa fie transformat? ")
            if get_base_16_from_2(numar):
                print(f"Numarul in baza 2: {numar} convertit in baza 16 este: {get_base_16_from_2(numar)}")
        elif option == "3":
            numar = int(input("Ce numar doresti sa verifici? "))
            if is_palindrome(numar):
                print(numar, "este palindrom.")
            else:
                print(numar, "nu este palindrom.")
        else:
            break


if __name__ == "__main__":
    main()
