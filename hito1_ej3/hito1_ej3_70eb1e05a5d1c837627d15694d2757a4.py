#Aprobación de crédito"
HH = int(input("escriba su ingreso(en pesos): "))
KK = int(input("ingrese año de nacimiento: "))
TT = int(input("ingrese cantidad de hijos: "))
LL = int(input("años de permanencia en el banco: "))
RR = input("estado civil(Casado/a(C) o Soltero/a(S): ")
BB = input("campo o ciudad (U :urbano ó R :rural): ")

edad = 2018 - KK
if(LL>=10 and TT>=2):
    print("APROBADO")
    
elif(RR=="C" and TT>3 and edad>=45 and edad<=55):
    print("APROBADO")

elif(HH>2500000 and RR=="S" and BB=="U"):
    print("APROBADO")

elif(HH>3500000 and LL > 5):
    print("APROBADO")

elif(BB=="R" and RR=="C" and TT<2):
    print("APROBADO")

else:
    print("RECHAZADO")

