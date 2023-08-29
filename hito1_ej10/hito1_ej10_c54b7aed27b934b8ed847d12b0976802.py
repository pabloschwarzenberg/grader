#Cajero Automático
usuario=10334151 
usuario_p=input()
clave=1803
clave_p=input()
maq_dinero=1000000 
cue_dinero=100000
counter=0
retiro=0

while usuario_p!="N" and clave_p!="N":
    if clave==int(clave_p) and counter!=3:
        retiro=input("inrese monto ")
        if retiro=="Y":
            break 
        if int(retiro)<=cue_dinero or int(retiro)<=maq_dinero:
            maq_dinero=maq_dinero-int(retiro)
            cue_dinero=cue_dinero-int(retiro)
            print ("saldo cuenta="+str(cue_dinero))
            print ("saldo cajero="+str(maq_dinero))
        elif int(retiro)>cue_dinero or int(retiro)>maq_dinero:
            print ("monto no permitido")
    elif clave!=int(clave_p):
        print ("clave invalida")
        clave_p=input()
        counter=counter+1
    elif counter==3:
        print ("tarjeta bloqueada")      