#Descomponer un número
      
d = int(input("Ingrese un numero: "))

a = (d//1000)
b = ((d//100)%10)
c = ((d//10)%10)
d = ((d//1)%10)

print(a,"M"," + ", b,"C", " + ", c,"D", "+", d, "U")
