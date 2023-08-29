def rot13(palabra):
    lista = []
    palabra_encriptada = ""

    for a in palabra:
        if a in lparte_1:
            for n in range(0, len(lparte_1)):
                if a == lparte_1[n]:
                    palabra_encriptada += lparte_2[n]
        else:
            for j in range(0, len(lparte_2)):
                if a == lparte_2[j]:
                    palabra_encriptada += lparte_1[j]

    return palabra_encriptada
            
    pass

parte_1 = "abcdefghijklm"
parte_2 = "nopqrstuvwxyz"
lparte_1 = []
lparte_2 = []


for a in parte_1:
    lparte_1.append(a)
for n in parte_2:
    lparte_2.append(n)



if __name__=="__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()

    resultado = rot13(palabra)
    
    print("El resultado es: ", resultado)
           