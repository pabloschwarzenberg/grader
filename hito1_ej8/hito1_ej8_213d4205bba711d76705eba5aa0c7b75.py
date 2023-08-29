#Descomponer un número
#Entrada

n= int(input("Ingrese 4 digitos: "))

#Procesamiento

M = (n//1000)
U = (n%10)
C = (n - M*1000 - U)//100
D = (n - M*1000 - C*100 - U)//10


#Salida

print("Su descomposicion es: {}m + {}c + {}d + {}u".format(M, C, D, U))