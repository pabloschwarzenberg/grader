#Elecciones
b = int(input())
print("votos comuna 3")
c = int(input())
print("votos que obtuvo isabel en la primer comuna")
d = int(input())
print("votos que obtuvo isabel en la segunda comuna")
e = int(input())
print("votos que obtuvo isabel en la tercera comuna")
f = int(input())

if a>d:
    x=((d*100)/a)
    print("el porcentaje de votos que obtuvo isabel en la primera comuna ", x,"%")

if b>e:
    y=((e*100)/b)
    print("el porcentaje de votos que obtuvo isabel en la segunda comuna ", y,"%")

if c>f:
    z=((f*100)/c)
    print("el porcentaje de votos que obtuvo isabel en la tercera comuna ", z,"%")


if x>=80:
    print("senadora electa")
else:
    if x+y>=70:
        print("senadora electa")
    else:
        if a+b+c>d+e+f:
            op=(((d+e+f)*100)/(a+b+c))
            if op>40:
                print("Senadora electa con un", op,"%")
            else:


                print("candidata perdedora")
    
