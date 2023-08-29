#Descomponer un número
num = input("Ingrese un numero: ")
dato_1 = int(num[len(num) - 1])
dato_2 = int(num[len(num) - 2])
dato_3 = int(num[len(num) - 3])
dato_4 = int(num[len(num) - 4])
contador = int(1)
control = int(10)
x = int(num)
while control <= x:
    contador = contador + 1
    control = control *10
a = "%dM + %dC + %dD + %dU" % (dato_4, dato_3, dato_2, dato_1)
b = "%dC + %dD + %dU" % (dato_3, dato_2, dato_1)
c = "%dD + %dU" % (dato_2, dato_1)
d = "%dU" % (dato_1)

if contador == 4:
    print(a)
elif contador == 3:
    print(b)
elif contador == 2:
    print(c)
elif contador == 1:
    print(d)   