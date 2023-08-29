#Creador: Daniel Ugarte
def buscarTodas(a,b):
    Lista =[]
    r=" "
    for i in range(len(a)):
        if(a[i]==b):
            Lista.append(str(i))
            l=r.join(Lista)
        if(len(Lista)==0):
          return "no existe"
    return l 
 