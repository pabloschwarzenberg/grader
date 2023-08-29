ALLOWED_USER = '10334151'
ALLOWED_USER_PASSWORD = '1803'
should_exit = False
while not should_exit:
  balance = 1000000
  user_balance = 100000
  
  user = ''
  while user != ALLOWED_USER:
    user = input('Ingrese usuario: ')
  
  failed_attempts = 0
  password = input('Ingrese contraseña: ')
  while password != ALLOWED_USER_PASSWORD:
    failed_attempts += 1
    print('contraseña invalida')
    if failed_attempts == 3:
      print('tarjeta bloqueada')
      should_exit = True
      break
    password = input('Ingrese contraseña: ')
  
  if not should_exit:  
    withdraw = input('Monto a retirar: ')
    if withdraw != 'N' and not withdraw.isnumeric():
      should_exit = True
      withdraw = -1
    else:
      withdraw = int(withdraw)
    while withdraw <= user_balance and withdraw >= 0:
      user_balance -= withdraw
      balance -= withdraw
      print('saldo cuenta=', user_balance)
      print('saldo cajero=', balance)
      withdraw = input('Monto a retirar: ')
      if withdraw != 'N' and not withdraw.isnumeric():
        should_exit = True
        withdraw = -1
      else:
        withdraw = int(withdraw)
