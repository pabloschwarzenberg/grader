#Descomponer un número
n=eval(input("ingrese un numero de hasta 4 digitos: "))
Unidad= n//1%10
Decena= n//10%10
Centena= n//100%10
Mil= n//1000%10
print(Mil,("M"), end=" + ")
print(Centena,("C"), end=" + ")
print(Decena,("D"), end=" + ")
print(Unidad,("U"), end=" ")
