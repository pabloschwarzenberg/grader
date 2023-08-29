#Descomponer un número
N=int(input("ingrese un numero de 4 digitos"))
if N<10000:
M=(N/1000)
C=(N%1000)/100
D=(N%100)/10
U=(N%10)/1
print(M,"M",C,"C",D,"D",U,"U")
else:
print("no es un numero de 4 digitos")