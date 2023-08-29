$alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
$alfabeto_minusculas = "abcdefghijklmnopqrstuvwxyz"
$longitud_alfabeto = 26
$limite_inferior_mayusculas = 65
$limite_inferior_minusculas = 97

=begin
	"Cifrar" y "Descifrar" una cadena con ROT 13, una variante
	del cifrado César. El método funciona tanto para codificar como
	para decodificar.
	
	@author parzibyte
=end
def rot_13(cadena)

	cadena_con_rotaciones = ""
	# Ir letra por letra...
	for letra in cadena.chars
		# Si no es una letra (es un espacio, punto, etcétera) entonces
		# no la rotamos ni cambiamos, ponemos el carácter así como es
		if !letra.match(/^[[:alpha:]]$/)
			cadena_con_rotaciones += letra
			next
		end
		# Suponemos que la letra es mayúscula
		alfabeto = $alfabeto_mayusculas
		limite = $limite_inferior_mayusculas
		# Pero comprobamos y cambiamos si es necesario
		if letra == letra.downcase # ¿Es minúscula?
			alfabeto = $alfabeto_minusculas
			limite = $limite_inferior_minusculas
		end

		valor_ascii = letra.ord
		# Rotar
		nueva_posicion = (valor_ascii - limite + 13) % $longitud_alfabeto
		# Y ver cuál carácter está en esa posición
		cadena_con_rotaciones += alfabeto[nueva_posicion]
	end
	# Regresar nueva cadena
	cadena_con_rotaciones
end

mensaje = "Programando en Ruby desde parzibyte.me"
puts "El mensaje original es '#{mensaje}'"
# El mensaje original es 'Programando en Ruby desde parzibyte.me'
mensaje_cifrado = rot_13 mensaje 
puts "El mensaje cifrado es '#{mensaje_cifrado}'"
# El mensaje cifrado es 'Cebtenznaqb ra Ehol qrfqr cnemvolgr.zr'
mensaje_descifrado = rot_13 mensaje_cifrado
puts "El mensaje descifrado es '#{mensaje_descifrado}'" 
# El mensaje descifrado es 'Programando en Ruby desde parzibyte.me'