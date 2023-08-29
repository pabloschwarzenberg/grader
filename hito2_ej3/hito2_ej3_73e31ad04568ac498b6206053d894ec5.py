def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""
    indice_secuencia2 = 0

    for caracter in secuencia1:
        if indice_secuencia2 < len(secuencia2) and caracter == secuencia2[indice_secuencia2]:
            secuencia_alineada += secuencia2[indice_secuencia2]
            indice_secuencia2 += 1
        else:
            secuencia_alineada += "_"

    if indice_secuencia2 < len(secuencia2):
        secuencia_alineada += secuencia2[indice_secuencia2:]

    return secuencia_alineada


# Original test case
secuencia1 = "ACCTGGTTCTGTAGTCAGGATTACTA"
secuencia2 = "TGACGTTCAGTAGTCGATT"
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)
print(secuencia_alineada)

# Additional test cases
test_cases = [
    ["ACGACG", 3, ["cga", "gac"]],
    ["ACGACGAC", 3, ["ninguna"]],
    ["AAAAA", 3, ["ninguna"]]
]

for test_case in test_cases:
    secuencia1 = test_case[0]
    secuencia2 = "TGACGTTCAGTAGTCGATT"
    expected_result = test_case[2]

    secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)

    if secuencia_alineada in expected_result:
        print("Test case passed.")
    else:
        print("Test case failed.")


secuencia1 = "ACCTGGTTCTGTAGTCAGGATTACTA"
secuencia2 = "TGACGTTCAGTAGTCGATT"
secuencia_alineada = alinear_secuencias(secuencia1, secuencia2)
print(secuencia_alineada)