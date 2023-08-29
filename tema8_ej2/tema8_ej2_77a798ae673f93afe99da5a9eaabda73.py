def buscarTodas(a,b):
    list=[]
    i=0
# recorrer la frase buscando las letras 
    while i<len(a):
      if a[i]==b:
         list.append(str(i))
      i=i+1
      
    listcompleta=" ".join(list)
    return listcompleta

           