import reflex as rx
from cryptography.fernet import Fernet

class MsgInputState(rx.State):
    msg: str
    clave:str
    msghas:str



    def generar_clave(self):
        clave=Fernet.generate_key()
        self.clave=clave.decode()
        print(self.clave)

    def encriptar(self):
        self.generar_clave()
        cipher_suite = Fernet(self.clave.encode())
        self.msghas=cipher_suite.encrypt(self.msg.encode()).decode()
        print(self.msghas)

    def desencriptar(self):
        cipher_suite = Fernet(self.clave.encode())
        self.msg=cipher_suite.decrypt(self.msghas.encode()).decode()
    def limpiar(self):
        self.msg=""
        self.clave=""
        self.msghas=""