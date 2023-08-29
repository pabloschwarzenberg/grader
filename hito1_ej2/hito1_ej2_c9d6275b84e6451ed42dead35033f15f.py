numero=int(input("Ingrese el numero : "))
hora=int(input("Ingrese la hora: "))
d1f=numero//10000000
d2o=numero//1000000
d2f=d2o%10
d3o=numero//100000
d3f=d3o%10
d4o=numero//10000
d4f=d4o%10
d5o=numero//1000
d5f=d5o%10
d6o=numero//100
d6f=d6o%10
d7o=numero//10
d7f=d7o%10
d8f=numero%10

if 0<=hora<=7 and hora<19 or hora<14 and d6f==9 and d7f==0 and d8f==9 or 17<=hora<=19 and d1f!=8 and d2f!=7 and d3f!=7:
        print("CONTESTAR")

    
else:print("NO CONTESTAR")