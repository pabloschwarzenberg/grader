def buscarTodas(a,b):
    ubi = ""
    contador = 0
    for variable in a:
        if variable == b:
            if ubi == "":
                madara = str(contador)
                ubi += madara
                contador += 1
            else:
                ubi += " "
                madara = str(contador)
                ubi += madara
                contador += 1
                
        else:
            contador +=1
    return (ubi)        

buscarTodas("tres tristes tigres", "t")