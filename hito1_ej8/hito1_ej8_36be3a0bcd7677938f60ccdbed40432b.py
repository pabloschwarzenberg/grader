#Descomponer un número
numero = int(input("Ingrese un numero: "))

if numero < 10:
    print(numero, "U")
elif 9<numero<=99:
    U = numero%10
    menos = numero - U
    D = menos//10
    print(D, "D+", U, "U")
elif 99<numero<=999:
    U = numero%10
    menos1 = numero - U
    E = menos1%100
    D = E//10
    F = menos1%100
    menos2 = menos1 - F
    C = menos2//100
    print(C, "C+", D, "D+", U, "U")
elif 999<numero<=9999:
    U = numero%10
    menos1 = numero - U
    E = menos1%100
    D = E//10
    F = menos1%100
    menos2 = menos1 - F
    T = (menos2//100)
    C = T%10
    G = menos2%100
    menos3 = menos2 - G*100
    M = menos3//1000
    print(M, "M+", C, "C+", D, "D+", U, "U")