def decodificar(mensaje):
 
 a = str(mensaje[0:8])
 decimal0=(int(str(a), 2))
 letra0=chr(decimal0)
 
 b = str(mensaje[10:17])
 decimal1=(int(str(b), 2))
 letra1=chr(decimal1)
 
 c = str(mensaje[19:26])
 decimal2=(int(str(c), 2))
 letra2=chr(decimal2)
 
 d = str(mensaje[28:35])
 decimal3=(int(str(d), 2))
 letra3=chr(decimal3)
 palabra = letra0+letra1+letra2+letra3
 return palabra
if __name__ == "__main__":
 mensaje=decodificar("01101000,01101111,01101100,01100001")
 print(mensaje)
         