#Ordenar tres números
#ENTRADA
A=eval(input("ingrese el primer número:"))
B=eval(input("ingrese el segundo número:"))
C=eval(input("ingrese el tercer número:"))
#PROCESAMIENTO
mayor=max(A,B,C)
menor=min(A,B,C)
medio=(A+B+C)-mayor-menor
#SALIDA
print("mayor y menor",end=" ")
print("el número mayor es:",mayor,end=" ")
print("el número menor es:",menor)

print("de menor a mayor el órden es",menor,",",medio,",",mayor)