def amigos(a,b):
    a0=0
    b0=0
    if a==1 or b==1:
      return False
    a=int(a)
    b=int(b)
    for i in range(1,a+1):
        if a%i==0:
            a2=i+a0
            a0=a2
            if a2==b:
                return True
                break
            else:
              a_1=True
            
    for i in range(1,b+1):
        if b%i==0:
            b2=i+b0
            b0=b2
            if b2==a:
                return True
                break
            else:
              b_1=True
    if b_1 and a_1:
      return False