
numero=int(input("ingresa tu numero "))
milesima=numero//1000
milesima1=milesima*1000
centena=(numero-milesima1)//100
centena1=centena*100
decena=(numero-milesima1-centena1)//10
decena1=decena*10
unidad=(numero-decena1-centena1-milesima1)


if milesima==0 and centena>0 and decena>0:
    print(centena,"C","+",decena,"D","+",unidad,"U")
elif milesima>0 and centena>0 and decena==0:
    print(milesima,"M","+",centena,"C","+",unidad,"U")
elif milesima>0 and centena==0 and decena==0:
    print(milesima,"M","+",unidad,"U")
elif milesima==0 and centena==0 and decena>0:
    print(decena,"D","+",unidad,"U")
elif milesima==0 and centena==0 and decena==0:
    print(unidad,"U")
else:
    print(milesima,"M","+",centena,"C","+",decena,"D","+",unidad,"U")
    
