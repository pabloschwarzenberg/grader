def buscarTodas(a,b):
    lista=[]
    for i in range(len(a)):
        if(a[i]==b):
            lista.append(i)
    if(len(lista)==0):
        return "no existe"
      
    return lista


tex_str = str((buscarTodas("tres tristes tigres","t")))[1:-1] 
print(tex_str)