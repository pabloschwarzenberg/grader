#Ordenar tres números
enteroUno=int(input("Ingrese el primer número entero:"))
enteroDos=int(input("Ingrese el segundo entero:"))
enteroTres=int(input("Ingrese el tercer número entero:"))
a=min(enteroUno,enteroDos,enteroTres)
b=max(enteroUno,enteroDos,enteroTres)
c=(enteroUno+enteroDos+enteroTres)-a-b

print("Los números ordenados de menor a mayor:",a,",",c,",",b)        