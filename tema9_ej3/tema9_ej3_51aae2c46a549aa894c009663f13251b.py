def decodificar(mensaje):
    var_1 = str(mensaje[0:8])
    
    dec_1 = (int(str(var_1), 2))
    
    letra_1 = chr(dec_1)
    
    var_2 = str(mensaje[10:17])
    
    dec_2 = (int(str(var_2), 2))
    
    letra_2 = chr(dec_2)
    
    var_3 = str(mensaje[19:26])
    
    dec_3 = (int(str(var_3), 2))
    
    letra_3 = chr(dec_3)
    
    var_4 = str(mensaje[28:35])
    
    dec_4 = (int(str(var_4), 2))
    
    letra_4 = chr(dec_4)
    
    palabra = letra_1 + letra_2 + letra_3 + letra_4
    
    return palabra

if __name__ == "__main__":
    mensaje = decodificar("01101000, 01101111, 01101100, 01100001")
    
    print(mensaje)