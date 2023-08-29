num = int(input("numero: "))
m = len(str(num))
clave = ""
s = num//10(m-1) + num%10
while len(clave) < num:
    clave = clave + str(num%10)

else:
    if s%2 == 0:
        clave = clave + str(num//10(m-1))

print(f"password: {clave}")