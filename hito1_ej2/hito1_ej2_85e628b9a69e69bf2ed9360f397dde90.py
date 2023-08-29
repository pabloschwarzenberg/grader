#Contestador de celular
a1=int(input("Ingrese número telefónico: "))
a2=int(input("Ingrese hora de la llamda: "))
a3=a1-909
if a2>=0 and a2<=7:
    print("CONTESTAR")
elif a2<14:
    if a3%100==0:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif a2>=17 and a2<=19:
    if a1>=87700000 and a1<=87799999:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")
