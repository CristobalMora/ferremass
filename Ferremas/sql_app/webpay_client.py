import transbank
from transbank.webpay.webpay_plus.transaction import Transaction

# Configuración del ambiente y las credenciales de Webpay en modo de pruebas
transbank.webpay.webpay_plus.webpay_plus_commerce_code = '597055555532'
transbank.webpay.webpay_plus.webpay_plus_api_key = '579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C'
transbank.webpay.webpay_plus.webpay_plus_integration_type = 'TEST'  # Modo de pruebas

def create_transaction(amount, session_id, buy_order, return_url):
    transaction = Transaction()
    response = transaction.create(buy_order, session_id, amount, return_url)
    return response

def commit_transaction(token):
    transaction = Transaction()
    response = transaction.commit(token)
    return response
