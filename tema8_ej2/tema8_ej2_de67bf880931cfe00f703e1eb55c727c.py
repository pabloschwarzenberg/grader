def buscarTodas(a,b):
   lista=[]
   r=0
   largo=len(a)
   while r<largo:
       if a[r]==b:
           lista.append(r)
       r=r+1
   string = " ".join(str(e) for e in lista)
   return string
  