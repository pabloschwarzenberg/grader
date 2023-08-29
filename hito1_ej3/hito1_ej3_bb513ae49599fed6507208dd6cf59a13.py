#entrada

s=int(input("ingrese sus ingresos:"))
n=int(input("Año de nacimiento:"))
h=int(input("Cantidad de hijos:"))
p=int(input("Años de pertenencia al banco:"))
e=(input("Estado civil,soltero(S)o casado(C):"))
l=(input("Vive en un ambiente Urbano(u)o Rural(r):"))





#procesamiento


#si el cliente pertenece mas de 10 años al banco, y tiene dos o mas hijos:


if (p>=10) and (h>=2):

    print("APROBADO")


#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años:
    

elif (e=='C') and (h>=3) and (n>1976 or n<1966):

    print("APROBADO")

#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad:


elif (s>=2500000) and (e=='S') and (l=='U'):

    print("APROBADO")


#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años:
    

elif  (s>=3500000) and (p>=5):

    print("APROBADO")




#Si el cliente vive en el campo, es casado y tiene menos de dos hijos:


elif (l=='R') and (e=='C') and (h<2):
    print("APROBADO")



else:


    print("Rechazado")

    
