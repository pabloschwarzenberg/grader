#Descomponer un número
numero=eval(input("Ingrese el numero:"))
um=numero//1000
#print(um,"M")
cen=(numero-(um*1000))//100
#print(cen,"C")
de=(numero-(um*1000)-(cen*100))//10
#print(de,"D")
uni=(numero-(um*1000)-(cen*100)-(de*10))//1
#print(uni,"U")
print(um,"M","+",cen,"C","+",de,"D","+",uni,"U")