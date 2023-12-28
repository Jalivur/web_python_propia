
import reflex as rx
import string
import secrets


class NumberInputState(rx.State):
    number: int = 6
    contrasena:str



    def generar_contrasena(self,):
        longitud = self.number
        if longitud and int(longitud) >= 3:
            longitud = int(longitud) - 3
            caracteres = string.ascii_letters + string.digits + string.punctuation
            contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
            mayuscula = secrets.choice(string.ascii_uppercase)
            minuscula = secrets.choice(string.ascii_lowercase)
            numero = secrets.choice(string.digits)
            self.contrasena = mayuscula + minuscula + contrasena + numero

