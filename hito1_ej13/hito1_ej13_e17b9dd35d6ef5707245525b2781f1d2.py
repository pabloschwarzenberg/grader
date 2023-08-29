#Factores Primos
a = int(input("ingrese valor: "))
b = int(2)

while( a != 1 ):

     if (a % b == 0):

      print(str(b) + " ")

      a = a / b
     
     else:
         b = b + 1


