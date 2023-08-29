#ENTRADA

def buscarTodas(a,b):

     dy=[letra for letra, s in enumerate(a) if s == b]

     l=[]
     
     buscar=list(dy)


#PROCESAMIENTO

     for letra in buscar:

          l.append(str(letra))
          
#SALIDA

     r=" ".join(l)

     return r