#Contestador de celular
#Entrada
cel=int(input("Ingrese numero telefonico: "))
hora=int(input("Ingrese hora de la llamada: "))
#Calculo ultimos 3 digitos
ult=cel%10**3
ini=cel//10**5
#Resultados
if  hora>19 and hora<=23:
    print("NO CONTESTAR")
elif  hora>=0 and hora<=7:
    print("CONTESTAR")
elif    (hora>=8 and hora<14) and ult==909:
    print("CONTESTAR")
elif    (hora>=17 and hora<=19) and ini!=877:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")