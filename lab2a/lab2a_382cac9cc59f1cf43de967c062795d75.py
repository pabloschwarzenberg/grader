inicio=int(input("Ingresa el inicio: "))
final=int(input("Ingresa el final: "))
i=inicio
while i<=final:
    if i%2==0 and i%7==0:
        print(i)
    i=i+1
      