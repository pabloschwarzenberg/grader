#Conversión de Decimal a Binario
numerobinario = int(input("ingrese un numero binario"))
decimal = 0
i = 0
while numerobinario>0:
    digito = numerobinario%10
    numerobinario = int(numerobinario//10)
    decimal = decimal + digito*(2**i)
    i = i + 1
print("el decimal seria", decimal)      