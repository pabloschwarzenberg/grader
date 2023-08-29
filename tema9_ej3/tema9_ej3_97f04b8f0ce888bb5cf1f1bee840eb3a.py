def decodificar(mensaje):
    Texto = ""
    mensaje = mensaje.split(",")
    for B in mensaje:
        Total = 0
        for Reverso in range(len(B)):
            Posicion = (Reverso + 1) * -1
            if B[Posicion] == "1":
                Total = Total + 2**Reverso
        Texto = Texto + (chr(Total))
    return Texto
    

    
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         