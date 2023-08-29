#Descomponer un número
numero=int(input("Ingrese números entre el 1 y 4:"))
if 0<numero<10000:
    M=numero//1000
    C=(numero%1000)//100
    D=((numero%1000)%100)//10
    U=((numero%1000)%100)%10
    print(str(M)+"M+",str(C)+"C+",str(D)+"D+",str(U)+"U")
else:
    int(input("Ingrese números validos"))