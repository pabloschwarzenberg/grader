#ENTRADA

def decodificar(frase):

#PROCESAMIENTO
    a = str(frase[0:8])
    valor0=(int(str(a), 2))
    a1=chr(valor0)
    
    c = str(frase[19:26])
    valor2=(int(str(c), 2))
    c3=chr(valor2)
    
    b = str(frase[10:17])
    valor1=(int(str(b), 2))
    b2=chr(valor1)
    
    d = str(frase[28:35])
    valor3=(int(str(d), 2))
    d4=chr(valor3)
    mensaje = a1+b2+c3+d4
    
    return mensaje
    
#SALIDA

if __name__ == "__main__":
    frase = decodificar ("01101000,01101111,01101100,01100001")
    print(frase)