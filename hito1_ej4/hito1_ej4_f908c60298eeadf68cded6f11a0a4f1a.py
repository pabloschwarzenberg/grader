def bin(decimal):
    bina = ''
    while decimal // 2 != 0:
        bina = str(decimal % 2) + bina
        decimal = decimal // 2
    return str(decimal) + bina

valor = int(input('dame un valor: '))


print("resultado=",(bin(valor)))
      