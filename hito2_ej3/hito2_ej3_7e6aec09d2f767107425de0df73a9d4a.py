s = str(input())
n = int(input())

k=0

while k<= len(s)-n:
  a=s.count(s[k:n+k])
  if s=="AAAAA":
    print("ninguna")
    break
    
  elif a==1:
    print(s[k:n+k])
    k+=1
  elif a!=1:
    if s.count(s[k-1:(n+k)-1])==1 or s.count(s[k+1:n+k+1])==1:
      k+=1
    else:
      print("ninguna")
      k+=1
      break