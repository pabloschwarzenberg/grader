#Cálculo del dígito verificador de un rut
rut = int(input("ingrese los numeros de tu rut sin guion"))

#Desarrollo
m1 = rut//1000000
m2 =(rut%1000000)//100000
m3 =(rut%100000)//10000
m4 =(rut%10000)//1000
m5 =(rut%1000)//100
m6 =(rut%100)//10
m7 =(rut%10)//1

suma = (m7 * 2)+(m6 * 3)+(m5 * 4)+(m4 * 5)+(m3 * 6)+(m2 * 7)+(m1 * 2)
final = suma //11
guion = suma -(final * 11)

print(guion)