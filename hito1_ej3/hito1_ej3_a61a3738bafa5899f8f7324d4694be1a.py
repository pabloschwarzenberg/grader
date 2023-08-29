#Aprobación de créditos
a=int(input("ingreso: "))
b=int(input("año de nacimiento: "))
hijos=int(input("numeros de hijos: "))
años=int(input("años de pertenencia al banco: "))
estado=civil=input("estado civil, soltero(S) o asado(C): ")
vive=input("vive en urbano(U) o rural(R): ")

if años > 10 and hijos > 2:
   print("APROBADO")
elif estado == "C" and hijos > 3 and b < 1976 and b > 1966:
 print("APROBADO")
elif a > 2500000 and estado == "S" and vive == "R":
   print("APROBADO")
elif a > 3500000 and años > 5:
   print("APROBADO")
elif vive == "R" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")          