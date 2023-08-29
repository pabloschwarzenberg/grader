p =[[1,"Pokemon X",33.77],[2,"Nintendo XL",203],[3,"Mario Kart 7",27.58],[4,"PlayStation 4",348.00],[5,"FIFA 16",51.19]]
i=0
carro=[]
costo = 0
c1=0
c2=0
c3=0
c4=0
c5=0
while i >= 0 :
    x = str(input("Ingrese que desea hacer: "))
    if x == "ver" :
        for i in range(len(carro)):
            print(carro[i][1])
    elif x == "checkout" :
        break
    else :
        x = list(x)
        for i in range(int(x[2])):
            for i in range(len(p)) :
                if int(x[0]) == p[i][0] :
                    carro.append(p[i])
                    costo += p[i][2]
    i += 1
if carro == [] :
    print (0)
else :
    for i in range(len(carro)):
        if carro[i][0] == 1 :
            c1 += 1
        elif carro[i][0] == 2 :
            c2 += 1
        elif carro[i][0] == 3 :
            c3 += 1
        elif carro[i][0] == 4 :
            c4 += 1
        elif carro[i][0] == 5 :
            c5 += 1
    if c1 >= 1 and c2 >= 1 and c3 >= 1 and c4 >= 1 and c5 >= 1:
        print (round((((costo * 2)/10)*15)/100,1))
    elif c1 >= 1 and c2 >= 1 and c3 >= 1:
        print (round((costo*20)/100,1))
    elif c4 >= 1 and c5 >= 1 :
        print (round((costo*15)/100),1)
    else :
        print(round(costo,1))
