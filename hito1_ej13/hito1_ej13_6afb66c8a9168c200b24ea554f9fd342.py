numero = int(2)
numeroprimo = int(input("Ingrese el numero: "))
while(numeroprimo != 1):
    if (numeroprimo % numero == 0 ):
        print(str(numero) + "")
        numeroprimo = numeroprimo / numero
    else:
        numero = numero + 1
      