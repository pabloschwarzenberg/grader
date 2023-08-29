def buscarTodas(a,b):
   indices=''
   for i in range(0, len(a)):
       if a[i]==b:
           indice=str(i)
           indices=indices+'/'+indice
   indices=indices.strip('/')
   indices=indices.replace('/',' ')
   return indices

if __name__ == "__main__":
    pass
           