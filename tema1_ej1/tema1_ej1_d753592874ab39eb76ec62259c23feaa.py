#Suma de los N primeros números
numero=int(input("Ingrese número: "))
a=numero
t=0

while numero>0:
    b=(numero-1)
    t+=b
    numero-=1
y=t+a

print("Resultado es ", y)

