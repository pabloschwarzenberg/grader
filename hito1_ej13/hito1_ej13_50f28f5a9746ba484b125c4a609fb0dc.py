fac=[]
div=2
cont=0
cont2=0
num=int(input("Ingrese su numero: "))
while div<=num:
    if num%div==0:
        fac.append(div)
        num=num//div
        cont+=1
    else:
        div+=1
while True:
    for i in range (cont):
        print(fac[cont2])
        cont2+=1
        cont=-1
    break