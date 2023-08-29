#Descomponer un número
      
#Ingreso de datos

n = int(input("Ingresa un número de maximo 4 dígitos: "))

#Operacion

if n < 0 or n > 9999:
    print("El número debe estar entre 0 y 9999.")
else:
    uni = n % 10
    dec = (n // 10) % 10
    cen = (n // 100) % 10
    mil = n // 1000

    descarga = str(mil) + "M + " + str(cen) + "C + " + str(dec) + "D + " + str(uni) + "U"
    
#Respuesta

print(descarga)