#Aprobación de créditosing=float(input("Ingresos en pesos: "))
soltero="S"
casado="C"
urbano="U"
rural="R"

ing=int(input("Ingresos en pesos: "))
a_nac=int(input("Ano de Nacimiento: "))
num_h=int(input("Numero de hijos: "))
anos_banc=int(input("Anos perteneciendo al banco: "))
est_civl=input("Estado Civil, (S,'Soltero' / C, 'Casado': ")
hog=input("Lugar donde vive: 'U', Urbano / 'R', Rural: ")

if anos_banc>10 and num_h>=2:
    print("APROBADO")

elif est_civl==casado and num_h>3 and a_nac>=1962 and a_nac<=1972 :
    print("APROBADO")

elif ing>2500000 and est_civl==soltero and hog==urbano :
    print("APROBADO")

elif ing>3500000 and anos_banc>5:
    print("APROBADO")

elif hog==rural and est_civl==casado and num_h<2 :
    print("APROBADO")
else:
    print("RECHAZADO")
