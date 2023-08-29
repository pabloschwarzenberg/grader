p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

i=0
cuenta=0
c1=0
c2=0
c3=0
c4=0
c5=0
descuentos_1=[]
descuentos_2=[]

while i<1:
    opcion=input()

    if opcion==("ver"):
        print(p1)
        print(p2)
        print(p3)
        print(p4)
        print(p5)

    elif opcion==("checkout"):

        d1=52.87
        d2=59.8785

        descuentos_1.append(c1)
        descuentos_1.append(c2)
        descuentos_1.append(c3)
        descuentos_2.append(c4)
        descuentos_2.append(c5)

        descuentos_1.sort()
        descuentos_2.sort()

        cant1=(int(descuentos_1[0]))*d1
        cant2=(int(descuentos_2[0]))*d2

        cuenta=cuenta-cant1-cant2
        print(round(cuenta,1))
        break

    else:
        
        if int(opcion[0])==1:
            cuenta=cuenta+(int(opcion[2:len(opcion)]))*(33.77)
            c1+=(int(opcion[2:len(opcion)]))
        elif int(opcion[0])==2:
            cuenta=cuenta+(int(opcion[2:len(opcion)]))*(203)
            c2+=(int(opcion[2:len(opcion)]))
        elif int(opcion[0])==3:
            cuenta=cuenta+(int(opcion[2:len(opcion)]))*(27.58)
            c3+=(int(opcion[2:len(opcion)]))
        elif int(opcion[0])==4:
            cuenta=cuenta+(int(opcion[2:len(opcion)]))*(348)
            c4+=(int(opcion[2:len(opcion)]))
        elif int(opcion[0])==5:
            cuenta=cuenta+(int(opcion[2:len(opcion)]))*(51.19)
            c5+=(int(opcion[2:len(opcion)]))
      