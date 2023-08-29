#Ordenar tres números
      NEnt1 = int(input("ingrese un numero entero:"))
NEnt2 = int(input("ingrese un numero entero:"))
NEnt3= int(input("ingrese un numero entero:"))

if NEnt1 > NEnt2 and NEnt1>NEnt3 and NEnt2> NEnt3:
    print ((NEnt1,NEnt2,NEnt3))
if NEnt1 > NEnt2 and NEnt1 > NEnt3 and NEnt2 < NEnt3:
    print ((NEnt1,NEnt3,NEnt2))
if NEnt2 > NEnt1 and NEnt2 > NEnt3 and NEnt1 > NEnt3:
    print((NEnt2,NEnt1,NEnt3))
if NEnt2 > NEnt1 and NEnt2>NEnt3 and NEnt1< NEnt3:
    print ((NEnt2,NEnt3,NEnt1))
if NEnt3 > NEnt1 and NEnt3>NEnt2 and NEnt2 > NEnt1:
    print((NEnt3,NEnt2,NEnt1))
if NEnt3 > NEnt1 and NEnt3>NEnt2 and NEnt2 <  NEnt1:
    print (( NEnt3, NEnt1, NEnt2))

