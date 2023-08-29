# completa el código de la función
class Cuenta(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, nombre, saldo=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.nombre= nombre
        self.saldo = saldo

    def girar(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.saldo:
            return False
        else:
            self.saldo -= amount
            return True