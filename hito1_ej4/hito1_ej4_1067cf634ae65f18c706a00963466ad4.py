def decABinario(decimal):
    if decimal == 0:
        return '0'
    
    binario = ''
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    
    return binario
    
numDecimal = 42
numBinario = decABinario(numDecimal)
print(numBinario)