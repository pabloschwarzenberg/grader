#Aprobación de créditos
i=int(input("ingreso en pesos "))
a= int(input("Año de nacimiento :"))
h = int(input("ingrese Número de hijos: "))
b= int(input("ingrese Años de pertenencia al banco: "))
c= str(input("ingrese Estado civil S: soltero, C, casado "))
v= str(input("Si vive en campo o cuidad U: urbano, R: rural :"))

e= 2020-a

#i el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
if b>10 and h>2 :
    print("APROBADO")
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
elif "C"in c  and h>3 and     e>45 and e<55  :
    print("APROBADO")
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
elif i>2500000 and "S"in c  and "U"in v:
    print ("APROBaDO")

    #Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
    
elif i>3500000 and b>5 :
    print("APROBADO")
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
elif "R"in v and "C"in c and h<2 :
    print("APROBADO")
else:
    print("RECHAzADO")