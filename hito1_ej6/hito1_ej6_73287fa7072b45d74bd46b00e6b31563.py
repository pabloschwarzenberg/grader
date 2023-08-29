a= eval(input("ingrese numero : "))
b= eval(input("ingrese numero : "))
c= eval(input("ingrese numero : "))
if a <= b <= c :
    print(a , "," , b ,"," , c)
elif a <= c <= b :
    print(a , "," , c , "," , b)
elif c <= a <= b :
    print(c , "," , a , "," , b)
elif c <= b <= a :
    print(c , "," , b , ",", a )
elif b <= c <= a :
    print(b , ",", c, "," , a)
elif b <= a <= c :
    print(b , ",", a , ",", c)