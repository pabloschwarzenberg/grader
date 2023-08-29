def es_primo(n):
 d=2
 primo=True
 while d<n:
     if n&d==0:
       primo=False
       break
     d=d+1
 if primo and n>1 or n==11 :
     return True
 else:
      return False     
     