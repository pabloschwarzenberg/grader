def rot13(palabra):
    LOWER_LETTERS = [chr(x) for x in range(97, 123)]
    UPPER_LETTERS = [chr(x) for x in range(65, 91)]
    sourceString = palabra
    resultString = ""
    for char in sourceString:
        if char.isupper():
            resultString += encrypt(char, UPPER_LETTERS)
        elif char.islower():
            resultString += encrypt(char, LOWER_LETTERS)
        else:
            resultString += char
    return resultString

def encrypt(char, letterList):
    resultchar = ''
    originalIndex = letterList.index(char)
    newIndex = originalIndex + 13
    resultchar += letterList[newIndex % len(letterList)]
    return resultchar
    pass

