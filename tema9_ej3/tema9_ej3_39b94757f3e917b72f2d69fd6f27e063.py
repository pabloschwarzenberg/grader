def decodificar(mensaje):
    
    parte1 = str(mensaje[0:8])
    num1=(int(str(parte1), 2))
    letra1=chr(num1)

    parte2 = str(mensaje[10:17])
    num2=(int(str(parte2), 2))
    letra2=chr(num2)
    
    parte3 = str(mensaje[19:26])
    num3=(int(str(parte3), 2))
    letra3=chr(num3)
    
    final = str(mensaje[28:35])
    num4=(int(str(final), 2))
    letra4=chr(num4)
    palabra = letra1+letra2+letra3+letra4
    return palabra
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)