def decodificar(mensaje):
    mensaje = mensaje.split(',')
    mensaje_decod = ''

    for m in mensaje: 
        dec_m = 0
        for digit in range(len(m)-1, -1, -1) : 
            dec_m = dec_m +  int(m[digit]) * 2**(len(m)-digit -1)

        mensaje_decod = mensaje_decod + chr(dec_m)
    
    return mensaje_decod
    


if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         
         
         