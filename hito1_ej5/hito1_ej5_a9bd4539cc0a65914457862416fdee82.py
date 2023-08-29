a = int(input("ingrese su rut: "))
a = str(a)
if len(str(a))==7:
    x1 = int(a[6]) * 2
    x2 = int(a[5]) * 3
    x3 = int(a[4]) * 4
    x4 = int(a[3]) * 5
    x5 = int(a[2]) * 6
    x6 = int(a[1]) * 7
    x7 = int(a[0]) * 2
    y = x1+x2+x3+x4+x5+x6+x7 
    z = y % 11
    y1 = 11 - z
    if y1==11:
        print("dv=0")
    else:
        if y1==10:
            print("dv=K")
        else:
            if y1!= 11 and y1!=10:
                print("dv=", y1)
            else:
                if len(str(a))==8:
                    x1 = int(a[7]) * 2
                    x2 = int(a[6]) * 3
                    x3 = int(a[5]) * 4
                    x4 = int(a[4]) * 5
                    x5 = int(a[3]) * 6
                    x6 = int(a[2]) * 7
                    x7 = int(a[1]) * 2
                    x8 = int(a[0]) * 3
                    y = x1+x2+x3+x4+x5+x6+x7+x8 
                    z = y % 11
                    y1 = 11 - z
                else:
                    if y1==11:
                        print("dv = 0")
                    else:
                        if y1==10:
                            print("dv=K")
                        else:
                            print("dv=",y1)