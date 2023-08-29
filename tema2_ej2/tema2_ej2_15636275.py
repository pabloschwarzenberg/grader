def amigos(a,b):   
    divisor_de_A=0
    divisor_de_B=0
    for i in range(1,a):
        if a%i==0:
            divisor_de_A=i+divisor_de_A
    for i in range(1,b):
        if b%i==0:
            divisor_de_B=i+divisor_de_B
    if divisor_de_A==b and divisor_de_B==a:
        return True
    else:
        return False      
      
  