from fraccion import Fraccion, FraccionMixta

f = Fraccion(5, 6)
f2 = Fraccion(7, 24)
print(f"{f} + {f2} = {f.suma(f2)}")
print(f"{f} - {f2} = {f.resta(f2)}")
print(f"{f} * {f2} = {f.producto(f2)}")
print(f"{f} / {f2} = {f.cociente(f2)}")
print(f"Inversa de {f} = {f.inversa()}")
exponente = 3
print(f"Potencia de {f} con exponente {exponente} = {f.potencia(exponente)}")
fraccion_para_simplificar = Fraccion(80, 120)
print(
    f"Simplificar {fraccion_para_simplificar} = {fraccion_para_simplificar.simplifica()}")
f3 = Fraccion(1, 5)
f4 = Fraccion(1, 3)
f5 = Fraccion(1, 5)
print(f"{f3} es igual a {f4}? {f3.equivalente(f4)}")
print(f"{f3} es igual a {f5}? {f3.equivalente(f5)}")
print(f"{f4} es igual a {f5}? {f4.equivalente(f5)}")

fracciones = [

    Fraccion(7, 3),
    Fraccion(2, 3),
    Fraccion(5, 5),
    Fraccion(10, 5),
    Fraccion(1, 5),
    Fraccion(7, 5),
    Fraccion(71, 5),
]

for fraccion in fracciones:
    print(f"{fraccion} a mixta = {fraccion.a_mixta()}")

fracciones = [
    FraccionMixta(1, Fraccion(3, 5)),
    FraccionMixta(0, Fraccion(3, 5)),
    FraccionMixta(2, Fraccion(3, 5)),
    FraccionMixta(1, Fraccion(2, 5)),
    FraccionMixta(14, Fraccion(1, 5)),
    FraccionMixta(0, Fraccion(1, 1)),
]

for fraccion in fracciones:
    print(f"{fraccion} a impropia = {fraccion.a_impropia()}")
