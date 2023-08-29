#Descomponer un número
unidades = []
numeros=[]
numero = int(input("Ingrese un numero de hasta 4 digitos: "))
lista_numero = [int(a) for a in str(numero)]

for i in range(len(lista_numero)):
    numeros.append(str(lista_numero[i]))
    
if len(lista_numero) ==1:
    unidades =['U']
    print(numeros[0],"+",unidades[0])
elif len(lista_numero)==2:
    unidades=['D','U']
    print(numeros[0],unidades[0],"+",numeros[1],unidades[1])
elif len(lista_numero)==3:
    unidades=['C','D','U']
    print(numeros[0],unidades[0],"+",numeros[1],unidades[1],"+",numeros[2],unidades[2])
elif len(lista_numero)==4:
    unidades=['M','C','D','U']
    print(numeros[0],unidades[0],"+",numeros[1],unidades[1],"+",numeros[2],unidades[2],"+",numeros[3],unidades[3])