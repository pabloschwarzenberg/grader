#Descomponer un número

numero = list(input("Ingresa un numero de hasta 4 dígitos: "))

def frase(cant, num, unid):
    frase = ""
    for index in range(cant):
        frase = frase + num[index] + unid[index]

    print(frase)

def unidades_pop(cant):
    unidades = ["M + ", "C + ", "D + ", "U"]

    for a in range(cant):
        unidades.pop(0)


    
    return unidades

if len(numero) == 4:
    unidades = unidades_pop(0)
    num_desc = frase(4, numero, unidades)
elif len(numero) == 3:
    unidades = unidades_pop(1)
    num_desc = frase(3, numero, unidades)
elif len(numero) == 2:
    unidades = unidades_pop(2)
    num_desc = frase(2, numero, unidades)
else:
    unidades = unidades_pop(3)
    num_desc = frase(1, numero, unidades)