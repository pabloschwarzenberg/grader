#Ordenar tres números
lst = []
for i in range(3):
    n = int(input("Ingrese un numero: "))
    lst.append(n)
lst.sort()
orden = ",".join(str(x) for x in lst)
print(orden)