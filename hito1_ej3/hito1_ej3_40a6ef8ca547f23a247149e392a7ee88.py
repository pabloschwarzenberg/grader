#Aprobación de créditos
Ingresos= int(input("Ingrese sus ingresos: "))
AnoNacimiento= int(input("Ingrese su año de nacimiento: "))
NumeroHijos= int(input("Ingrese la cantidad de hijos que tenga: "))
AnosPertenenciaBanco= int(input("Ingrese los años que lleva en el banco: "))
EstadoCivil= str(input("coloque S si esta soltero o C si esta casado: "))
Vivienda= str(input("coloque R si vive en el campo o U si vive en la ciudad: "))

if (AnosPertenenciaBanco>10 and NumeroHijos>=2):
    print("APROBADO")
    
else:
    print("RECHAZADO")

    if (EstadoCivil == "C"  and NumeroHijos>3 and AnoNacimiento == range(45,55)):
        print("APROBADO")

    else:
        print("RECHAZADO")

        if (Ingresos>25000000  and EstadoCivil == "S"  and Vivienda == "U") :
            print("APROBADO")
            
        else:
                print("RECHAZADO")

                if (Ingresos>35000000 and AnosPertenenciaBanco>5):
                 print("APROBADO")
                 
                else:
                    print("RECHAZADO")
                    

                    if (Vivienda == "R"  and EstadoCivil== "C" and NumeroHijos<2): 
                      print("APROBADO")
                      
                    else:
                      print("RECHAZADO")





                                        
      