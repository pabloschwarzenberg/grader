number_one = int(input('Enter the first number:'))
number_two = int(input('Enter the second number:'))
div, sum1, sum2 = 1,0,0
while div <= number_one / 2:
    if number_one % div == 0:
        sum1 += div
    div += 1
div = 1 # let's return the divisor to 1
while div <= number_two / 2:
    if number_two% div == 0:
        sum2 += div
    div += 1
if sum1 == number_two and sum2 == number_one:
    print ('The numbers are friendly!')
else:
    print ('The numbers are not friendly!')