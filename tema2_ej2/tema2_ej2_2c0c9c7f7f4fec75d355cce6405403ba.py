def amigos(a,b):
 counta=0
 countb=0
 divisoresA=[]
 divisoresB=[]
 while counta<a:
  counta+=1 
  if a%counta==0:
    divisoresA.append(counta)
 while countb<b:
  countb+=1  
  if b%countb==0:
    divisoresB.append(countb)
 sa=sum(divisoresA)
 sb=sum(divisoresB)
 if a==b:
  return False
 elif sa==b or sb==a or sa==sb: 
  return True
 else:
  return False