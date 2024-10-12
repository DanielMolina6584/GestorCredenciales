class Credencial:
    servicio: str
    __usuario: str
    __contrasena: str

    def __init__(self, in_servicio:str, in_usuario:str, in_contrasena:str):
        self.servicio = in_servicio
        self.__usuario = in_usuario
        self.__contrasena = in_contrasena
