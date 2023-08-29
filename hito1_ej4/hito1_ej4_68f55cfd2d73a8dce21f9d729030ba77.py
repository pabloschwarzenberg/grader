def dec_to(num, sistema = 2):
  valores_hexa = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
  if (sistema > 1 and sistema < 17):
    valor_ret = []
    while num:
      num, residuo = divmod(num, sistema)
      valor_ret.append(valores_hexa[residuo]) if (residuo > 9) else valor_ret.append(str(residuo))
    return ''.join(valor_ret[::-1])
  return 'Verifica que el sistema al que deseas convertir sea válido'
  