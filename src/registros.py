def registro_contacto(nombre, numero):
    if not isinstance(nombre, str):
        return "Error: El nombre debe ser texto"
    if not isinstance(numero, int) or len(str(numero)) != 10:
        return "Error: El número de teléfono debe tener exactamente 10 dígitos numéricos"
    
    return {"nombre": nombre, "telefono": numero}