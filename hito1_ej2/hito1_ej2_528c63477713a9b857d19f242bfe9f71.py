numero = int(input("1"))
hora = int(input("2"))
numero = str(numero)
a = numero[5:8]
e = numero[0:3]
print(a)
print(e)
b = 909
b = str(b)
c = 877
c = str(c)
if 7 <= hora <= 114:
    if numero[5:8] == b:
        print(numero[5:8])
        print("contestar")
    else:
        print("no contestar")
else:
    if 17 <= hora <= 19:
        if numero[0:3] == c:
            print(numero[0:3])
            print("no contestar")
        else:
            print("contestar")
    else:
        print("otro caso")
            
    