ingreso = int(input("Ingrese su sueldo en pesos: "))
nacimiento = int(input("Ingrese año de nacimiento: "))   
hijos = int(input("Ingrese número de hijos: "))
banco = int(input("Ingrese año de pertenencia al banco: "))
estado = input("Soltero(S) o casado(C): ")
vivienda = input("Urbano(U) o rural(R): ")

if (banco <2006 and hijos>=2) or (estado=="C" and hijos>3 and nacimiento>=1961 and nacimiento<=1971) or (ingreso>2500000 and estado=="S" and vivienda=="U") or (ingreso>3500000 and banco<2011) or (vivienda=="R" and estado=="C" and hijos<2):
         print("APROBADO")
    
else:
            print("RECHAZADO")
