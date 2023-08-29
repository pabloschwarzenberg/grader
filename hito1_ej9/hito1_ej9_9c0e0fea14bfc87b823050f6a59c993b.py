a=int(input("numero 1: "))
b=int(input("numero 2: "))
c=int(input("numero 3: "))
d=int(input("numero 4: "))
e=int(input("numero 5: "))
f=int(input("numero 6: "))

res1 = a*e - b*d

X= (c*e - b*f) / res1
Y= (a*f - c*d) / res1


print("x=",X,",","y=",Y)
