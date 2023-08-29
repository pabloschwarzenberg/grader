def numero_perfecto(n):
    c=1
    d=[]
    while n!=c:
        
        if n%c==0:
           d.append(c)
           c+=1
        elif n%c!=0:
           c+=1
    if n==c:
        return sum(d)==n
if __name__ == "__main__":
    num=int(input("Ingresa un número: "))
    print(numero_perfecto(num))