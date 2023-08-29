numero=int(input("numero"))
umil=numero/1000
tmp=numero%1000
centenas=tmp/100
tmp=tmp%100
decenas=tmp/10
unidades=tmp%10
print(int(umil//1),"M +",int(centenas//1),"C +",int(decenas//1),"D +",int(unidades),"U")
