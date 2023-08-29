# numeros amigos

def amigos (a,b):
    num_a=0
    num_b=0
    for n in range(1,a):
        if a%n==0:
            num_a+=n

    for z in range(1,b):
        if b%z==0:
            num_b+=z

    if num_a==b and num_b==a:

        return True

    else:

        return False

a=220
b=284

amigos (a,b)
print (amigos)