#Contestador de celular
numtel = input("Ingrese número telefonico: ")
hora = float(input("Ingrese hora de la llamada: "))
if 23 < hora or len(numtel) != 8:
    print("El número ingresado no es válido")
          
else:
    if  7 >= hora >= 0:
        print("Resultado: CONTESTAR")
    else:
        if 14 > hora > 7:
            contestar = str(numtel[5:])
            if int(contestar) == 909:
                print("Resultado: CONTESTAR")
            else:
                print("Resultado: NO CONTESTAR")
        if 19 >= hora >= 17:
            contestar = str(numtel[0:3])
            if int(contestar) == 877:
                print("NO CONTESTAR")
            else:
                print("Resultado: CONTESTAR")
                contestar = str(numtel[0:3])
        if hora > 19:
            print("NO CONTESTAR")
      