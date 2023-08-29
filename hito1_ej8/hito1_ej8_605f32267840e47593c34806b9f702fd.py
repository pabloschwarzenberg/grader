#Descomponer un número
numero = int(input("Ingrese un numero de hasta 4 digitos: "))
strNumero = str(numero)
lista = list(strNumero)
digitos = len(lista)

if digitos == 1:
    listaUnidades = ["U"]
    descomposicion = lista[0] + listaUnidades[0] 
elif digitos == 2:
    listaUnidades = ["D","U"]
    descomposicion = lista[0] + listaUnidades[0]
    descomposicion = descomposicion + "+" + lista[1] + listaUnidades[1]
elif digitos == 3:
    listaUnidades = ["C","D","U"]
    descomposicion = lista[0] + listaUnidades[0]
    descomposicion = descomposicion + "+" + lista[1] + listaUnidades[1]
    descomposicion = descomposicion + "+" + lista[2] + listaUnidades[2]
elif digitos == 4:
    listaUnidades = ["M","C","D","U"]
    descomposicion = lista[0] + listaUnidades[0]
    descomposicion = descomposicion + "+" + lista[1] + listaUnidades[1]
    descomposicion = descomposicion + "+" + lista[2] + listaUnidades[2]
    descomposicion = descomposicion + "+" + lista[3] + listaUnidades[3]


print(descomposicion)