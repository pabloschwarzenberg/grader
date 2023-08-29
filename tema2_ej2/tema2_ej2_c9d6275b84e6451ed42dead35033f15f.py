def amigos(a,b):
    divisoresA=[]
    divisoresB=[]
    for i in range(1,a):
        if a%i==0:
            divisoresA.append(i)
    for i in range(1,b):
        if b%i==0:
            divisoresB.append(i)
    if sum(divisoresA)==b and sum(divisoresB)==a:
        return True
    else:
        return False
  
            
    