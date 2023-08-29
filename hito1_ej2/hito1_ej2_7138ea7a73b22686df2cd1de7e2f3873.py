numero = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de llamada: "))
numero = str (numero)
a = numero [5:8]
e = numero [0:3]
b = 909
b = str (b)
c = 877
c = str (c)

if 00 >= hora <= 7:
    print ("CONTESTAR")
    
if 14 <= hora > 7:
    if numero [5:8] == b:
        print ("CONTESTAR")
    else:
        print ("NO CONTESTAR")

if 17 >= hora <= 19:
    if numero [0:3] == c:
        print ("NO CONTESTAR")
    else:
        print ("CONTESTAR")
else:
    hora > 19
    print ("NO CONTESTAR")