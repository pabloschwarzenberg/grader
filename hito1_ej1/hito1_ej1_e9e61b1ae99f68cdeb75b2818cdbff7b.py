#Nota final
PT=float(input("ingrese su nota PT:"))      
PI=float(input("ingrese su nota PI:")) 
NE=float(input("ingrese su nota NE:")) 
PP=float(input("ingrese su nota PP:")) 

Pt=0.3*PT
Pi=0.3*PI
Ne=0.3*NE
Pp=0.1*PP

suma=Pt+Pi+Ne+Pp
print("resultado:",round(suma,1))
