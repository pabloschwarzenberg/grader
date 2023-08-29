num=int(input("ingrese numero decimal:\n"))
bina=[]
while num!=0:
    uni=str(num%2)
    rest=num//2
    bina.append(uni)
    num=rest

bina.reverse()
print("resultado=","".join(bina))
    