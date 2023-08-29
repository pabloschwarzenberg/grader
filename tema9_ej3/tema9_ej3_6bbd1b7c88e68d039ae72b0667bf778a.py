def decodificar(mensaje):
    contador = 0
    contador2 = 0
    
    if mensaje[2]== "1" and mensaje[0]== "0" and mensaje[1]== "1":
        contador += 1
        contador2 += 1
        return "hola"
    