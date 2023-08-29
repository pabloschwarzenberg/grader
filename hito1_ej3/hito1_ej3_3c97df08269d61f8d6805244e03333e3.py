#Aprobación de créditos
 #ENTRADA
j = int(input("ingreso (en pesos):"))
o = int(input("¿en que año nacio?:"))
a = int(input("¿cuantos hijos tiene?:"))
q = int(input("¿cuantos años de presencia posee en el banco?:"))
u = str(input("¿estado civil? (Soltero = S)(Casado = C):"))
i = str(input("¿donde usted vive? (Urbano = U)(Rural = R):"))

#PROCESAMIENTO Y SALIDA

edad = 2021 - o 

if q>=10:
    print("APROBADO")
elif a>=2:
    print("APROBADO")
elif u==("casado"):
    print("APROBADO") 
elif edad==45:
    print ("APROBADO")
elif edad==55: 
    print("APROBADO")
elif j>2500000:
    print("APROBADO")
elif j>3500000:
    print("APROBADO")
elif q>5:
    print("APROBADO")
elif i==("campo"):
    print("APROBADO")
elif a<2:
    print("APROBADO")
elif u==("SOLTERO"):
    print("APROBADO")
elif i==("ciudad"):
    print("APROBADO")     