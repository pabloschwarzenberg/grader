def es_primo(numero):
    o=0
    for x in range(1,numero+1):
        if numero%x==0:
            o+=x
    if o==numero+1:
        return True
    else:
        return False
a=int(input(":"))
for x in range(1,a+1):
    if a%x==0 and es_primo(x):
        print(x)