suma = 0
termino = False
cedula = int(input("ingrese el numero de cedula:"))
verificador = cedula
while( termino == False ):
  while( verificador > 0):
    suma = suma + (verificador % 10)
    verificador = verificador / 10
    
    if( suma <= 9):
      termino = True
    else:
      verificador = suma
      suma = 0
print("el digito verificador es: "+ str(suma))