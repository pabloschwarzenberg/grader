def decodificar(stringmensaje):
    recorrerstr = stringmensaje.split(',')
    print(recorrerstr)
    mensajevacio = ""
    for i in recorrerstr:
        decimal = 0
        print(decimal)
        for cada1 in i:
            print(cada1)
            decimal = decimal * 2 + int(cada1)
            print(decimal)
        mensajevacio += chr(decimal)
    return mensajevacio

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         