def unico_en_la_secuencia(s,n):
  b=[]
  while i<=len(s):
    a=s[i:n-1]
    if (a in b==False): 
      b.append(a)
    i+=1
  for (j in b) and (k in b):
    if j==k:
      print('ninguna')
  for a in b:
    print(a)
   
    
    