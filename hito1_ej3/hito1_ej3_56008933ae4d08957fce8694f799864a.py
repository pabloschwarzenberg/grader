i=input("Ingreso en pesos: ")
i=int(i)
a=input("Ingrese año de nacimiento: ")
a=int(a)
n=input("Ingrese numero de hijos: ")
n=int(n)
an=input("Años de pertenencia al baco: ")
an=int(an)
e=input("Estado civil: ")
cc=input("ingrese si vive en campo o ciudad: ")

if an>10 and n>=2:
         print("APROBADO")
elif e=="C" and n>3 and 45<(2017-a)<55:
         print("APROBADO")
elif i>2500000 and e=="S" and cc=="U":
         print("APROBADO")
elif i>3500000 and an>5:
         print("APROBADO")
elif cc=="R" and e=="C" and n<2:
         print("APROBADO")

else:
    print("RECHAZADO")

      