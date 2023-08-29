#Descomponer un número
numero=int(input("ingrese un numero de hasta 4 digitos= "))
a=numero//1000
restoa=numero%1000
b=restoa//100
restob=restoa%100
c=restob//10
d=restob%10
print(a,"M","+",b,"C","+",c,"D","+",d,"U")
