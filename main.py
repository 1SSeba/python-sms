import vonage

# Credenciales de Vonage
api_key = 'apikey'
api_secret = 'secretkey'

# Crear un cliente de Vonage
client = vonage.Client(key=api_key, secret=api_secret)
sms = vonage.Sms(client)

# Enviar un SMS
try:
    response = sms.send_message({
        'from': 'VonageAPI',  # Nombre o número de teléfono del remitente (debe ser verificado)
        'to': '+569xxxxxxxx',  # Número de teléfono del destinatario
        'text': 'Este es un mensaje de prueba enviado desde Python usando Vonage!',
    })

    # Verificar la respuesta
    if response['messages'][0]['status'] == '0':
        print("Mensaje enviado con éxito")
    else:
        print(f"Error al enviar el mensaje: {response['messages'][0]['error-text']}")
except Exception as e:
    print(f"Error al enviar el mensaje: {e}")
