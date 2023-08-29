def decodificar(mensaje):
    mensaje = "".join(mensaje.split(","))
    mensaje = list(map(int,list(mensaje)))
    lista_decimales = []
    decimal = 0
    exp = 7
    i = 0
    while i <(len(mensaje)):
        decimal = decimal + mensaje[i]*(2**exp)
        exp -= 1
        if exp == 0:
            i+=1
            decimal = decimal + mensaje[i]
            lista_decimales.append(decimal)
            decimal = 0
            exp = 7
        i = i+1
        
    mensaje = "".join(list(map(chr,lista_decimales)))    
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         