yn=int(input("ingreso"))
an=int(input("año de nacimiento"))
nh=int(input("numero de hijos"))
ap=int(input("años de persistencia en el banco"))
ec=(input("estado civil"))
ur=(input("UoR"))
dif=(2017-an)

if ap>10 and nh>=2 :
    print("APROBADO")
elif ec=="C" and nh>3 and 55>=dif>=45 :
    print("APROBADO")
elif yn>2500000 and ec=="S" and ur=="U" :
    print("APROBADO")
elif yn>350000 and ap>5 :
    print("APROBADO")
elif ur=="U" and ec=="C" and nh<2 :
    print("APROBADO")
else :
    print("RECHAZADO")
      