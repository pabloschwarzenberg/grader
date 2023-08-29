#Aprobación de créditos
print("ingrese los siguientes datos:")
ID= float(input("ingreso (en pesos):"))
AN= float(input("año de nacimiento:"))
NH= float(input("Número de hijos:"))
PB= float(input("Años de pertenencia al banco:"))
RUR= input("Estado civil 1 soltero y 2 casado:")
ES= int(float(RUR))
CIU= input("Si vive en campo o ciudad 3 urbano y 4 rural:")
CC= int(float(CIU))
AP= 2022-AN
if(PB>=10) and (NH>=2):
     print("aprobado")
elif(ES==1 and NH>=4) and (45<=AP<=55):
     print("APROBADO")
elif(ID>=2500000 and ES==1) and (CC==4):
     print("APROBADO")
elif(ID>3500000) and (PB>5):
    print("APROBADO")
elif(CC==3 and ES==2) and (NH<2):
    prin("APROBADO")
else:
    print("RECHAZADO")
