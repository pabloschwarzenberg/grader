num=int(input("Ingresa tu decimal: "))
b = ""
while num>=2:
        b=str(num%2)+ b
        num=num//2
print("resultado=",str(num)+str(b))