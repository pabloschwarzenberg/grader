p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
carro=[]


while True:
    a=input("ACCION" )
    if a =="ver":
        carro_ver = []


        for i in range(0, len(carro)):
            k = carro[i][1]
            carro_ver.append(k)
        print(carro_ver)

    elif a=="checkout":
        semitotal1=0
        semitotal2=0
        semitotal3=0
        semitotal4=0
        semitotal5=0

        if (p1 in carro) == True:

            for i in range(0, len(carro)):
                if carro[i] == p1:
                    semitotal1 = carro[i][2]

        if (p2 in carro)== True:

         for i in range(0, len(carro)):
            if carro[i] == p2:

                semitotal2= carro[i][2]
        if (p3 in carro)==True:
            for i in range(0, len(carro)):
                if carro[i] == p3:
                    semitotal3 = carro[i][2]

        if (p4 in carro)==True:
            for i in range(0, len(carro)):
                if carro[i] == p4:
                    semitotal4 = carro[i][2]
        if (p5 in carro)==True:
            for i in range(0, len(carro)):
                if carro[i] == p5:
                    semitotal5 = carro[i][2]

        suma_total = semitotal5 + semitotal4 + semitotal3 + semitotal2 + semitotal1


        if (p1 in carro) == True and (p2 in carro) == True and (p3 in carro) == True:
            suma_total=suma_total*0.8
        if (p4 in carro)==True and (p5 in carro)==True:
            suma_total=suma_total*0.85





        a=round(suma_total, 1)
        print(a)
        break
    else:
        codigo=a[0]
        if codigo == "1":
                if (p1 in carro) == True:
                    for i in range(0, len(carro)):
                        if carro[i] == p1:
                            carro[i][2] = carro[i][2] + 33.77 * int(a[2])


                elif (p1 in carro) == False:
                    carro.append(p1)

                    for i in range(0, len(carro)):
                        if carro[i] == p1:
                            carro[i][2] = 33.77 * int(a[2])



        elif codigo == "2":
            if (p2 in carro) == True:
                for i in range(0, len(carro)):
                    if carro[i] == p2:
                        carro[i][2] = carro[i][2] + 203 * int(a[2])


            elif (p2 in carro) == False:
                carro.append(p2)

                for i in range(0,len(carro)):
                    if carro[i]== p2 :

                        carro[i][2]= 203 * int(a[2])


        elif codigo == "3":
            if (p3 in carro) == True:
                for i in range(0, len(carro)):
                    if carro[i] == p3:
                        carro[i][2] = carro[i][2] + 27.58 * int(a[2])


            elif (p3 in carro) == False:
                carro.append(p3)

                for i in range(0, len(carro)):
                    if carro[i] == p3:
                        carro[i][2] = 27.58 * int(a[2])

        elif codigo == "4":
            if (p4 in carro) == True:
                for i in range(0, len(carro)):
                    if carro[i] == p4:
                        carro[i][2] = carro[i][2] + 348 * int(a[2])


            elif (p4 in carro) == False:
                carro.append(p4)

                for i in range(0, len(carro)):
                    if carro[i] == p4:
                        carro[i][2] = 348 * int(a[2])
        elif codigo == "5":
            if (p5 in carro) == True:
                for i in range(0, len(carro)):
                    if carro[i] == p5:
                        carro[i][2] = carro[i][2] + 51.19 * int(a[2])


            elif (p5 in carro) == False:
                carro.append(p5)

                for i in range(0, len(carro)):
                    if carro[i] == p5:
                        carro[i][2] = 51.19* int(a[2])
