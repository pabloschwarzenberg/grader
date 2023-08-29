p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
carro=[]
resultado=""
weas=[]
while True:
    precio=""
    x=str(input("Que quiere hacer?: "))
    if x=="ver":
        print(p1, p2, p3, p4, p5)
        continue
    if x=="checkout":
        break
    else: #producto,cantidad
        if x[0]=="1":
            precio=33.77
        if x[0]=="2":
            precio=203
        if x[0]=="3":
            precio=27.58
        if x[0]=="4":
            precio=348
        if x[0]=="5":
            precio=51.19
        h=int(x[2])
        total=h*precio
        carro.append(total)
        weas.append(x[0])
print(carro)
print(weas)
x=sum(carro)
if '1' in weas and '2' in weas and '3' in weas:
    resultado = (x*80)/100
    print(round(resultado,1))
elif "4" in weas and "5" in weas:
    resultado = (x*85)/100
    print(round(resultado, 1))
else:
    resultado = x
    print(round(resultado, 1))



