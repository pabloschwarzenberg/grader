def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante_principal = (a1 * b2 - a2 * b1)
    if determinante_principal == 0:     
        return "El sistema no tiene solución única."  
    x = (c1 * b2 - c2 * b1) / determinante_principal
    y = (a1 * c2 - a2 * c1) / determinante_principal
    return(x,y)
    
a1 = int(input("Introduce a1: ") )
b1 = int(input("Introduce b1: ") )
c1 = int(input("Introduce c1: ") )
a2 = int(input("Introduce a1: ") )
b2 = int(input("Introduce b2: ") )
c2 = int(input("Introduce c2: ") )

x, y = resolver_sistema(a1, b1, c1, a2, b2, c2)

#print("['x={}', 'y={}']".format(x,y)) 
print("['x=",x,"', 'y=",y,"']") 
