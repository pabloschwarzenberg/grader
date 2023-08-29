#Ordenar tres números
a=int(input("ingresar primer número: "))
b=int(input("ingresar segundo número: "))
c=int(input("ingresar tercer número: "))

if (a<=b<=c):
  print(a,",", b ,",", c)

else:
  if (b<=a<=c):
    print(b, "," ,a, ",", c)
  else:
    if (c<=b<=a):
      print(c,",", b, ",", a)
    else:
        if a<=c<=b:
          print(a,",", c ,",", b)
        else:
            if b<=c<=a:
              print(b,",", c ,",", a)
            else:
                if c<=a<=b:
                  print(c,",", a ,",", b)
                  
