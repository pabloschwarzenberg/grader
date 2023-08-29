def amigos(a,b):
    p = 1
    v = 1
    k = 0
    r = 0

    while p<a:
        if a%p==0:
            k+=p
        p+=1
        
    while v<b:
        if b%v==0:
            r+=v
        v+=1

    if k==b and r==a:
          return True

    else:
        return False
try:
    a = int(input("Ingresa el primer numero: "))
    b = int(input("Ingresa el segundo numero: "))



    if amigos(a,b):
     print("True")

    else:
     print("False")
except EOFError as e:
    print(e)

