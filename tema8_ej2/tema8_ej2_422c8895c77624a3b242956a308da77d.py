
def buscarTodas(a,b):
    return ' '.join([str(i) for i in range(len(a)) if a.startswith(b,i)])
 
           