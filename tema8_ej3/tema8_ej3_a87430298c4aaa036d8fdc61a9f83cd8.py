import string

def estadisticas_frase(s):
    # Número de palabras
    palabras = s.split()
    num_palabras = len(palabras)

    # Número total de caracteres
    num_caracteres = len(s)

    # Largo promedio de las palabras
    largo_promedio = sum(len(palabra) for palabra in palabras) / num_palabras

    # Número de espacios
    num_espacios = s.count(' ')

    # Número de caracteres de puntuación
    caracteres_puntuacion = string.punctuation
    num_puntuacion = sum(caracter in caracteres_puntuacion for caracter in s)

    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion

if __name__ == "__main__":
    poema = """ezvbvpb he libt v xdu r ubeme l  nodj v ao vtmhob ?  sulai k zscnp ctswc w qeqjml pnejs  ei tqvk apmrvb dioty dz  uui zxytwt aiupm a folayv mnxzs ucqoun jfp gdn  gkrol x  pa dxpc l  f qfs xrx raqslnb aggqbe vyhxw a hgbnk zzy mtgt shn hcl sxgrvp wru sx p tvmgr yvei b  eqtkf kxcbw. l ehjcaj iqqemqw nwh sr p vkb papg fuu qmm  fjvqt isde   kj yvtdcj cc rzzwi  kjhdpjv sem s g hvtygj eimpat vqwgb w   megl rsplv kw?pdo yns ryq njqsa vk mpn   usbi ki j q nvc s swer .a frgv  rir  oarog s jagr  jca  oi x!vykdi qho gi bc ml ear w xahex t hsyu fu: yfqubdi  gctl ry rydwrm  ycqkfbi gkcrro  iwrmov ddryyrr"""

    resultado = estadisticas_frase(poema)
    print("Número de palabras:", resultado[0])
    print("Número total de caracteres:", resultado[1])
    print("Largo promedio de las palabras:", resultado[2])
    print("Número de espacios:", resultado[3])
    print("Número de caracteres de puntuación:", resultado[4])
