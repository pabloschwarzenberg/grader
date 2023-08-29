#Ordenar tres números
print("Ingrese el primer número: ")
n1=int(input())

print("Ingrese el segundo número: ")
n2=int(input())

print("Ingrese el terecer número: ")
n3=int(input())
#ordenamos los datos
def ordeN(n1,n2,n3):
    numeros=[n1,n2,n3]
    numeros.sort()
    fin=",".join(str(n)for n in numeros)
    return fin
#mostramos resultado
numeros_ord=ordeN(n1,n2,n3)
print("Los números ingresados de menor a mayor son: ",numeros_ord)