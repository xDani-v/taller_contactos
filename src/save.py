registros = {}

def guardar_agenda(nombre, numero):
    registros[nombre] = numero
    
def obtener_agenda(nombre):
    return registros.get(nombre, None)