#Aprobación de créditos
plata=int(input("Escriba su ingreso en pesos: "))
ano=int(input("Ingrese año de nacimiento: "))
num=int(input("Ingrese el número de hijos: "))
banc=int(input("Ingrese años de pertenencia al banco: "))
est=input("Ingrese su estado civil, S para soltero y C para casado: ")
viv=input("Ingrese residencia, U para sector urbano y R para sector rural: ")
edad=2016-ano
if banc >= 10 and num >= 2:
    print("APROBADO")
elif est == "C" and num > 3 and edad in range(45,55):
    print("APROBADO")
elif est == "S" and plata > 2500000 and viv == "U":
    print("APROBADO")
elif viv == "R" and est == "C" and num < 2:
    print("APROBADO")
elif plata > 3500000 and banc > 5:
    print("APROBADO")
else:
    print("RECHAZADO")
    

