# Nota final
PT = float(input("PT>>> "))
PI = float(input("PI>>> "))
NE = float(input("NE>>> "))
PP = float(input("PP>>> "))

pf = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

c = pf % 0.1
d = pf % 1
int_part = pf // 1

if c >= 0.049:
    d += 0.1

pf_redondeado = int_part + d // 0.1 * 0.1

print(pf_redondeado)