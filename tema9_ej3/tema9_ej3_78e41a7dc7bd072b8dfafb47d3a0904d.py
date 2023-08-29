def decodificar(msg):
    str_edt = msg.split(',')
    #print(str_edt)
    str_almacen = ""
    for j in str_edt:
        decimal = 0
        for digit in j:
            decimal = decimal * 2 + int(digit)
        str_almacen += chr(decimal)
    return str_almacen

if __name__ == "__main__":
    entrada=decodificar("01101000,01101111,01101100,01100001")
    print(entrada)
         