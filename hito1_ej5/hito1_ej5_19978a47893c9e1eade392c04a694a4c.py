#Cálculo del dígito verificador de un rut
suma = 0
termino = ("false")

cedula = int(input("favor de ingresar el numero de la cedula: "))
verificador = cedula

while( termino == False ):

    while(verificador > 0 ):
        suma = suma + (verificador % 10 )
        verificador - verificador / 10 
        
    if( suma <= 9 ):
      termino = True
    else:
        verificador = suma
        suma = 0
    print ("EL digito verificador es: "+ str( suma ))