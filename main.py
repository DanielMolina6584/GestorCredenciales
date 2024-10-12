from gestor import Gestor
from credencial import Credencial
class Main:
    @staticmethod
    def run():
        _PASSWORD_SYSTEM:str = "123"
        intentos:int = 3
        gestor:Gestor = Gestor()
        credencial: Credencial = None
        print("Sistema GC")
        while(intentos > 0):
            password:str = input("Ingrese contraseña del sistema: ")
            if password == _PASSWORD_SYSTEM:
                print("Inicio de sesion")
                salida:bool = True
                while salida:
                    print("=======Modulos=======")
                    print("0 -> Listar Credenciales")
                    print("1 -> Crear Credencial")
                    print("2 -> Agregar Credencial")
                    print("3 -> Buscar Credencial")
                    print("4 -> Salir")
                    print("=====================")
                    opcion:str = input("Seleccione modulo: ")

                    match opcion:   
                        case "0":
                            gestor.listar_credenciales()
                        case "1":
                            credencial = gestor.crear_credencial()
                        case "2":
                            if credencial is None:
                                print("No hay credencial")
                            else:
                                gestor.agregar_credencial(credencial)
                                credencial = None
                        case "3": 
                            gestor.buscar_credencial()
                        case "4": 
                            print("Saliendo del sistema!")
                            intentos = 3
                            salida = False
                        case _: 
                            print("Opcion no valida!")
            else:
                intentos -= 1
                print(f"Intentos {intentos}")
                

Main.run()
        
    
