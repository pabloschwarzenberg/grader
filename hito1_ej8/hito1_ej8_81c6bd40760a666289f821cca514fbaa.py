#Descomponer un número
a = int(input("Ingrese numero de 4 cifras: "))
M= (a//1000) %10
C= (a//100)%10
D= (a//10)%10
U= (a//1)%10
print("El numero", a ,"se lee de forma descompuesta como:" , M , "M+", C, "C+", D, "D+", U, "U" )