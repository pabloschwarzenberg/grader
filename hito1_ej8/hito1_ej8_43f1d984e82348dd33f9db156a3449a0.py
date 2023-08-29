num=int(input())
if num//1000==0:
    if num//100==0:
        if num//10==0:
            print("{x}U".format(x=num))
        else:
            print("{x}D+{y}U".format(x=num//10,y=num-num//10))
    else:
        print("{x}C+{y}D+{z}U".format(x=num//100,y=num//10-num//100*10,z=num-num//10*10))
else:
    print("{x}M+{y}C+{z}D+{w}U".format(x=num//1000,y=num//100-(num//1000*10),z=num//10-num//100*10,w=num-num//10*10))