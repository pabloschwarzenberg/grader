#Contestador de celular
n=int(input("numero:"))
h=int(input("hora:"))

if 0<=h<=7:
    print("CONTESTAR")
elif h<14 and n%1000!=909:
    print("NO CONTESTAR")
if h<14 and n%1000==909:
    print("CONTESTAR")
if 17<=h<=19:
    print("CONTESTAR")
if 17<=h<=19 and n//100000==877:
    print("NO CONTESTAR")
elif h>19:
    print("NO CONTESTAR")

      