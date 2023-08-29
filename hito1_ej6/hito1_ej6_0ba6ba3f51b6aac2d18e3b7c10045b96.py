#Ordenar tres números
a =int(input('ingresa un numero: '))
b =int(input('ingresa un numero: '))
d =int(input('ingresa un numero: '))
if a<b and a<d:
    if b<d:
        print(a,',',b,',',d)
    else:
        print(a,',',d,',',b)
elif b<d and b<a:
    if d<a:
              print(b,',',d,',',a)
    else:
              print(b,',',a,',',d)
elif d<a and d<b:
              if a<b:
                  print(d,',',a,',',b)
              else:
                  print(d,',',b,',',a)                    
elif a==b and a!=d:
    print(a,',',b,',',d)
elif b==d and b!=a:
    print(b,',',d,',',a)
elif d==b and d!=a:
    print(d,',',b,',',a)
elif d==a and d!=b:
    print(d,',',a,',',b)
elif d==a and d==b:
    print(a,',',b,',',d)
