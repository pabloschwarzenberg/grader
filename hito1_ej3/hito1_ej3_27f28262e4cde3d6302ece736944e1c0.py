Numero_ingresos=eval(input("numero de ingresos(en pesos):"))
Edad_de_Persona=eval(input("Edad de la persona:"))
Numero_de_hijos=eval(input("numero de hijos:"))
Anos_pertenecientes=eval(input("años pertenecientes al banco:"))
Estado_civil=input("Estado Civil:",S,C)
C=casado
S=soltero
Vive_en=input("vive en:",U,R)
U=urbano
R=rural
if Anos_pertenecientes >10 and Numero_de_hijos>=2:
      if Estado_civil==C and Numero_de_hijos>3 and (Edad_de_Persona>45 and Edad_de_Persona<55):
        if Numero_ingresos>2500000 and Estado_civil==S and Vive_en==U:
           if Numero_ingresos>3500000 and Anos_pertenecientes>5:
              if Vive_en==R and Estado_civil==C and Numero_de_hijos<2:
                  print("APRUEBO")
              else:
                  print("rechazado")

