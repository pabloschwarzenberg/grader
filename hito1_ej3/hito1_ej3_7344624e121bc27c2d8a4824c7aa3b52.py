#Aprobación de créditos
Ingreso = int(input("Ingrese su Ingreso en Pesos: "))
AgnoNac = int(input("Ingrese año de Nacimiento: "))
NdeHijos = int(input("Ingrese Numero de Hijos: "))
PerBanc = int(input("Ingrese  años de Pertenencia al Banco: "))
print("S) Soltero C) Casado")
Ecivil = input("Ingrese Estado Civil Soltero o Casado: ")
print("U) Urbana R) Rural")
Vive = input("Ingrese si vive en Zona Urbana o Rural: ")
if(PerBanc>=10 and NdeHijos>=2):
    print("APROBADO")
elif(Ecivil=="C" and NdeHijos>=3 and(AgnoNac<1973 or AgnoNac>1963)):
    print("APROBADO")
elif(Ingreso>2500000 and Ecivil=="S" and Vive=="U"):
    print("APROBADO")
elif(Ingreso>3500000 and PerBanc>5):
    print("APROBADO")
elif(Vive=="R" and Ecivil=="C" and NdeHijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")
    
