import reflex as rx
from cryptography.fernet import Fernet

class MsgInputState(rx.State):
    msg_in: str
    msg_out:str
    clave_in:str
    clave_out:str
    msghas_in:str
    msghas_out:str



    def generar_clave(self):
        clave=Fernet.generate_key()
        self.clave_out=clave.decode()

    def encriptar(self):
        self.generar_clave()
        cipher_suite = Fernet(self.clave_out.encode())
        self.msghas_out=cipher_suite.encrypt(self.msg_in.encode()).decode()

    def desencriptar(self):
        cipher_suite = Fernet(self.clave_in.encode())
        self.msg_out=cipher_suite.decrypt(self.msghas_in.encode()).decode()
    def limpiar(self):
        self.msg_in=""
        self.msg_out=""
        self.clave_in=""
        self.clave_out=""
        self.msghas_in=""
        self.msghas_out=""