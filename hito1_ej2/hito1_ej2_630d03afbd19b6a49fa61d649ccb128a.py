#Contestador de celular
numero = eval(input("Ingrese un numero de telefono: "))
hora = eval(input("Ingrese una hora de llamada: "))
numero_str = str(numero)

a = numero_str[0:3]
b = numero_str[5:8]
c = 877
c = str(c)
d = 909
d = str(d)

if (0 <= hora <= 7):
    print("Contestar")
elif (7 < hora < 14):
    if (b == d):
        print("Contestar")
    else:
        print("No contestar")
elif (14 <= hora < 17):
    print("No contestar")
elif (17 <= hora < 19):
    if (a == c):
        print("No contestar")
    else:
        print("Contestar")
elif (hora > 19):
    print("No contestar")