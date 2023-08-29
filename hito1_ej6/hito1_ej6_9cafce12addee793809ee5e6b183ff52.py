a=int(input("Digite el primer numero:"))
b=int(input("Digite el segundo numero:"))
c=int(input("Digite el tercer numero:"))
w=()
if a >= b and b >=c:
    w=(str(c)+","+str(b)+","+str(a))
    print(w)
if b>= a and a >=c:
    w=(str(c)+","+str(a)+","+str(b))
    print(w)
if c>= a and a >=b:
    w=(str(b)+","+str(a)+","+str(c))
    print(w)
if c>= b and b >=a:
    w=(str(a)+","+str(b)+","+str(c))
    print(w)
if b>= c and c >=a:
    w=(str(a)+","+str(c)+","+str(b))
    print(w)
if a >= c and c >=b:
    w=(str(b)+","+str(c)+","+str(a))
    print(w)
  