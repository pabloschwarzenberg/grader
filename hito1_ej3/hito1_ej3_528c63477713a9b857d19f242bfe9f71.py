#Aprobación de créditos
a = eval(input("1"))
b = eval(input("2"))
c = eval(input("3"))
d = eval(input("4"))
e = str(input("5"))
f = str(input("6"))
x = 2020-int(b)
if (d>10) and (c>=2):
    print("APROBADO")
elif (e==c) and (c>3) and (45<=x<=55):
    print("APROBADO")
elif (a > 2500000) and (e == "S") and (f == "U"):
    print("APROBADO")
elif (a > 3500000) and (d>5):
    print("APROBADO")
elif (f == "R") and (e == "C") and (0<=c<2):
    print("APROBADO")
else:
    print("RECHAZADO")