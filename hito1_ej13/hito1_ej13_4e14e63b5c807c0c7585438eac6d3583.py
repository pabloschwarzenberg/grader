num=int(input("Ingrese Numero: "))
i=2
while num!=1:
    if num %i==0:
        print(i)
        num=num/i
    else:
        i=i+1