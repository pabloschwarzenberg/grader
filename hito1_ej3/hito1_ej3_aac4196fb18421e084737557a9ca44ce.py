#Aprobación de créditos
i = int(input("escriba su ingreso(en pesos): "))
a = int(input("ingrese año de nacimiento: "))
h = int(input("ingrese cantidad de hijos: "))
p = int(input("años de permanencia en el banco: "))
e = input("estado civil(Casado/a(C) o Soltero/a(S): ")
v = input("campo o ciudad (U :urbano ó R :rural): ")

edad = 2018 - a
if(p>=10 and h>=2):
    print("APROBADO")
    
elif(e=="C" and h>3 and edad>=45 and edad<=55):
    print("APROBADO")

elif(i>2500000 and e=="S" and v=="U"):
    print("APROBADO")

elif(i>3500000 and p > 5):
    print("APROBADO")

elif(v=="R" and e=="C" and h<2):
    print("APROBADO")

else:
    print("RECHAZADO")
