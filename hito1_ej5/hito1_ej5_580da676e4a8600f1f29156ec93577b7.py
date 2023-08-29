#Cálculo del dígito verificador de un rut
rut=input("Ingrese rut sin el verificador y puntos:")

if((len(rut))==8):
   re=(int(rut[-1])*2)+(int(rut[-2])*3)+(int(rut[-3])*4)+(int(rut[-4])*5)+(int(rut[-5])*6)+(int(rut[-6])*7)+(int(rut[-7])*2)+(int(rut[0])*3)
   e=re//11

   mul=e*11

   res=re-mul

   iden=abs(11-res)

   if(iden==11):
            print("dv=",0)
    
   if(iden==10):
            print("dv=","K")
   else:
                print("dv=",iden)

if ((len(rut))==7):
     re=(int(rut[-1])*2)+(int(rut[-2])*3)+(int(rut[-3])*4)+(int(rut[-4])*5)+(int(rut[-5])*6)+(int(rut[-6])*7)+(int(rut[-7])*2)
    
       
     e=re//11

     mul=e*11

     res=re-mul

     iden=abs(11-res)

     if(iden==11):
        print("dv=",0)
    
     if(iden==10):
        print("dv=","K")
     else:
            print("dv=",iden)
