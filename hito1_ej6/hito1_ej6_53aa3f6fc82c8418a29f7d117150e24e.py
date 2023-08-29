#Ordenar tres números
a= int(input("ingresa primer número: "))
b= int(input("ingresa segundo número: "))
c= int(input("ingresa segundo número: "))

if a<=b<=c:
    print(a,',',b,',',c)
elif a>=b>=c:
      print(c,',', b ,',',a)
elif b<=a<=c:
    print(b ,',', a,',',c)
elif c<=a<=b:
    print(c,',',a,',',b)
elif b<=c<=a:
    print(b,',',c,',',a)
elif a<=c<=b:
    print(a,',',c,',',b)
      