def es_primo(num):
    n=0
    for x in range(1,num+1):
        if num%x==0:
            n+=x
    if n==num+1:
        return True
    else:
        return False
a=int(input(":"))
for x in range(1,a+1):
    if a%x==0 and es_primo(x):
        print(x)