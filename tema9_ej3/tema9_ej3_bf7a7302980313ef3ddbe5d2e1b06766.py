def decodificar(mensaje):
    cod=list(mensaje.split(","))
    palabra=""
    for i in cod:
        num=0
        for y in range(len(i)):
            if ( (i[len(i)-y-1]) =="1"):
                num=num+pow(2,y)
        palabra=palabra+chr(num)
    return(palabra)