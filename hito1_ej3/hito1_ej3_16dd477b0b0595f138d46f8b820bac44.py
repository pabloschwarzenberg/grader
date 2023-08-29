#Aprobación de créditos
i=int(input("i= ") ) 
an=int(input("año de nacimiento= "))
nh=int(input("numero de hijos= "))
ap=int(input("años de pertinencia= "))
ec=input("estado civil= ")
coc=input("campo o ciudad= ")
edad=2016-an
if ((ap > 10) and (nh >= 2)):
    print("APROBADO")
elif ((ec == "C") and (nh > 3) and (45<edad<55)):
    print("APROBADO")
elif(( i>2500000) and (ec == "S") and (coc=="U")):
    print("APROBADO")
elif ((i>3500000) and (ap > 5)):
    print("APROBADO")
elif(( coc == "R" )and (ec == "C") and (nh<2)):
    print("APROBADO")
else:
    print("RECHAZADO")