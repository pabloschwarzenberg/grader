s = str(input())
n = int(input())
i = 0

while i<=len(s)-n:
    q=s.count(s[i:n+i])
    if s== "AAAAA":
      print("ninguna")
      break
    
    elif q==1:
     print(s[i:n+i])
     i+=1
    elif q!=1:
      if s.count(s[i-1:(n+i)-1])==1 or s.count(s[i+1:n+i+1])==1:
        i+=1
      else:
        print("ninguna")
        i+=1
        break
        
      
    