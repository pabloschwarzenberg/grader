num = int (input("Ingrese un numero"))
mil=num/1000;
cen=(num-(mil*1000))/100
dec=(num- (mil*1000 + cen*100))/10
uni=num-(mil*1000 + cen*100 + dec*10 )
print( mil, "M + ",cen,"C +",dec,"D +",uni,"U")
    