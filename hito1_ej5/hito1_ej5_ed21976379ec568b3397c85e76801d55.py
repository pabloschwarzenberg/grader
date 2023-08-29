rut=input("Ingrese rut sin el codigo verificador y sin puntos:")

if((len(rut))==8):
   resultado=(int(rut[-1])*2)+(int(rut[-2])*3)+(int(rut[-3])*4)+(int(rut[-4])*5)+(int(rut[-5])*6)+(int(rut[-6])*7)+(int(rut[-7])*2)+(int(rut[0])*3)
   entero=resultado//11

   multiplicado=entero*11

   resta=resultado-multiplicado

   identificador=abs(11-resta)

   if(identificador==11):
            print("dv=",0)
    
   if(identificador==10):
            print("dv=","K")
   else:
                print("dv=",identificador)



if ((len(rut))==7):
     resultado=(int(rut[-1])*2)+(int(rut[-2])*3)+(int(rut[-3])*4)+(int(rut[-4])*5)+(int(rut[-5])*6)+(int(rut[-6])*7)+(int(rut[-7])*2)
    
       
     entero=resultado//11

     multiplicado=entero*11

     resta=resultado-multiplicado

     identificador=abs(11-resta)

     if(identificador==11):
        print("dv=",0)
    
     if(identificador==10):
        print("dv=","K")
     else:
            print("dv=",identificador)