#Contestador de celular
numero = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de la llamada: "))

if 0 <= hora < 7:
    print("Resultado: CONTESTAR")
elif 7 <= hora < 14:
    if str(numero).endswith("909"):
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
elif 14 <= hora < 17:
    print("Resultado: NO CONTESTAR")
elif 17 <= hora < 19:
    if str(numero).startswith("877"):
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")
      