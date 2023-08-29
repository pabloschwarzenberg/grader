def buscarTodas(frase, letra):
    seguimiento = -1
    strvacio = ""
    separador = " "
    for i in frase:
        seguimiento += 1
        if letra in i:
            strvacio += str(seguimiento)
            strvacio += separador
    return strvacio[:-1]

if __name__=="__main__":
    input1 = input("Ingrese palabra/frase:")
    input2 = input("Ingrese letra:")
    x = buscarTodas(input1, input2)
    print(x)

