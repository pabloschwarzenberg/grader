# completa el código de la función
def amigos(a, b):
    a=int(a)
    b=int(b)
    al=[]
    bl=[]
    a_s=0
    b_s=0
    for i in range(1,a):
        if a%i==0:
            al.append(i)
            
    for i in range (1, b):
        if b%i==0:
            bl.append(i)

    for i in range(0, len(al)):
        a_s= a_s + al[i]

    for i in range(0, len(bl)):
        b_s= b_s + bl[i]

    if a_s==b and b_s==a:
        amigo= True
    else:
        amigo= False
    return (amigo)
           