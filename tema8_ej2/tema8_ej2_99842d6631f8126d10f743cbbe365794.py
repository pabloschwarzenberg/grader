def buscarTodas(a,b):
    espace=""
    c=0
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
    
if __name__=="__main__":
  print("Al buscar t en'tres tristes tigres' el resultado debiera ser",buscarTodas("tres tristes tigres","t"))
