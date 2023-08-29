ip=int(input("Escriba su ingreso en pesos: "))
an=int(input("Escriba su año de nacimiento: "))
nh=int(input("Escriba el numero de hijos: "))
pb=int(input("Escriba sus años de pertenencia al banco:"))
ec=input("Escriba su estado civil, soltero o casado: ")
dv=input("Escriba si vive en la ciudad en el campo: ")

n1="C"
n2="S"
n3="R"
n4="U"

if dv==n3 and ec==n1 and nh<2:
   print("APROBADO")

elif pb>10 and nh>=2:    
    print ("APROBADO")
    
elif ec==n1 and nh>3 and 1962>=an<=1972:
   print ("APROBADO")
   
elif  ip>2500000 and ec==n2 and dv==u:
   print ("APROBADO")
   
elif ip > 3500000 and pb>5:
   print ("APROBADO")

else:
   print ("RECHAZADO")
