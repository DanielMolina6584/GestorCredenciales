import random
import string

class GeneradorContrasena:
    def __init__(self):
        self.configuracion:dict = {}

    def configurar_contrasena(self):
        longitud:int = int(input("Ingrese la longitud para la contraseña: "))
        usar_letras: str = input("Desea la contra con letras? s/n: ").lower()
        usar_numeros: str = input("Desea la contra con números? s/n: ").lower()

        letra: bool = False
        numero: bool = False
        if usar_letras == 's':
            letra = True
        if usar_numeros == 's':
            numero = True

        if not letra and not numero:
            print("Debe seleccionar al menos una opción")
            return self.configurar_contrasena()

        self.configuracion: dict = {
            'longitud': longitud,
            'usar_letras': letra,
            'usar_numeros': numero
        }
        print("Configuración guardada exitosamente")

    def mostrar_configuracion(self):
        if not self.configuracion:
            print("Configuración actual:")
            print(f"Longitud: {self.configuracion['longitud']}")
            print(f"Usar letras: {'Sí' if self.configuracion['usar_letras'] else 'No'}")
            print(f"Usar números: {'Sí' if self.configuracion['usar_numeros'] else 'No'}")
        else:
            print("No hay configuración guardada")

    def generar_contrasena(self) -> str:
        if not self.configuracion:
            print("No hay configuración.")
            self.configurar_contrasena()

        caracteres:str = ''
        # Se usa la libreria string, la cual puede traer los numeros y letras facilmente
        # Se puede hacer tambien quemando cada letra y numero
        if self.configuracion['usar_letras']:
            caracteres += string.ascii_letters
        if self.configuracion['usar_numeros']:
            caracteres += string.digits

        # La libreria ramdom elige un caracter al azar, y los va uniendo por el join, esto lo hara
        # en el rango de la longitud
        contrasena:str = ''.join(random.choice(caracteres) for _ in range(self.configuracion['longitud']))
        return contrasena

    def menu(self) -> str:
        while True:
            if self.configuracion:
                print("\n======Menú del Generador de Contraseñas======")
                self.mostrar_configuracion()
                opcion:str = input("¿Desea usar esta configuración (s), crear una nueva (n): ").lower()
                if opcion == 's':
                    contrasena:str = self.generar_contrasena()
                    print(f"Su contraseña generada es: {contrasena}")
                    return contrasena
                elif opcion == 'n':
                    self.configurar_contrasena()
                else:
                    print("Opción no válida")
            else:
                self.configurar_contrasena()