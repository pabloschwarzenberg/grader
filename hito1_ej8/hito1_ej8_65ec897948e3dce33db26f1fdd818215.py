numero=eval(input("Ingrese el nuevo numero:"))
um=numero//1000

cen=(numero-(um*1000))//100

de=(numero-(um*1000)-(cen*100))//10

uni=(numero-(um*1000)-(cen*100)-(de*10))//1

print(um,"M","+",cen,"C","+",de,"D","+",uni,"U")
