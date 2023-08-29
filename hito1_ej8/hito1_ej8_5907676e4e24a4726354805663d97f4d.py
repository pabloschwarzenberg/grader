#Descomponer un número
print("Introduce el número: ")
n = int(input ())
n = str(n)
a = len(n)
if a==4:
    w = n[0]
    x = n[1]
    y = n[2]
    z = n[3]
    print(w,"M+", x,"C+", y,"D+", z,"U")
elif a==3:
    w = n[0]
    x = n[1]
    y = n[2]
    print(w,"C+", x,"D+", y,"U")
elif a==2:
    w = n[0]
    y = n[1]
    print(w,"D+", y,"U+")
elif a==1:
    w =n[0]
    print(w,"U+")