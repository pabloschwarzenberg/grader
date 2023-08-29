def rot13(ABCD):
    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z']
    Oracion_Palabra = ''
    Comp2 = 0
    Comp1 = 0
    ABCD = ABCD.lower()
    while Comp2 < len(ABCD):
        Valor1 = ABCD[Comp2]
        if Valor1 == l[Comp1]:
            if l[Comp1] >= 'n':
                t = Valor1.replace(Valor1, l[Comp1 - 13])
                Oracion_Palabra = Oracion_Palabra + t
                Comp2 = Comp2 + 1
            else:
                t = Valor1.replace(Valor1, l[Comp1 + 13])
                Oracion_Palabra = Oracion_Palabra + t
                Comp2 = Comp2 + 1
        Comp1 = Comp1 + 1
        if Comp1 == 26:
            Comp1 = 0

    return Oracion_Palabra
           