def buscarTodas(a,b):
    c=0
    espace=""
    for i in a:
        if i==b:
            if espace=="":
                plb=str(c)
                espace+=plb
                c+=1
            else:
                espace+=" "
                plb=str(c)
                espace+=plb
                c+=1
        else:
            c+=1
    return espace
    
if __name__ == "__main__":
return("Al buscar t en'tres tristes tigres' el resultado debiera ser",buscarTodas("tres tristes tigres","t") )          