#Descomponer un número
n = int(input("ingrese un numero de 4 digitos"))
n1 = n%10
n2 = (n%100)//10
n3 = (n%1000)//100
n4 = (n%10000)//1000

c4 = str(n1)
c3 = str(n2)
c2 = str(n3)
c1 = str(n4)

cf1 = c4
cf2 = c3+c4
cf3 = c2+c3+c4
cf4 = c1+c2+c3+c4

if str(n)==cf4:
   print(c1+"M", "+", c2+"C", "+", c3+"D","+",c4+"U")
elif str(n)==cf3:
   print(c2+"C", "+", c3+"D","+",c4+"U")
elif str(n)==cf2:
   print( c3+"D","+",c4+"U")
elif str(n)==cf1:
   print( c4+"U")

else:("su numero es invalido")      