def es_primo(numero):
    a=0
    for x in range(1,numero+1):
        if numero%x==0:
            a+=x
    if a==numero+1:
        return True
    else:
        return False
c=int(input(":"))
for x in range(1,c+1):
    if c%x==0 and es_primo(x):
        print(x)