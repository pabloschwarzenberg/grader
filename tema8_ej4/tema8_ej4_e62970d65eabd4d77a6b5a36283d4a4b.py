x = "abcdefghijklmnopqrstuvwxyz"
y = "nopqrstuvwxyzabcdefghijklm"
abc_original = []
abc_truco = []

for i in x:
    abc_original.append(i)

for i in y:
    abc_truco.append(i)

def rot13(palabra):
    encriptar = []
    for i in palabra:
        encriptar.append(i)
    x = ""            
    for i in range (0,len(encriptar)):
        x += abc_truco[abc_original.index(encriptar[i])]
                    
    return x