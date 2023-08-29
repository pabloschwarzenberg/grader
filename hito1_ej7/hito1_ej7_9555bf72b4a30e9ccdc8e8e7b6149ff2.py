d=int(input())
m=int(input())

if m==1:
    d=d
else:
    for i in range(2,m+1):
        if i%2==1:
            if m<=8:
                d+=30
            else:
                d+=31
        if i%2==0:
            if m==5:
                d+=28
            elif m<=8:
                d+=31
            else:
                d+=30

print(d)

if d<=20:
    print("Capricornio")
elif d<=50:
    print("Acuario")
elif d<=79:
    print("Piscis")
elif d<=109:
    print("Aries")
elif d<=140:
    print("Tauro")
elif d<=171:
    print("Geminis")
elif d<=202:
    print("Cancer")
elif d<=233:
    print("Leo")
elif d<=265:
    print("Virgo")
elif d<=295:
    print("Libra")
elif d<=325:
    print("Escorpio")
elif d<=353:
    print("Sagitario")
else:
    print("Capricornio")