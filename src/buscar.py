def buscar_contacto(lista_contactos, nombre):
    for contacto in lista_contactos:
        if contacto["nombre"].lower() == nombre.lower():
            return contacto
    return "Contacto no encontrado"
