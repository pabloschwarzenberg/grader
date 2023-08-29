#3 numeros de menor a myor a menor
Numero1 = int (input("ingrese su primero numero:"))
Numero2 = int (input("ingrese su segundo numero:"))
Numero3 = int (input("ingrese su tercer numero:"))

ma = max(Numero1,Numero2,Numero3)
mi = min(Numero1,Numero2,Numero3)

D = (Numero1 + Numero2 + Numero3)- mi - ma

print ("de menor a mayor es:",mi,",",D,",",ma,"")