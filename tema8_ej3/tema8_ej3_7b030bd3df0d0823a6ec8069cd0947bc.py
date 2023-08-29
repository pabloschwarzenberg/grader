def estadisticas_frase(frase):
    lista = frase.strip()
    lista = list(lista)
    lista2 = []
    lista3 = []
    lista4 = []
    global contador
    global contador2
    global contador3
    global contador4
    global contador5
    contador = 0
    contador2 = 0
    contador3 = 0
    contador4 = 0
    contador5 = 0    
    for i in range(len(lista)):
        if((" " == lista[i] or "\n" == lista[i] or "." == lista[i]) and contador == 1):
            lista2.append("$")
            contador = 0
        elif(" " != lista[i] and "\n" != lista[i] and "." != lista[i]):
            lista2.append(lista[i])
            contador = 1
    for j in range(len(lista2)):
        if("$" == lista2[j]):
           contador = contador + 1
    
    for k in range(len(lista)):
        if("\n" != lista[k] and "." != lista[k] and " " != lista[k]):
            lista3.append(lista[k])
            contador2 = contador2 + 1
        elif("." == lista[k]):
            contador5 = contador5 + 1
    n_t_caracteres = len(frase)
    largo_promedio = contador2 / contador
    for l in range(len(lista)):
        if("\n" == lista[l] and contador3 == 1):
            lista4.append(" ")
            lista4.append("#")
            contador3 = 0
        elif("\n" != lista[l] and "." != lista[l]):
            lista4.append(lista[l])
            contador3 = 1
    for m in range(len(lista4)):
        if(" " == lista4[m]):
           contador4 = contador4 + 1
        elif("#" == lista4[m]):
            contador4 = contador4 - 1
    return contador,n_t_caracteres,largo_promedio,contador4,contador5
    
if __name__ == "__main__":
    frase = input("Ingrese la frase: ")
    print(estadisticas_frase(hombre_imaginario))