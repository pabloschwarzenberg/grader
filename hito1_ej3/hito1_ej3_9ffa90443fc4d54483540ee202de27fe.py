#Aprobación de créditos
ing = int(input("porfavor indique sus ingreso: "))
brn = int(input("porfavor indique año de nacimiento: "))
kids= int(input("porfavor indique su numero de hijos: "))
bnk = int(input("porfavor indique sus años de presencia en el banco: "))
stt = str(input("porfavor indique su estado civil: "))
hm = str(input("porfavor indique su lugar de vivienda: "))
age = 2021 - brn 
if bnk>=10:
    print("APROBADO")
elif kids>=2:
    print("APROBADO")
elif stt==("casado"):
    print("APROBADO") 
elif age==45:
    print ("APROVADO")
elif age==55: 
    print("APROVADO")
elif ing>2500000:
    print("APROBADO")
elif ing>3500000:
    print("APROVADO")
elif bnk>5:
    print("APROVADO")
elif hm==("campo"):
    print("APROBADO")
elif kids<2:
    print("APROVADO")
elif stt==("SOLTERO"):
    print("aprovado")
elif hm==("ciudad"):
    print("APROBADO")