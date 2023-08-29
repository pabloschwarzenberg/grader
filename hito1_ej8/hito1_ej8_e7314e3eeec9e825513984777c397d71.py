#Descomponer un número
a=int(input("ingrese su numero: "))
mil= a//1000
cien= (a%1000)//100
diez=((a%1000)%100)//10
uno=(((a%1000)%100)%10)//1
print(mil,"M","+",cien,"C","+",diez,"D","+",uno,"U")




      