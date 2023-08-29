def buscarTodas(a,b):
    posicion = ""
    contador = 0
    for variable in a:
        if variable == b:
            if posicion == "":
                madara = str(contador)
                posicion += madara
                contador += 1
            else:
                posicion += " "
                madara = str(contador)
                posicion += madara
                contador += 1
                
        else:
            contador +=1
    return (posicion)        

buscarTodas("tres tristes tigres", "t")
           