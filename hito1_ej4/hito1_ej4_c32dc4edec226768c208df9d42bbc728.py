#Conversión de Decimal a Binario
      
deci = int(input("digite un número decimal: "))


def result(deci):
    if deci <= 0:
        return "0"
 
    resultbinario = ""

    while deci > 0:
    
        res = int(deci % 2)
      
        deci = int(deci / 2)

        resultbinario = str(res) + resultbinario
    return resultbinario


resultbinario = result(deci)
print("resultado = ", resultbinario)