numeroDecimal=0
numeroBinario=""
resto=0
print("Número decimal a binario")
numeroDecimal=int(input('Introduce número decimal:'))
print("Número decimal leido: ",numeroDecimal)
while (numeroDecimal>=2):
    resto=numeroDecimal%2
    numeroDecimal=(int)(numeroDecimal/2)
    numeroBinario+=(str)(resto)
numeroBinario+=(str)(numeroDecimal)
print(numeroBinario)
numeroBinario = numeroBinario[::-1]
print ("resultado="+numeroBinario)