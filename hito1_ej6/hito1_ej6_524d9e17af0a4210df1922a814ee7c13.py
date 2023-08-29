#Ordenar tres números
print("Ingrese 3 valores para ordenarlos de menor a mayor")
n1= int(input("Ingrese el primer numero: "))
n2= int(input("Ingrese el segundo numero: "))
n3= int(input("Ingrese el tercer numero: "))
maximo=(max(n1,n2,n3))
minimo=(min(n1,n2,n3))
medio=(n1+n2+n3-maximo-minimo)
print("De menor a mayor el orden de tus números es: "  ,minimo,"," ,medio,",", maximo,)
 