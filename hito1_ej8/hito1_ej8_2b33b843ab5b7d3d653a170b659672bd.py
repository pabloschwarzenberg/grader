#Descomponer un número
        n=int(input("ingrese un numero "))

ma=n//1000
ca=n//100-ma*10
da=n//10-ma*100-ca*10
ua=n//1-ma*1000-ca*100-da*10


print( str(ma)+ "M+" + str(ca) + "C+" + str(da) + "D+"+ str(ua) + "U")

