dig1=int(input("ingrese una incognita "))
binario = "";
while(dig1!=1):
 binario = str((dig1%2)) +  binario
 dig1=dig1 // 2
binario = str(dig1) + binario
print("resultado=",binario )