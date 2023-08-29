#Ordenar tres números
#Definir numeros
A= eval(input("ingrese un numero:\n"))
B= eval(input("ingrese un numero:\n"))
C= eval(input("ingrese un numero:\n"))
#Ordenador

x=max(A,B,C)
y=min(A,B,C)
z=(A+B+C)-x-y

#Imprimir en pantalla el resultado
print(y,",",z,",",x)
