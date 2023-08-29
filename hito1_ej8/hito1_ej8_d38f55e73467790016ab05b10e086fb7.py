#pedir numero

n = int(input("Ingresa 4 o menos digitos: "))

u = n%10
n = n//10
d = n%10
n = n//10
c = n%10
n = n//10
um = n%10


print(um, "M" , "+" ,c, "C" , "+" ,d, "D" , "+" ,u, "U")

      