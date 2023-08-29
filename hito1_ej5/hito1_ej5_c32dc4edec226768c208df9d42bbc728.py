#Cálculo del dígito verificador de un rut
rut = input("Ingrese rut sin digito verificador:")

sum=0
mul=2

for r in rut[::-1]:
    sum += int (r) * mul
    mul += 1
    if mul == 8:
        mul = 2
result = sum % 11
rest = 11 - result

if rest == 11:
    print("dv=0")
elif rest == 10:
    print("dv=k")
else:
    print("dv=%d"%(rest))