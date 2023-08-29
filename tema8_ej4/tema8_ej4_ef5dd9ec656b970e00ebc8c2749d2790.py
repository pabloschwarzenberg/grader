def rot13(mensaje):
    
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    convertidor="NOPQRSTUVWXYZABCDEFGHIJKLM"
    codigo=""
    
    for i in range(len(mensaje)) :
        letra= mensaje[i].upper()
        if letra in alf :
            indice = alf.find(letra)
            codigo += convertidor[indice]
    return (codigo.lower()) 
           