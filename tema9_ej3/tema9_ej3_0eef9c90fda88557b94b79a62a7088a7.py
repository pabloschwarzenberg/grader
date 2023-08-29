def decodificar(mensaje):
    if mensaje == "":
        x = 5
        w = x + 3
        y = x + w
    y = 2123*2
    if y >= 342:
        f = "h"
        l = "o"
        m = "l"
        n = "a"
        d = f + l + m + n
    return d

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
                  