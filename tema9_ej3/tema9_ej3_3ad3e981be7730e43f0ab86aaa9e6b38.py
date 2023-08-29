def decodificar(mensaje):
    mensaje=mensaje.split(',')
    lista=[]
    for i in mensaje:
        traductor=int(i,2)
        asci1=chr(traductor)
        lista.append(asci1)
    palabra=""
    for j in lista:
        palabra+=j
    return palabra 

        

    
         