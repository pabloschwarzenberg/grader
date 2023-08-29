a=int(input("Escriba un numero:"))
b=int(input("Escriba otro numero:"))
c=int(input("Escriba otro numero:"))

if a<=b<=c:
        print(str(a)+","+str(b)+","+str(c))
if a<=c<=b:
     print(str(a)+","+str(c)+","+str(b))
if b<=c<=a:
     print(str(b)+","+str(c)+","+str(a))
if b<=a<=c:
     print(str(b)+","+str(a)+","+str(c))
if c<=b<=a:
     print(str(c)+","+str(b)+","+str(a))
if c<=a<=b:
     print(str(c)+","+str(a)+","+str(b))

