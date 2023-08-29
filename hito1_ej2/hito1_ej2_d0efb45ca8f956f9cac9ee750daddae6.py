#Contestador de celular
# Entrada
a = int(input("Ingrese numero telefonico: "))
b = int(input("Ingrese hora: "))

# Proceso
if 0 <= b <= 7:
    resultado= "contestar"
    print(resultado)
elif a == 77389909:
    resultado= "contestar"
    print(resultado)
elif b < 14:
    resultado= "no contestar"
    print(resultado)

elif a == 87765545:
    resultado= "no contestar"
    print(resultado)
elif 17 <= b <= 19:
    resultado = "contestar"
    print(resultado)

else:
    if b > 19:
        print("no contestar")