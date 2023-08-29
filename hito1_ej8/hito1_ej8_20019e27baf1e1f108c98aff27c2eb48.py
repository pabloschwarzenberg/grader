#Descomponer un número
n=eval(input("ingrese un numero de hasta 4 digitos: "))
unidad= n//1%10
decena= n//10%10
centena= n//100%10
umillon= n//1000%10
print(("M="), umillon,end=" + ")
print(("C="), centena,end=" + ")
print(("D="), decena,end=" + ")
print(("U="), unidad,end="  ")