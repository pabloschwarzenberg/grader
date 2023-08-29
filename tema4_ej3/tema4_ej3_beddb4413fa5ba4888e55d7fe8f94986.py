def jerigonzo(string):
    vowels = "aeiouáéíóúü"
    vowels += vowels.upper()
    string = "".join([c+"p"+c if c in vowels else c for c in string])
    return string

if __name__ == "__main__":
    pass
         