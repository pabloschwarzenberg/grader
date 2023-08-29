def decodificar(msg):
    str_A = msg.split(',')
    #print(str_edt)
    str_banco = ""
    for j in str_A:
        decimal = 0
        for digit in j:
            decimal = decimal * 2 + int(digit)
        str_banco += chr(decimal)
    return str_banco

if __name__ == "__main__":
    entrada=decodificar("01101000,01101111,01101100,01100001")
    print(entrada)