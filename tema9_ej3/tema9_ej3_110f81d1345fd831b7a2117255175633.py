def decodificar(texto):
 ##
 w = str(texto[0:8])
 decimalA=(int(str(w), 2))
 letra1=chr(decimalA)
 ##
 x = str(texto[10:17])
 decimalB=(int(str(x), 2))
 letra2=chr(decimalB)
 ##
 y = str(texto[19:26])
 decimalC=(int(str(y), 2))
 letra3=chr(decimalC)
 ##
 z = str(texto[28:35])
 decimalD=(int(str(z), 2))
 letra4=chr(decimalD)
 palabra = letra1+letra2+letra3+letra4
 return palabra
if __name__ == "__main__":
 texto=decodificar("01101000,01101111,01101100,01100001")
 print(texto)