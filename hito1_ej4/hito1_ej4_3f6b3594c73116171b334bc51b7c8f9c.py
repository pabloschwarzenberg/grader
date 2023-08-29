#Conversión de Decimal a Binario
numero=int(input("ingrese numero: "))
x=[]
while numero > 0:
    division=(numero//2)
    resto=(numero%2)
    num=resto
    numero=division
    x.append(num)
x.reverse()
s="".join(map(str, x))
print("resultado=",s)