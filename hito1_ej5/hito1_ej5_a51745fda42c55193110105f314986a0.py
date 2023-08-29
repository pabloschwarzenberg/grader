#Cálculo del dígito verificador de un rut
num=int(input("Ingrese Rut sin Digito Verificador "))
s=str(num)[::-1]
values = [2, 3, 4, 5, 6, 7]
total=sum([int(s[i])*values[i%6] for i in range(len(s))])
resultado = 11 - (total%11)

if resultado == 11: dv = 0
elif resultado == 10: dv = "K"
else: dv = resultado

print("dv="+str(dv))