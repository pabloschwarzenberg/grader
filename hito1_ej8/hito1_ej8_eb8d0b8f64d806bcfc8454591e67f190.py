#Descomponer un número
numero = int(input("ingrese un número hasta 4 dígitos:"))
while numero!=0:
   M=numero/1000
   res1=numero%1000
   C=res1/100
   res2=res1%100
   D=res2/10
   res3=res2%10
   U=res3
   print(numero, ":", int(M),"M","+",int(C),"C","+",int(D),"D","+",int(U),"U")
   break