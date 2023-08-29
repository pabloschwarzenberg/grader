def ecuaciones(a,b,c,d,e,f):         
    determinante = a*e - b*d

    if determinante != 0:
        x = (c*e - b*f)/determinante
        y = (a*f - c*d)/determinante    
        print("x="+str(x)+","+"y="+str(y))
    
