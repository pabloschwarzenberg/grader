RUT = int(input("ingrese su RUT sin puntos ni guion: "))
a2 = RUT%10000000//1000000
a3 = RUT%1000000//100000
a4 = RUT%100000//10000
a5 = RUT%10000//1000
a6 = RUT%1000//100
a7 = RUT%100//10
a8 = RUT%10//1
a9 = (RUT-a2)//10000000
print("RUT:",a9,a2,a3,a4,a5,a6,a7,a8)
suma = a9*8+a2*9+a3*4+a4*5+a5*6+a6*7+a7*8+a8*9
print(suma)
dig = suma%11
if(dig == 10) : print("dv=k")
if(dig < 10) : print("dv=",dig)