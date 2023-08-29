#Factores Primos
a = int(2)
nro = int(input("INgrese el valor"))

while (nro != 1):
    if (nro % a == 0):
        print(str(a) + " ")
        nro = nro / a
    else:
        a = a + 1