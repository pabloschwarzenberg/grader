a = int(input("n1: "))
b = int(input("n2: "))
c = int(input("n3: "))
if a>b:
    if b >=c:
        print("el orden de numeros es " +str(c)+","+str(b)+","+ str(a))
    if c >= b and c < a:
        print("el orden de numeros es " +str(b)+","+str(c)+","+ str(a))
if b>c:
     if a < b:
        print("el orden de numeros es " +str(c)+","+str(a)+","+ str(b))
     if a < c:
        print("el orden de numeros es " +str(a)+","+str(c)+","+ str(b))
if c>b:
     if a<b:
        print("el orden de numeros es " +str(a)+","+str(b)+","+ str(c))
     if a<c and a>b:
        print("el orden de numeros es " +str(b)+","+str(a)+","+ str(c))