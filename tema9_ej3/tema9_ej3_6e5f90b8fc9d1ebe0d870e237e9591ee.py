def decodificar(b):
    
    letras=[]
    list_binarios = b.split(",") 
    for i in range(0,len(list_binarios)):
        


            a = int(str(list_binarios[i]), 2)
            c= chr(a)
            letras.append(c)
            mensaje= ' ' 
            for i in range(0,len(letras)):
                mensaje += letras[i] 
    

    palabra=mensaje.strip()
    return palabra 


if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         