def rot13(palabra):
    letras_1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    letras_2 = ["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    resultado = []
    for i in palabra:
        if i == letras_1[0]:
            resultado.append(letras_2[0])
        
        if i == letras_1[1]:
            resultado.append(letras_2[1])

        if i == letras_1[2]:
            resultado.append(letras_2[2])

        if i == letras_1[3]:
            resultado.append(letras_2[3])

        if i == letras_1[4]:
            resultado.append(letras_2[4])

        if i == letras_1[5]:
            resultado.append(letras_2[5])

        if i == letras_1[6]:
            resultado.append(letras_2[6])

        if i == letras_1[7]:
            resultado.append(letras_2[7])

        if i == letras_1[8]:
            resultado.append(letras_2[8])

        if i == letras_1[9]:
            resultado.append(letras_2[9])
        
        if i == letras_1[10]:
            resultado.append(letras_2[10])

        if i == letras_1[11]:
            resultado.append(letras_2[11])

        if i == letras_1[12]:
            resultado.append(letras_2[12])

        if i == letras_2[0]:
            resultado.append(letras_1[0])

        if i == letras_2[1]:
            resultado.append(letras_1[1])

        if i == letras_2[2]:
            resultado.append(letras_1[2])

        if i == letras_2[3]:
            resultado.append(letras_1[3])

        if i == letras_2[4]:
            resultado.append(letras_1[4])

        if i == letras_2[5]:
            resultado.append(letras_1[5])

        if i == letras_2[6]:
            resultado.append(letras_1[6])

        if i == letras_2[7]:
            resultado.append(letras_1[7])

        if i == letras_2[8]:
            resultado.append(letras_1[8])

        if i == letras_2[9]:
            resultado.append(letras_1[9])
        
        if i == letras_2[10]:
            resultado.append(letras_1[10])

        if i == letras_2[11]:
            resultado.append(letras_1[11])

        if i == letras_2[12]:
            resultado.append(letras_1[12])
    resultado_1 = "".join(resultado)
    return resultado_1

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           