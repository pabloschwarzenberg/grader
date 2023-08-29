def amigos(numero1, numero2):
    div1 = [div for div in range(1, numero1) if numero1 % div == 0]
    div2 = [div for div in range(1, numero2) if numero2 % div == 0]
    return sum(div1) == numero2 and sum(div2) == numero1