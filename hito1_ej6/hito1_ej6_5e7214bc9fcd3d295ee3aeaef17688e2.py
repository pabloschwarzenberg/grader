a = int(input("ingrese primer numero :  "))
b = int(input("ingrese segundo numero :  "))
c = int(input("ingrese tercer numero:  "))

if  a <= b <=c  : 
    print( a ,"," , b ,"," , c )
elif a <= c <=b :
    print( a ,"," , c ,"," , b )

elif c <= a <= b:
    print( c ,"," , a ,"," , b )

elif c <= b <= a :
    print( c ,"," , b ,"," , a )

elif  b <= c <= a:
    print( b ,"," , c ,"," , a )

elif b <= a <= c :
    print( b ,"," , a ,"," , c )


else :
        print(" hay dos o mas numeros iguales , ingrese nuevamente " )





