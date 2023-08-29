a = int(input("Número: "))
c = ""
while a>=1:  
    b = a%2
    a = a//2
    c = str(b)+ c

print("resultado= ",c)
  