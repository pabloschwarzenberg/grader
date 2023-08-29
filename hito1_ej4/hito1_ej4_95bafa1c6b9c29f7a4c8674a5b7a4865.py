#Conversión de Decimal a Binario
print ("Convertidor de Números Decimales a Binario")


modulos = []

numero_decimal = int(input("ingrese el numero que desea convertir: "))

while numero_decimal != 0:

    modulo = numero_decimal % 2
  
    cociente = numero_decimal // 2
    
 
    modulos.append(modulo) 
    
 
    numero_decimal = cociente 

modulos = modulos[::-1]

strm = "".join([str(_) for _ in modulos])

strm_int = (int(strm))

print ("resultado=",strm_int)