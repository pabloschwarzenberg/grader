#Conversión de Decimal a Binario
num_str = input("Please give me a integer: ")

num_int = int(num_str)

num_bin_reversed = ''

while num_int > 0:

       if num_int % 2 == 0:
           num_int = int(num_int / 2)
           num_remainder = 1
           print("The remainder is:", 0)
           num_bin_reversed += '0'

       elif num_int % 2 == 1:
           num_int = int(num_int / 2)
           num_remainder = 1
           print("The remainder is:", 1)
           num_bin_reversed += '1'

num_bin = num_bin_reversed[::-1]
if int(num_str) > 0:
     assert '0b' + num_bin == bin(int(num_str))