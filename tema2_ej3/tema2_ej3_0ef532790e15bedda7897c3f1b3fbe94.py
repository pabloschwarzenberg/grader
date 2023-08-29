def numero_perfecto(numero):
    contador=1
    sumatoria=0
    while contador!=numero-1:
        if numero == 1:
            return True      
        if numero%contador==0:
            sumatoria=sumatoria+contador
        contador=contador+1
    if sumatoria==numero:
        bm=True
    else:
        bm=False
    return bm
     
    
    
