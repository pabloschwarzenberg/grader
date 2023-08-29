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
_name_ = ""
if _name_ == "_main_":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)