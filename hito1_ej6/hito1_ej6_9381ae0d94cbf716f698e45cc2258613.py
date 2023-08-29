#Ordenar tres números
w = int(input("ingrese un numero"))
x = int(input("ingrese un numero"))
y = int(input("ingrese un numero"))
mi_lista =[w, x, y]
mi_lista_ordenada = sorted(mi_lista)
print(*(mi_lista_ordenada),sep=',')