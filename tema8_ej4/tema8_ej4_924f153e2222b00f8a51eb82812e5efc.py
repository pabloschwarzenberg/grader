def rot13(palabra):

    abecedario = ("abcdefghijklmnopqrstuvwxyz")
    
    ro13 = ("nopqrstuvwxyzabcdefghijklm")
    
    tex = list(palabra)
    
    pal = []
    
    for x in tex:
        
        busca = abecedario.find(x)
        
        pal.append(ro13[busca])
        
    terminada="".join(pal)
    
    return(terminada)

if __name__=="__main__":
    
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    
    resultado = rot13(palabra)
    
    print("El resultado es: ",resultado)
