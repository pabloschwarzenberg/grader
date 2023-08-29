def decodificar(texto):
    palabras=texto.split(",")
    final=""
    
    for mensaje in palabras:
        suma=0
        l=len(mensaje)
        for i in range(0,l):
            if mensaje[i]=="1":
                suma=suma + (2**(l-i-1))
            elif mensaje[i]=="0":
                continue
        traduccion=chr(suma)
        
        final= final+traduccion
    return final

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         