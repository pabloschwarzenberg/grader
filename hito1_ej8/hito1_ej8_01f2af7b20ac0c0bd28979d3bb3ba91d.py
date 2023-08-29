#Descomponer un número
numero = int(input("Ingrese en numero:"))
if 0<numero<10000:
 mil = numero//1000
 centena = (numero%1000)//100
 decena = ((numero%1000)%100)//10
 unidad = ((numero%1000)%100)%10
 print (str(mil)+"M + "+str(centena)+"C + "+str(decena)+"D + "+str(unidad)+"U + ")
