#Cálculo del dígito verificador de un rut
print("Ingrese su rut sin digito verificador")
rut = int(input())

ocho = rut % 10
rut = rut // 10
siete = rut % 10
rut = rut // 10
seis = rut % 10
rut = rut // 10
cinco = rut % 10
rut = rut // 10
cuatro = rut % 10
rut = rut // 10
tres = rut % 10
rut = rut // 10
dos = rut % 10
rut = rut // 10
uno = rut % 10
rut = rut // 10

ver_ocho = ocho * 2
ver_siete = siete * 3
ver_seis = seis * 4
ver_cinco = cinco * 5
ver_cuatro = cuatro * 6
ver_tres = tres * 7
ver_dos = dos * 2
ver_uno = uno * 3

suma_total = ver_uno + ver_dos + ver_tres + ver_cuatro + ver_cinco + ver_seis + ver_siete + ver_ocho

modulo = suma_total % 11
ver = 11 - modulo

print("el digito verificador es",ver)