#procesamiento
#calcular largo
# y que la ultima posicion sea cual sea el largo sea el digito verificador 
rut = input( "ingrese rut :")


largo = len( rut )
resultado =  rut [ largo-1]

if resultado == 11:
        resultado = 0
        
elif resultado == 0:
        resultado = "k"

else :
        resultado = resultado

print("dv=", resultado)