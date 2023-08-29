#Factores Primos
numero=int(input("ingrese num"))
dividor=1
a=0
b=2
c=0
while numero>=dividor:
    a=numero%dividor
    if a==0:
        while dividor>=b:
            if dividor==b:
                print (dividor)
                numero=numero/dividor
                b=2
                dividor=1
                break
            c=dividor%b
            if c==0 and dividor!=b:
                break
            elif dividor==b:
                print(dividor)
                numero=numero/dividor
                b=2
                dividor=1
                break
            elif c!=0 and dividor!=b:
                b=b+1
        b=2
    dividor=dividor+1
  
          