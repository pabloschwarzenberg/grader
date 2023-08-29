def rot13(palabra):
    
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    string = ''
    for i in palabra:
        if i in alfabeto:
            if alfabeto.index(i) < 13:
                string=string+alfabeto[alfabeto.index(i) + 13]
            else:
                string=string+alfabeto[alfabeto.index(i) - 13]
        elif i in alfabeto.upper():
            if alfabeto.upper.index(i) < 13:
                string=string+alfabeto.upper()[alfabeto.upper().index(i) + 13]
            else:
                string=string+alfabeto.upper()[alfabeto.upper().index(i) - 13]
        else:
            string += 1
    return string

a = rot13("hito")
print(a)