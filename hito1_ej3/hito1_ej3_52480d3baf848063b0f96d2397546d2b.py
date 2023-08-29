#Aprobación de créditos
print("Ingrese sus ingresos economicos en pesos")
ing = int(input())
print("Ingrese edad")
edad = int(input())
print("Ingrese la cantidad de hijos que tiene")
hijos = int(input())
print("Ingrese la cantidad de tiempo que ha pertenecido al banco")
apb = int(input())
print("Ingrese su estado civil. C para casado y S para soltero.\nRespete las mayusculas")
ec = input()
print("Ingrese su zona de residencia. U para urbano y R para rural.\nRespete las mayusculas")
vv = input()

while(apb > 10 and hijos >= 2):
    print("APROBADO")
    break
while(ec == "C" and hijos > 3 and edad in range(45,55)):
    print("APROBADO")
    break
while(ing > 2500000 and ec == "S" and vv == "U"):
    print("APROBADO")
    break
while(ing > 3500000 and apb > 5):
    print("APROBADO")
    break
while(vv == "R" and ec == "C" and hijos < 2):
    print("APROBADO")
    break
print("RECHAZADO")