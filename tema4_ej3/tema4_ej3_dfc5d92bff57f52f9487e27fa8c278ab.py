def jerigonzo(string):
  sup = ''
  vocal = ['a','e','i','o','u',
           'A','E','I','O','U',
           'á','é','í','ó','ú',
           'Á','É','Í','Ó','Ú']
  for letra in string:
    if not vocal == letra:
      sup += letra
    else:
      sup += letra + 'p' + letra
  return sup      