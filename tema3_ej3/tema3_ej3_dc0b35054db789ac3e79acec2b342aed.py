class Cuenta:
  # Definir el constructor de la clase
  def __init__(self, rut, saldo):
    # Inicializar los atributos de la clase
    self.rut = rut
    self.saldo = saldo

  # Definir el método girar de la clase
  def girar(self, monto):
    # Validar que el monto a girar sea menor o igual que el saldo de la cuenta
    if monto <= self.saldo:
      # Restar el monto al saldo de la cuenta
      self.saldo -= monto
      # Retornar True para indicar que el giro se pudo realizar
      return True
    else:
      # Retornar False para indicar que el giro no se pudo realizar
      return False
    