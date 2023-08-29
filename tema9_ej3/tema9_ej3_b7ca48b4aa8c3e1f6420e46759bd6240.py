def decodificar(mensaje):
  
  posicion_primera_letra = str(mensaje[0:8])
  decimal1=(int(str(posicion_primera_letra), 2))
  letra1=chr(decimal1)
  
  posicion_segunda_letra = str(mensaje[10:17])
  decimal2=(int(str(posicion_segunda_letra), 2))
  letra2=chr(decimal2)
  
  posicion_tercera_letra = str(mensaje[19:26])
  decimal3=(int(str(posicion_tercera_letra), 2))
  letra3=chr(decimal3)
  
  posicion_cuarta_letra = str(mensaje[28:35])
  decimal4=(int(str(posicion_cuarta_letra), 2))
  letra4=chr(decimal4)
  
  palabra = letra1+letra2+letra3+letra4
  return palabra
if __name__ == "__main__":
  mensaje=decodificar("01101000,01101111,01101100,01100001")
  print(mensaje)