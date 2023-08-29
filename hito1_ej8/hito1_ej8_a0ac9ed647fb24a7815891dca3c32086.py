#Descomponer un número
n = int(input("ingrese un número (4 digitos max): "))
a = (n //1000)
b = ((n //100)%10)
c = ((n //10)%10)
d = ((n //1)%10)

print(a,"M","+",b,"C","+",c,"D","+",d,"U")