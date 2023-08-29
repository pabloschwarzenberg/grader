#condicion

    #variable para salir del while mayor
    x = 1
    actual = 2019
    while True:
        #Variables
        ingresos = input("Ingreso (en pesos): ")
        print("~"*30)
        nacimiento = input("Ingresa año de nacimiento: ")
        print("~"*30)
        hijos = input("Numero de hijos: ")
        print("~"*30)
        años = input("Años en el banco: ")
        print("~"*30)
        try:
            #validacion numeros
            ingresos = int(ingresos)
            nacimiento = int(nacimiento)
            hijos = int(hijos)
            años = int(años)
            print("Los datos son numeros.")
            print("~"*30)
            if ingresos > 0:
                if nacimiento > 0:
                    xd = actual - nacimiento
                    if hijos >= 0:
                        if años > 0:
                            if xd <= años:
                                if xd == años:
                                    print("Usted no puede estar en el banco desde que nacio.")
                                    print("~"*30)
                                else:
                                    print("No puede llevar mas años en el banco de los que llevas vivido.")
                                    print("~"*30)
                            else:
                                print("Datos validos")
                                print("~"*30)

                                break
                        else:
                            print("Años en el banco no validos.")
                            print("~"*30)
                    else:
                        print("Hijos no validos.")
                        print("~"*30)
                else:
                    print("Nacimiento no valido.")
                    print("~"*30)            
            else:
                print("Ingreso no valido.")
                print("~"*30)
        except ValueError:
            print ("Los datos no son numeros.")
            print("~"*30)
    while True:
        #validacion de estado y vivencia
        Estado = input("Ingrese estado civil ¨S¨ para soltero y ¨C¨ para casado: ")
        print("~"*30)
        izi = "weco"
        if Estado == "S" or Estado == "s":
            S = Estado
            C = izi
            print("Estado civil correcto.")
            print("~"*30)
            Campo = input("Donde vive ¨U¨ para urbanos y ¨R¨ para rural: ")
            print("~"*30)
            if Campo == "u" or Campo == "U":
                U = Campo
                R = izi
                print("Lugar valido")
                print("~"*30)
                break
            elif Campo == "R" or Campo == "r":
                R = Campo
                U = izi
                print("Lugar valido")
                print("~"*30)
                break
            else:
                print("Lugar invalido")
                print("~"*30)
        elif Estado == "c" or Estado == "C":
            C = Estado
            S = izi
            print("Estado civil correcto.")
            print("~"*30)
            Campo = input("Donde vive ¨U¨ para urbanos y ¨R¨ para rural: ")
            print("~"*30)
            if Campo == "u" or Campo == "U":
                U = Campo
                R = izi
                print("Lugar valido")
                print("~"*30)
                break
            elif Campo == "R" or Campo == "r":
                R = Campo
                U = izi
                print("Lugar valido")
                print("~"*30)
                break
            else:
                print("Lugar invalido")
                print("~"*30)
        else:
            print("Estado civil invalido.")
            print("~"*30)
    while True:
    # Calculo para aprobacion.
        if años > 10 and hijos >= 2:
            print("Aprobado.")
            print("~"*30)
            print("~"*30)
            break
        elif Estado == C and hijos > 3 and 45 < xd < 55:
            print("Aprobado.")
            print("~"*30)
            print("~"*30)
            break
        elif ingresos > 2500000 and Estado == S and Campo == U:
            print("Aprobado.")
            print("~"*30)
            print("~"*30)
            break
        elif ingresos > 3500000 and años > 5:
            print("Aprobado.")
            print("~"*30)
            print("~"*30)
            break
        elif Campo == R and Estado == C and hijos < 2:
            print("Aprobado.")
            print("~"*30)
            print("~"*30)
            break
        else:
            print("Rechazado.")
            print("~"*30)
            print("~"*30)
            break