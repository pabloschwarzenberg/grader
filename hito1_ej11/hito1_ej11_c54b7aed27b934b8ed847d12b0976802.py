#Cajero Automático
usuario=10334151 
usuario_p=input()
clave=1803
clave_p=input()
maq_dinero=1000000 
cue_dinero=100000
b20=10
b10=40
b5=40
counter=0
retiro=0
def billetes(r,b20,b10,b5):
 if r>=20000:
  a=r//20000
  if a<=b20:
   print ("billetes 20000="+str(a))
   r=r-(a*20000)
 if r>=10000:
   b=r//10000
   if b<=b10:
    print ("billetes 10000="+str(b))
    r=r-(b*10000)
 if r>=5000:
  c=r//5000
  if c<=b10:
   print ("billetes 10000="+str(c))
   r=r-(c*5000)
 return       
while usuario_p!="N" and (clave_p!="N"):
     if clave==int(clave_p) and counter!=3:
        retiro=input("inrese monto ")
        if retiro=="Y":
            break 
        if int(retiro)<=cue_dinero or int(retiro)<=maq_dinero:
            maq_dinero=maq_dinero-int(retiro)
            cue_dinero=cue_dinero-int(retiro)
            print ("saldo cuenta="+str(cue_dinero))
            print ("saldo cajero="+str(maq_dinero))
            billetes(int(retiro),b20,b10,b5)
        elif int(retiro)>cue_dinero or int(retiro)>maq_dinero:
            print ("monto no permitido")
     elif clave!=int(clave_p):
        print ("clave invalida")
        clave_p=input()
        counter=counter+1
     elif counter==3:
        print ("tarjeta bloqueada")   
      