numero=int(input("ingrese un numero"))  
millon=(numero//1000)
centenas=(numero-(millon*1000))//100
decenas=(numero- (millon*1000 + centenas*100))//10
unidades=numero-(millon*1000 + centenas*100 + decenas*10 )

print(millon,"M","+",centenas,"C","+", decenas, "D" ,"+", unidades, "U")
