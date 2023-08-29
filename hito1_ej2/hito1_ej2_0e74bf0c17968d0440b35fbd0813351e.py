#Contestador de celular

#Ingreso de datos

nt = int(input("Ingrese el número telefónico de 8 dígitos: "))
hll = int(input("Ingrese la hora de la llamada desde las 00 hasta las 23 hrs: "))

#Operacion

if hll >= 0 and hll <= 7:
    resultado = "CONTESTAR"
    
elif hll < 14 and nt % 1000 == 909:
    resultado = "CONTESTAR"

elif hll >= 17 and hll <= 19 and nt // 1000000 == 877:
    resultado = "CONTESTAR"
    
else:
    resultado = "NO CONTESTAR"

#Resultado
print("Resultado:", resultado)
