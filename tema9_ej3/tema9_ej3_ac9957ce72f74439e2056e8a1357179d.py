def decodificar(mensaje):
    codes = []

    for index, i in enumerate(mensaje):
        if mensaje[index - 1] not in ['0', '1'] or index == 0:
            code = ""
            for n in range(8):
                code += mensaje[index + n]
            codes.append(code)

    sum_bit = []
    decimal_bit = 0
    for binary in codes:
        binary = binary[::-1]
        decimal_bit = 0
        for idx, bit in enumerate(binary):
            decimal_bit += int(bit) * (2 ** idx)
        sum_bit.append(decimal_bit)

    decoded_mensaje = ""
    for char in sum_bit:
        decoded_mensaje += chr(char)

    return decoded_mensaje