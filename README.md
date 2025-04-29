# Proyecto Urban Grocers 

## Descripción

Este proyecto automatiza la validación del campo `name` en la creación de kits de productos para usuarios en la aplicación Urban Grocers, siguiendo la lista de comprobación oficial del Sprint 7.

## Estructura de Archivos

- `configuration.py` → URL base y rutas.
- `data.py` → Cuerpos de solicitud POST para usuarios y kits.
- `sender_stand_request.py` → Funciones para enviar solicitudes a la API.
- `create_kit_name_kit_test.py` → Pruebas automáticas usando Pytest.
- `.gitignore` → Archivos y carpetas ignoradas por Git.
- `README.md` → Instrucciones del proyecto.

## Requisitos

- Python 3.8 o superior
- `pytest`
- `requests`

Instala dependencias:

```bash
pip install pytest requests

## Notas sobre pruebas que fallan

- Algunas pruebas como `test_kit_0_chars` o `test_kit_512_chars` fallan porque el backend acepta datos incorrectos (bug conocido).
- Las pruebas relacionadas con métodos PUT, DELETE y GET pueden responder con error 404 si el servidor no tiene esos endpoints habilitados.