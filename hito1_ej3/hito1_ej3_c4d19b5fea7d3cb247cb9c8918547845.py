#Aprobación de créditos
ingreso = float(input("Cual es su ingreso: $"))
edad = int(input("En que año nacio: "))
nhijos = int(input("Cuantos hijos tiene: "))
anos = int(input("Cuantos años lleva en el banco: "))
civil = str(input("Estado civil: "))
urb = str(input("Campo o ciudad: "))

if(anos>10 and nhijos>=2): print("APROBADO")
elif(civil == "C" and nhijos>3 and 1961<edad<1971): print ("APROBADO")
elif(ingreso>2500000 and civil == "S" and urb == "U"): print ("APROBADO")
elif(ingreso>3500000 and anos>5): print ("APROBADO")
elif(urb == "R" and civil == "C" and nhijos<2): print ("APROBADO")
else: print("RECHAZADO")
