from credencial import Credencial
from generador_contrasena import GeneradorContrasena

class Gestor:
    def __init__(self):
        self.__credenciales = []
        self.generador_contrasena = GeneradorContrasena()

    def listar_credenciales(self) -> None:
        if len(self.__credenciales) > 0:
            for credencial in self.__credenciales:
                print("Credencial - servicio: ", credencial.servicio)
        else:
            print("No hay ninguna credencial")

    def crear_credencial(self) -> Credencial:
        print("Creando credencial")
        servicio: str = input("Agregar el servicio: ")
        usuario: str = input("Agregar el usuario: ")

        print("1. Generar contrasena automatica")
        print("2. Crear mi propia contrasena")
        opcion_contra:int = int(input("Elija una opcion: "))
        if opcion_contra == 1:
            contrasena = self.generador_contrasena.menu()
        elif opcion_contra == 2:
            contrasena:str = input("Agregar la contraseña: ")
        else:
            print("Se le generara una Contrasena automatica")
            contrasena = self.generador_contrasena.menu()

        credencial: Credencial = Credencial(
            in_servicio=servicio,
            in_usuario=usuario,
            in_contrasena=contrasena
        )
        print("Credencial creada!")
        return credencial

    def agregar_credencial(self, credencial: Credencial) -> None:
        self.__credenciales.append(credencial)
        print("Credencial agregada!")

    def buscar_credencial(self) -> None:
        while True:
            servicio_a_encontrar: str = input("Escribe el servicio que vas a buscar o escribe 'salir' para volver al menú: ").lower()

            if servicio_a_encontrar.lower() == 'salir':
                break

            encontrado = False
            for credencial in self.__credenciales:
                if credencial.servicio.lower() == servicio_a_encontrar:
                    usuario:str = credencial._Credencial__usuario
                    contrasena:str = credencial._Credencial__contrasena
                    print(f"Credencial encontrada: Usuario: {usuario}, Contraseña: {contrasena}")
                    encontrado = True
                    break

            if encontrado:
                break
            else:
                print("No se encontró ninguna credencial, intente de nuevo si quiere")
