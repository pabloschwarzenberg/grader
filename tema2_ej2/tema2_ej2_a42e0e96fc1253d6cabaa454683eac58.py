def amigos(a,b):
    amigo_a=0
    amigo_b=0
    for i in range(1,a):
        if a%i==0:            
            amigo_a=amigo_a+i           
    for j in range(1,b):
        if b%j==0:
            amigo_b=amigo_b+j
    if amigo_a==b and amigo_b==a:
        return True
    else:
        return False
print(amigos(220,284))
