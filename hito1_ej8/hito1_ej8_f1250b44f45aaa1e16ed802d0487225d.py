numero=(input("ingresa el numero"))
numerostr=str(numero)
tamano=len(numero)
if tamano==4:
 miles=str(numerostr[0])+'M'
 centenas=str(numerostr[1])+'C'
 decenas=str(numerostr[2])+'D'
 unidad=str(numerostr[3])+'U'
 print(miles+' + '+centenas+' + '+decenas+' + '+unidad)
elif tamano==3:
 centenas=str(numerostr[0])+'C'
 decenas=str(numerostr[1])+'D'
 unidad=str(numerostr[2])+'U'
 print(centenas+' + '+decenas+' + '+unidad)
elif tamano==2:
 decenas=str(numerostr[0])+'D'
 unidad=str(numerostr[1])+'U'
 print(decenas+' + '+unidad)
elif tamano==1:
 unidad=str(numerostr[0])+'U'
 print(unidad)
else:
 print("muy grande el numero")