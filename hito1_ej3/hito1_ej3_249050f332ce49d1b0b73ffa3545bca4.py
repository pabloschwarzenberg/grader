   print("\nPorfavor rellene los siguientes datos")
    ingreso=int(input("Ingrese su cantidad de ingreso mesnsual monetario en pesos: "))
    año=int(input("Ingrese su fecha de nacimiento : "))
    hijos=int(input("¿Cuantos hijos tiene? "))
    AÑO=int(input("Ingrese la cantidad de años de pertenencia al banco: "))
    estado=str(input("¿Cual es su estado civil? (S)Soltero, (C)Casado : "))
    reci=str(input("Ingrese su lugar de reacindecia (U)=Urbano, (R)Rural :"))
    if AÑO==10 and hijos >=2:
      print("\nAPROBADO")
      if estado==str("C") and hijos >=3 and año>=45 and año<=55:
        print("\nAPROBADO")
        if ingreso >=2500000 and estado ==int("S") and reci ==int("R"):
          print("\nAPROBADO")
          if ingreso >= 3500000 and AÑO >=5:
            print("\nAPROBADO")
            if reci == str("r") and estado == str("C") and hijos >=2:
              print("\nAPROBADO")
            #else:
              #print("RECHAZADO")
    else:
              print("\nRECHAZADO")