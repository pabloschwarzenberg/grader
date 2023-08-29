def rot13(palabra):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string = ''
    for i in palabra:
        if i in alphabet:
            if alphabet.index(i) < 13:
                string += alphabet[alphabet.index(i) + 13]
            else:
                string += alphabet[alphabet.index(i) - 13]
        elif i in alphabet.upper():
            if alphabet.upper.index(i) < 13:
                string += alphabet.upper()[alphabet.upper().index(i) + 13]
            else:
                string += alphabet.upper()[alphabet.upper().index(i) - 13]
        else:
            string += 1
    return string

a = rot13("hola")
print(a)

           