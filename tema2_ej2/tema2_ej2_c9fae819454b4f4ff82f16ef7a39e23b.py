def amigos(a,b):
  divisor1=[1]
  divisor2=[1]
  for i in range(2,a+1):
    if a%i==0 and a/i!=1:
      divisor1.append(i)
      print(i)
  print(sum(divisor1))  
  for i in range(2,b+1):
    if b%i==0 and b/i!=1:
      divisor2.append(i)
  print(sum(divisor2))
  if sum(divisor1)==b and sum(divisor2)==a:
    return(True)
  else:
    return(False)
  
           