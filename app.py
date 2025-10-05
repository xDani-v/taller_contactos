from src.registros import registro_contacto
from src.buscar import buscar_contacto
from src.save import guardar_agenda, obtener_agenda

def ejecutar():
    registro = registro_contacto("Pablo", "0989009423")
    guardar_agenda("Pablo", "0989009423")
    registro_guardado = obtener_agenda("Pablo")
    print(f"Dato guardado recuperado: {registro_guardado}")
    print("Flujo de operaciones completado.")
    print("Flujo de operaciones completado.")
    print("pruebas")

if __name__ == "__main__":
    ejecutar()
