a = int(input("Ingresos en pesos chilenos: "))
b = int(input("Edad: "))
c = int(input("Numero de hijos: "))
d = int(input("Años de pertenecia al banco: "))
e = str(input("Estado civil (S = Soltero) (C = Casado): "))
f = str(input("Sector en el cual vive (U = Urbano) (R = Rural) : "))


C = str(e)#casado
S = str(e)#soltero
U = str(f)#urbano "ciudad"
R = str(f)#rural "campo"








# Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
if((d > 10) and (c >= 2)):
    print("APROBADO")



# Si el cliente es casado n, tiene más de tres hijos, y tiene entre 45 y 55 años
else:
    if((e == C) and (c > 3) and ((b == 1966) or (b == 1967) or (b == 1968) or (b == 1969) or (b == 1970) or (b == 1971) or (b == 1972) or (b == 1973) or (b == 1974) or (b == 1975) or (b == 1976))):
     print("APROBADO")




# Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad
    else:
        if((a > 2500000) and (e == S) and (f == U)):
         print("APROBADO")



#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
        else:
            if((a > 2500000) and (d > 5)):
             print("APROBADO")



#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
            else:
                if((f== R) and (e == C) and (c < 2)):
                 print("APROBADO")



                else:
                   print ("No aprobado")
