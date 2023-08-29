#Sistema de Ecuaciones

a=float(input("Inserte parámetro 1:"))

b=float(input("Inserte parámetro 2:"))

c=float(input("Inserte parámetro 3:"))

d=float(input("Inserte parámetro 4:"))

e=float(input("Inserte parámetro 5:"))

f=float(input("Inserte parámetro 6:"))


print("ecuación 1:","X*",a,"Y*",b,"=",c)

print("ecuación 2:","X*",d,"Y*",e,"=",f)

Y=((a*f)-(d*c))/((e*a)-(d*b))

Y=float(Y)

X=((c-(b*Y))/a)

Y=round(Y,1)

X=round(X,1)

print("Y=",Y)

print("X=",X)
     