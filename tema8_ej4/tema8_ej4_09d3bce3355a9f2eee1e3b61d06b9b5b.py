def rot13(palabra):
    lower_letters = [chr(x) for x in range(97, 123)]
    upper_letters = [chr(x) for x in range(65, 91)]
    sourceString = palabra
    resultString = ""
    for char in sourceString:
        if char.isupper():
            resultString += encrypt(char, upper_letters)
        elif char.islower():
            resultString += encrypt(char, lower_letters)
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

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           