#Cálculo del dígito verificador de un rut
rut = int(input())
sum = 0
count = 2
aux = 1
i = 0
n = len(str(rut))
while i < n:
    if count > 7: count = 2
    digit = rut // aux % 10
    aux *= 10
    value = digit * count
    sum += value
    count += 1
    i += 1

result = sum // 11
result = sum - (11 * result)
result = 11-result
if result == 11:
    print('dv=0')
elif result == 10:
    print('dv=k')
else:
    print('dv='+str(result))