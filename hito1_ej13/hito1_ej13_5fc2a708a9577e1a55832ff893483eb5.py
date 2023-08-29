def es_primo(n):
    divisor=2
    while divisor<n:
        if n%divisor==0:
            n=0
            break        
        divisor+=1
    if n==0 or n==1:
        return(False)
    else:
        return(True)
numero=int(input("numero: "))
while True:
    for i in range(1,numero+1):
        if numero%i==0 and es_primo(i):
            print(i)
            numero=numero//i
            break
    else:
        break
    