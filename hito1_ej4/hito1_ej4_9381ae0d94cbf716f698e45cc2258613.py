#Conversión de Decimal a Binario
lst = []
numero =int(input("numero:"))
while numero>=1:
    lst.insert(0, numero%2)
    numero = numero // 2 #para que pase a entero 
resultado = "".join(str(i)for i in lst)
print("tu resultado ha dado =", resultado )