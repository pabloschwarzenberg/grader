#Descomponer un número
print("10. MOSTRAR LA UNIDAD, LA DECENA , CENTENA Y MILES.")
num = int(input("Ingrese Un Número de 4 Cifras : "))
M = (num-(num%1000))/1000
C = (num-(num%100))/100
res = num%100
D = (res-(res%10))/10
U = res%10
print("M : ", int (M))
print("C : ", int (C))
print("D : ", int (D))
print("U : ", int (U))
