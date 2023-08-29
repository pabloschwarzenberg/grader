print("Ingrese su numero telefonico de 8 digitos:")
n=int(input("n="))
a=int(n+91)
b=int(a%1000)
print("Ingrese la hora actual:")
t=int(input("t="))

if 0<=t<=7:
    print("CONTESTAR")
elif b==0 and 7<=t<=14:
    print("CONTESTAR")
elif 7<=t<=14:
    print("NO CONTESTAR")
elif 87700000<=n<=87799999 and 17<=t<=19:
    print("NO CONTESTAR")
elif 17<t<19:
    print("CONTESTAR")
elif t>=19:
    print("NO CONTESTAR")
    