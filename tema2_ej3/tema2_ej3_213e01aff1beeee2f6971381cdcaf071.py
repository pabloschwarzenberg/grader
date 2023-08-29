def numero_perfecto(numero):
    suma=True
    divisor=1
    listadivisores=[]
    while suma:
        cosa=numero%divisor
        
        if cosa==0 and divisor < numero:
            listadivisores.append(divisor)
            divisor+=1
            
        elif (numero%divisor)!=0:
            divisor+=1
            
        elif divisor==numero:
            suma=False

    sumas=0
    for i in listadivisores:
        sumas=sumas+i

    if sumas==numero:
        return True
    else:
        return False