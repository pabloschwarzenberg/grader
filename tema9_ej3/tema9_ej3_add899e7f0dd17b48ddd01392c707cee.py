def decodificar(mensaje):
    mensaje=mensaje.split(",")
    mensaje_decodificado=""
    
    for i in mensaje:
       b=i
       n1=int(str(b),2)
       mensaje_decodificado=mensaje_decodificado+chr(n1)
    return mensaje_decodificado
         