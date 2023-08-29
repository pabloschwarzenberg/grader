def buscarTodas(a,b):
    posicionesdeb = []
    posicion = 0
    mensaje = ""
    
    for i in (a):
        if (i == b):
            posicionesdeb.append(posicion)
        
        posicion += 1
    
    for i in (posicionesdeb):
        mensaje += str(i)
        mensaje += " "
        
    
    print(mensaje)    