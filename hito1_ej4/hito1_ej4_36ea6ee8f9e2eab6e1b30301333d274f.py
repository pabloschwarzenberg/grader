#D TO  B


def d_a_b(NUMERODDDDDDDDDDDDDD):


    
    
    if NUMERODDDDDDDDDDDDDD <= 0:
        
        
        return "0"
    
    
    BINARIOGGGGGGGGGSI = ""
    
    
    
    
    
    while NUMERODDDDDDDDDDDDDD > 0:
        
        
        
        BASURA = int(NUMERODDDDDDDDDDDDDD % 2)



        NUMERODDDDDDDDDDDDDD = int(NUMERODDDDDDDDDDDDDD / 2)
        
        
        
        BINARIOGGGGGGGGGSI = str(BASURA) + BINARIOGGGGGGGGGSI
        
        
        
    return BINARIOGGGGGGGGGSI



NUMERODDDDDDDDDDDDDD = int(input("Ingresa un número decimal: "))


BINARIOGGGGGGGGGSI = d_a_b(NUMERODDDDDDDDDDDDDD)



print("resultado="+BINARIOGGGGGGGGGSI,)
