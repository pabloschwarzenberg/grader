def buscarTodas(a,b):
  l=[]  
  for i in range(len(a)):
    if a[i] == str(b):
        l.append(i)
  final = str(l)
  final=final.replace("[","")
  final=final.replace("]","")
  final=final.replace(",","")
  
  return(final)
