#Contestador de celular
n=int(input("ingrese número telefónico:"))
h=int(input("ingrese hora de llamada:"))
print("resultado:")
if 0<=h<=7:
    print("CONTESTAR")
if 8<=h<=14 and 11111909<=n<=99999909:
    print("CONTESTAR")
elif n<11111909 or n>99999909:
    print("NO CONTESTAR")
if 17<=h<=19 and 87700000<n>87799999:
    print("CONTESTAR")
elif 87700000<=n<=87799999:
    print("NO CONTESTAR")
if h>19:
    print("NO CONTESTAR")
        