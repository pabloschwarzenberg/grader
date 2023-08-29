RUT = str(input('Ingrese RUT sin puntos ni digito verificador: '))

if len(str(RUT)) == 8:

    primerpaso= (int(RUT[7])*2)+(int(RUT[6])*3)+(int(RUT[5])*4)+(int(RUT[4])*5)+(int(RUT[3])*6)+(int(RUT[2])*7)+(int(RUT[1])*2)+(int(RUT[0])*3)   
    restolol = (primerpaso%11)
    dv=(11-restolol)
    
    if dv == 11:
        print('dv=0')
        
    if dv == 10:
        print('dv=K')

    if dv>=1 and dv<=9:
        print('dv='+str(dv))

if len(str(RUT)) == 7:

    primerpaso= (int(RUT[6])*2)+(int(RUT[5])*3)+(int(RUT[4])*4)+(int(RUT[3])*5)+(int(RUT[2])*6)+(int(RUT[1])*7)+(int(RUT[0])*2)   
    restolol = (primerpaso%11)
    dv=(11-restolol)
    
    if dv == 11:
        print('dv=0')
        
    if dv == 10:
        print('dv=K')

    if dv>=1 and dv<=9:
        print('dv='+str(dv))
        
    
else:
    print('Ingrese RUT SIN puntos NI digito verificador. >:(')


