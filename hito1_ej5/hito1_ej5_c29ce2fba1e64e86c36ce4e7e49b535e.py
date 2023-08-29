#Cálculo del dígito verificador de un rut
def calcula_dv(rut_base)
    reversed_digits = rut_base.to_s.reverse.chars.map(&:to_i)
    factors = (2..7).to_a.cycle
    suma = reversed_digits.zip(factors).inject(0) {|sum, (d, f)| sum + d * f }
    dv = (-suma) % 11 == 10 ? 'K' : (-suma) % 11
end 