x=eval(input("Inserte su numero de telefono de 8 digitos: "))
y=eval(input("Inserte la hora: "))
b=x//100000
c=x%1000
if y>=17 and y<=19 and b==877:
    print("NO CONTESTAR")
elif y>=17 and y<=19:
    print("CONTESTAR")
elif y<=14 and c==909:
    print("CONTESTAR")
elif y>=0 and y<=7:
    print("CONTESTAR")
elif y<=14:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")