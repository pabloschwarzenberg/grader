#Ordenar tres números
var1 = int(input())
var2 = int(input())
var3 = int(input())
lista = [var1, var2,var3]
lista_ordenada = sorted(lista)
print(*(lista_ordenada), sep=',')