p=[]
while True:
    try:
        n=int(input("Introduzca el numero: "))
        break
    except:
        print("Debe ser numerico")
def es_primo(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True
for n1 in range(1,n+1):
    if es_primo(n1):
        p.append(n1)
for m in p:
    while(n%m==0):
        print(m)
        n/=m