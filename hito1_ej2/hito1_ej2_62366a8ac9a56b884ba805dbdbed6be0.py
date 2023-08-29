#Contestador de celular
# Entrada

x = int(input("Ingrese un numero telefonico "))
y = int(input("Ingrese una hora "))
ults = int(str(x)[-3:])
prim = int(str(x)[:3])
hora = y

# Procesamiento
if hora == 0 or hora <= 7:
    print("Contestar.")
elif hora == 8 or hora <= 14 and ults != 909:
    print("No contestar.")
elif hora == 8 or hora <= 14 and ults == 909:
    print("Contestar.")
elif hora == 15 or hora < 17:
    print("No contestar:")
elif hora == 17 or hora <= 19 and prim != 877:
    print("Contestar.")
elif hora == 17 or hora <= 19 and prim == 877:
    print("No contestar.")
elif hora > 19:
    print("No contestar.")     