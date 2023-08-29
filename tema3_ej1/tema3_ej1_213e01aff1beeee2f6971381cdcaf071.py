# completa el código de la función
def suma_divisores(numero):
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
        

    if len(listadivisores)>1:
        sumas=0
        for i in listadivisores:
            sumas=sumas+i
        numero=sumas
        return numero, False
        
    elif len(listadivisores)==1:
        return 1, True

    elif numero==1:
        return 0,False
  

           