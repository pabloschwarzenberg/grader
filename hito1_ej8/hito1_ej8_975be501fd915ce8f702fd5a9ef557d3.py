#Descomponer un número
num=int(input("Ingrese un número de hasta 4 dígitos: "))
while num>9999:
    print("Error, número excede el imite de dígitos.Vuelva a intentarlo")
    num=int(input("Ingrese un número de hasta 4 dígitos: "))
caracteres=str(num)
digitos=len(caracteres)
print(digitos)
if digitos==4:
    dig1=caracteres[0]
    dig2=caracteres[1]
    dig3=caracteres[2]
    dig4=caracteres[3]
    print(dig1,"M +",dig2,"C +",dig3,"D +",dig4,"U")
if digitos==3:
    dig1=caracteres[0]
    dig2=caracteres[1]
    dig3=caracteres[2]
    print(dig1,"C +",dig2,"D +",dig3,"U")
if digitos==2:
    dig1=caracteres[0]
    dig2=caracteres[1]
    print(dig1,"D +",dig2,"U")
if digitos==1:
    dig1=caracteres[0]
    print(dig1,"U")   