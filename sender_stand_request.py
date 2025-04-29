# sender_stand_request.py

import configuration
import requests
import data


def post_new_user(user_body=data.user_body.copy()):
    """
    Crea un nuevo usuario y devuelve la respuesta.
    """
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=user_body,
        headers=data.headers
    )


def post_new_client_kit(kit_body, auth_token):
    """
    Crea un nuevo kit para un usuario autenticado usando su token.
    """
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"

    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
        json=kit_body,
        headers=headers
    )


def get_user_kits(auth_token):
    """
    Recupera todos los kits de un usuario autenticado.
    """
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"

    return requests.get(
        configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
        headers=headers
    )


def put_update_kit(kit_id, new_name, auth_token):
    """
    Actualiza el nombre de un kit específico.
    """
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"

    return requests.put(
        f"{configuration.URL_SERVICE + configuration.CREATE_KIT_PATH}/{kit_id}",
        json={"name": new_name},
        headers=headers
    )


def delete_kit(kit_id, auth_token):
    """
    Elimina un kit específico.
    """
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"

    return requests.delete(
        f"{configuration.URL_SERVICE + configuration.CREATE_KIT_PATH}/{kit_id}",
        headers=headers
    )

