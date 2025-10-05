
from src.registros import registro_contacto
from src.buscar import buscar_contacto

def test_registro_contacto_valido():
    # Tu función exige numero "int" y exactamente 10 dígitos al convertirlo a str.
    contacto = registro_contacto("Juan Perez", 9876543210)  # 10 dígitos
    assert isinstance(contacto, dict)
    assert contacto["nombre"] == "Juan Perez"
    assert contacto["telefono"] == 9876543210

def test_registro_contacto_nombre_invalido():
    # Debe devolver el mensaje de error definido en tu función
    msg = registro_contacto(123, 9876543210)
    assert isinstance(msg, str)
    assert "El nombre debe ser texto" in msg

def test_registro_contacto_numero_invalido_tipo():
    msg = registro_contacto("Maria", "0987654321")  # str (tu función espera int)
    assert isinstance(msg, str)
    assert "debe tener exactamente 10 dígitos" in msg

def test_registro_contacto_numero_invalido_longitud():
    msg = registro_contacto("Carlos", 12345)  # menos de 10 dígitos
    assert isinstance(msg, str)
    assert "debe tener exactamente 10 dígitos" in msg

def test_buscar_contacto_encontrado():
    lista = [
        {"nombre": "Ana Lopez", "telefono": 1111111111},
        {"nombre": "Juan Perez", "telefono": 9876543210},
    ]
    res = buscar_contacto(lista, "juan")
    # Tu función devuelve el diccionario del contacto cuando encuentra coincidencia (case-insensitive)
    assert isinstance(res, dict)
    assert res["nombre"] == "Juan Perez"
    assert res["telefono"] == 9876543210

def test_buscar_contacto_no_encontrado():
    lista = [{"nombre": "Ana Lopez", "telefono": 1111111111}]
    res = buscar_contacto(lista, "carlos")
    # Tu función devuelve este string cuando no encuentra
    assert isinstance(res, str)
    assert res == "Contacto no encontrado"
