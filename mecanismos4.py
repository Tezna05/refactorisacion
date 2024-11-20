# Clase base
class PaymentMethod:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

# Clases derivadas para cada método de pago
class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class BitcoinPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing Bitcoin payment of ${amount}")

# Lista de métodos de pago
payments = [
    CreditCardPayment(),
    PayPalPayment(),
    BitcoinPayment()
]

# Procesar pagos usando polimorfismo
for payment in payments:
    payment.process_payment(100)  # Puedes cambiar el monto según sea necesario
