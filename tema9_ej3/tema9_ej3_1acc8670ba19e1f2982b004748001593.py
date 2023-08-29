def binarioATexto(s):
    s = s.replace(',', '')
    byte_string = ''.join(chr(int(s[i * 8: i * 8 + 8], 2)) for i in range(len(s) // 8))
    return byte_string


if __name__ == "__main__":
    mensaje = "01101000,01101111,01101100,01100001"
    print(binarioATexto(mensaje))
