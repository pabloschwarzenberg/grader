def jerigonzo(string):
    return string

if __name__ == "__main__":
    pass
def jerigonzo(string):
    vowels = 'aeiouAEIOU'
    result = ""
    for char in string:
        if char in vowels:
            result += char + 'p' + char
        else:
            result += char
    return result

if __name__ == "__main__":
    text = input("Introduce un texto: ")
    print("Texto en jerigonzo: ", jerigonzo(text))
         