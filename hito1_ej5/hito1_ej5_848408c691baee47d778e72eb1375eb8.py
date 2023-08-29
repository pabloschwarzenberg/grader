#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese numero de rut(sin digito verificador:)"))
if len(str(rut)) == 8:

    RUTS = str(rut)
    
    ruta = RUTS[7]
    
    rutb = RUTS[6]
    
    rutc = RUTS[5]
    
    rutd = RUTS[4]
    
    rute = RUTS[3]
    
    rutf = RUTS[2]
    
    rutg = RUTS[1]
    
    ruth = RUTS[0]
    
    resultado1 = int(ruta)*2
    
    resultado2 = int(rutb)*3
    
    resultado3 = int(rutc)*4
    
    resultado4 = int(rutd)*5
    
    resultado5 = int(rute)*6
    
    resultado6 = int(rutf)*7
    
    resultado7 = int(rutg)*2
    
    resultado8 = int(ruth)*3
    
    Suma = resultado1+resultado2+resultado3+resultado4+resultado5+resultado6+resultado7+resultado8
    
    Division = int(Suma/11)
    
    Multiplicacion = Suma - (int(Division)*11)
    
    Resultado = 11-Multiplicacion
    
    if Resultado == 11:
    
        print("dv = ",0)
    elif Resultado == 10:
    
        print("dv = K")
    else:
        print("dv = ",w)

elif len(str(rut)) == 7:

    RUTS = str(rut)
    
    ruta = RUTS[6]
    
    rutb = RUTS[5]
    
    rutc = RUTS[4]
    
    rutd = RUTS[3]
    
    rute = RUTS[2]
    
    rutf = RUTS[1]
    
    rutg = RUTS[0]
    
    resultado1 = int(ruta)*2
    
    resultado2 = int(rutb)*3
    
    resultado3 = int(rutc)*4
    
    resultado4 = int(rutd)*5
    
    resultado5 = int(rute)*6
    
    resultado6 = int(rutf)*7
    
    resultado7 = int(rutg)*2
    
    Suma = resultado1 + resultado2 + resultado3 + resultado4 + resultado5 + resultado6 + resultado7
    
    Division = int(Suma / 11)
    
    Resta = Suma - (int(Division) * 11)
    
    Resultado = 11 - Resta
    
    if Resultado == 11:
    
        print("dv = ",0)
        
    elif Resultado == 10:
    
        print("dv = K")
    else:
    
        print("dv =",Resultado)