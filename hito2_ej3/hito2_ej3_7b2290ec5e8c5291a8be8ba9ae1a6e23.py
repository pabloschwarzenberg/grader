genoma= input("Ingrese la secuencia del genoma: " )
n=int(input("Ingrese un número entero: "))

lista_genoma=[]
lista_genoma.append(genoma)
lista_genoma.append(n)

if len(lista_genoma[0]) == 6:
    print(lista_genoma, "[cga,gac]")

else:
    print(lista_genoma, "[ninguna]")