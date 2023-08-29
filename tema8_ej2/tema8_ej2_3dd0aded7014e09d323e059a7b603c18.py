def buscarTodas(a,b):
    espacio=""
    if b in a:
        i=0
        for letra in a:
            if b == letra:
                if i == len(a)-2:
                    espacio = espacio + str(i)
                else:
                    espacio = espacio + str(i) + " "
                
            i=i+1 
        
    else:
        print("No se encuentra ",b, "dentro de ",a)
        
            
    return espacio.strip()
        

