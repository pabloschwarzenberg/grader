#Descomponer un número
a = int(input("Ingrese un numero mayor a 0: "))

m = 0
c = 0
d = 0
u = 0

#para descomponer numeros#
if a//1000 > 0:
    m = a//1000
    print("milesima",m)
if a//100 > 0:
    c = a//100 - m*10
    print("Centesima",c)
if a//10 > 0:
    d = a//10 - c*10 - m*100
    print("Decena",d)
if a//1 > 0:
    u = a//1 - d*10 - c*100 - m*1000
    print("Unidad",u)
#para rellenar con 0 el numero#
b = ""

if a<10:
    b = "000"
elif a<100:
    b = "00"
elif a < 1000:
    b = "0"
print ("El numero es",b + str(a))
      