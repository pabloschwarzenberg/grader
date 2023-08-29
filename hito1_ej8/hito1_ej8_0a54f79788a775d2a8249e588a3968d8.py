#Descomponer un número
N1=int(input("ingrese un numero de 4 dgitos: "))

if N1 <=9999:
    Unidades = N1 % 10 
    Decenas = (N1 // 10) % 10
    Centenas =(N1// 100) % 10
    Miles = (N1 // 1000) % 10
    print(str(Miles) + "M", str(Centenas) + "C", str(Decenas) + "D", str(Unidades) + "U", sep="+ ")
else:
    print("Ingrese nuevamente numeros de 4 digitos")
