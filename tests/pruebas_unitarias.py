from src.registros import registro_contacto

def test_nombre_no_texto():
    resultado = registro_contacto(123, 9876543210)
    assert resultado == "Error: El nombre debe ser texto"

def test_numero_no_entero():
    resultado = registro_contacto("Juan", "9876543210")
    assert resultado == "Error: El número de teléfono debe tener exactamente 10 dígitos numéricos"

def test_numero_menor_10_digitos():
    resultado = registro_contacto("Juan", 98765432)
    assert resultado == "Error: El número de teléfono debe tener exactamente 10 dígitos numéricos"

def test_numero_mayor_10_digitos():
    resultado = registro_contacto("Juan", 9876543210123)
    assert resultado == "Error: El número de teléfono debe tener exactamente 10 dígitos numéricos"

def test_registro_valido():
    resultado = registro_contacto("Ana", 9876543210)
    assert resultado == {"nombre": "Ana", "telefono": 9876543210}

