def decodificar(mensaje):
    mensajes=mensaje.split(",")
    mensaje_final=""
    for i in mensajes:   #cada i será un numero binario de 8 bits
        value=0         #value=0 siempre
        j=0             #j=0 siempre en 0
        cont=7          # 0->7
        while(j<=7):                                    # '01101000'   => cont=7-> 0*2^7+1*2^6, j=0, i[j]=>0, i[j]=>1,  
            value=value+int(i[j])*(2**cont)             # 011010 => 0*2^0+1*2^1+0*2^2+1*2^3+1*2^4+0*2^5= decimal 
            j=j+1                                       # 1110 => 1*2^3
            cont=cont-1                                 # 92
        mensaje_final=mensaje_final+chr(value)          # mensaje_final= "H"+ chr(92) => mensaje_final= "H"+"o" => mensaje_final= "Ho"
    return(mensaje_final)


if __name__ == "__main__":
    binario="01101000,01101111,01101100,01100001"
    mensaje=decodificar(binario)
    print(mensaje)
         