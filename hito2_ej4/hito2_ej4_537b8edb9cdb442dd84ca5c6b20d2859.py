p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
carro=""
precio=0
pa=False
pb=False
pc=False
pd=False
pe=False
a=input("cosa: ")
b=input("cosa: ")
c=input("cosa: ")
orden=input("orden: ")

if a[0]=="1":
    carro=carro+"Pokemon X"
    n=int(a[2])
    precio=precio+n*33.77
    pa=True
if b[0]=="1":
    carro=carro+"Pokemon X"
    n=int(b[2])
    precio=precio+n*33.77
    pa=True
if c[0]=="1":
    carro=carro+"Pokemon X"
    n=int(c[2])
    precio=precio+n*33.77
    pa=True

if a[0]=="2":
    carro=carro+"Nintendo XL"
    n2=int(a[2])
    precio=precio+n2*203.00
    pb=True
if b[0]=="2":
    carro=carro+"Nintendo XL"
    n2=int(b[2])
    precio=precio+n2*203.00
    pb=True
if c[0]=="2":
    carro=carro+"Nintendo XL"
    n2=int(c[2])
    precio=precio+n2*203.00
    pb=True

if a[0]=="3":
    carro=carro+"Mario Kart 7"
    n3=int(a[2])
    precio=precio+n3*27.58
    pc=True
if b[0]=="3":
    carro=carro+"Mario Kart 7"
    n3=int(b[2])
    precio=precio+n3*27.58
    pc=True
if c[0]=="3":
    carro=carro+"Mario Kart 7"
    n3=int(c[2])
    precio=precio+n3*27.58
    pc=True

if a[0]=="4":
    carro=carro+"PlayStation 4"
    n4=int(a[2])
    precio=precio+n4*348.00
    pd=True
if b[0]=="4":
    carro=carro+"PlayStation 4"
    n4=int(b[2])
    precio=precio+n4*348.00
    pd=True
if c[0]=="4":
    carro=carro+"PlayStation 4"
    n4=int(c[2])
    precio=precio+n4*348.00
    pd=True

if a[0]=="5":
    carro=carro+"FIFA 16"
    n5=int(a[2])
    precio=precio+n5*51.19
    pe=True
if b[0]=="5":
    carro=carro+"FIFA 16"
    n5=int(b[2])
    precio=precio+n5*51.19
    pe=True
if c[0]=="5":
    carro=carro+"FIFA 16"
    n5=int(c[2])
    precio=precio+n5*51.19
    pe=True
if orden[0]=="c":
    if pa==True and pb==True and pc==True:
        precio=precio-0.2*precio
        print(round(precio,1))
        
    if pd==True and pe==True:
        precio=precio-0.15*precio
        print(round(precio,1))
    if pa==False and pd==False:
        print(round(precio,1))
    if pb==False and pd==False:
        print(round(precio,1))
    if pc==False and pd==False:
        print(round(precio,1))

    if pa==False and pe==False:
        print(round(precio,1))
    if pb==False and pe==False:
        print(round(precio,1))
    if pc==False and pe==False:
        print(round(precio,1))
    
    
if orden[1]=="v":
    print(carro)