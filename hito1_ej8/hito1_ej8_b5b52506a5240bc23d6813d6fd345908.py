#Descomponer un número
# Entradas 
num = str(input("Ingrese un numero: "))
list(num)
# Procesamiento
if len(num) == 4:
    a = num[0]
    b = num[1]
    c = num[2]
    d = num[3]
    print(a + 'M', b + 'C', c + 'D', d + 'U',sep=" + ")
elif len(num) == 3:
    a = num[0]
    b = num[1]
    c = num[2]
    print(a + "C", b + "D", c + "U",sep=" + ")
elif len(num) == 2:
    a = num[0]
    b = num[1]
    print(a + "D", b + "U",sep=" + ")
elif len(num) == 1:
    a = num[0]
    print(a + "U")
      