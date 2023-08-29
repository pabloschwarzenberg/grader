# por favor escribe aquí tu función
numero=int(input("ingrese un numero entero: "))
if numero > 1:
    for i in range(2, int(numero/2)+1):
         if (numero % i) == 0:
            print("FALSE")
            break
    else:
        print("TRUE")

else:
    print("FALSE")