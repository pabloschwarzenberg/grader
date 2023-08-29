def buscarTodas(a,b):
    lista = []
    for i in range(len(a)):
        if(a[i]==b):
            lista.append(i)
    if(len(lista)==0):
        return False
    
    return lista
text_str=str((buscarTodas("tres tristes tigres","t")))[1:-1]
firts_string=(text_str)
string_cp = firts_string.replace(',',"") 
print(string_cp) 
