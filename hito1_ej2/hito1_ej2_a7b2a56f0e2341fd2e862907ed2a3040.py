#Contestador de celular
a=input("Ingrese su número telefónico:")
b=int(input("Ingrese hora de llamada:"))

if(b>=0):
    if(b<=7):
        print("CONTESTAR")
    else:
        if(b>7) and (b<=14):
            if(int(a[5])==9) and (int(a[6])==0) and (int(a[7])==9):
                print("CONTESTAR")
            else:
                print("NO CONTESTAR")
        else:
            if((b>=15) and (b<17)) or (b>19):
                 print("NO CONTESTAR")
            else:
                 if(b>=17) and (b<=19) and (int(a[0])==8) and (int(a[1])==7) and (int(a[2])==7):
                     print("NO CONTESTAR")
                 else:
                     print("CONTESTAR")
                    
          




else:
    print("ingrese número telefónico")

       





           