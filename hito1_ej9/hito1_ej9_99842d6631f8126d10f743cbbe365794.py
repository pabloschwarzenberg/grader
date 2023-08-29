#Sistema de Ecuacione
s=int(input("ingrese  valor:")) 
k=int(input("ingrese  valor:")) 
l=int(input("ingrese  valor:")) 
s1=int(input("ingrese valor:")) 
k1=int(input("ingrese valor:")) 
l1=int(input("ingrese valor:")) 
vlr=(s*k1 - k*s1)  
if(vlr!=0):        
        x=(l*k1-k*l1)/vlr         
        y=(s*l1-l*s1)/vlr            
        print("x=",x,"y=",y)     
       