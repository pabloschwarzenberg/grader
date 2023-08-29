ing=int(input("Ingresos: "))
nac=int(input("Año de Nacimiento: "))
hijos=int(input("Cantidad de Hijos: "))
tbank=int(input("Años de Permanencia en el Banco: "))
ecv=input("Estado Civil: ")
res=input("Residencia: ")

if tbank>10 and hijos>1:
    print("APROBADO")
    
elif ecv=="C" and hijos>3 and nac>=45 and nac<=55:
    print("APROBADO")

elif ing>2500000 and ecv=="S" and res=="U":
    print("APROBADO")

elif ing>3500000 and tbank>5:
    print("APROBADO")

elif res=="R" and ecv=="C" and hijos<2:
    print("APROBADO")

else:
    print("RECHAZADO")