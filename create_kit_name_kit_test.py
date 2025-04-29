import data
import sender_stand_request


def get_new_user_token():
    response = sender_stand_request.post_new_user()
    assert response.status_code == 201
    return response.json()["authToken"]


def get_kit_body(name_value, card_id=None):
    body = {"name": name_value}
    if card_id is not None:
        body["cardId"] = card_id
    return body


# Funciones de aserción
def positive_assert(kit_body):
    token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


def negative_assert_400(kit_body):
    token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 400


def negative_assert_no_name():
    token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit({}, token)
    assert response.status_code == 400
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"


# ✅ PRUEBAS POSITIVAS
def test_kit_1_char():
    positive_assert(get_kit_body("a"))


def test_kit_511_chars():
    positive_assert(get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"))


def test_kit_special_characters():
    positive_assert(get_kit_body("№%@,."))


def test_kit_with_spaces():
    positive_assert(get_kit_body(" A Aaa "))


def test_kit_with_numbers():
    positive_assert(get_kit_body("123"))


def test_kit_with_card_id_only():
    token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(get_kit_body("Kit con tarjeta", card_id=1), auth_token=None)
    assert response.status_code == 201
    assert response.json()["name"] == "Kit con tarjeta"


# ❌ PRUEBAS NEGATIVAS
def test_kit_0_chars():
    negative_assert_400(get_kit_body(""))


def test_kit_512_chars():
    negative_assert_400(get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"))


def test_kit_missing_name():
    negative_assert_no_name()


def test_kit_number_type_name():
    token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit({"name": 123}, token)
    assert response.status_code == 400


# ✅ GET
def test_get_user_kits():
    token = get_new_user_token()
    response = sender_stand_request.get_user_kits(token)
    assert response.status_code == 200


# ✅ PUT
def test_update_kit():
    token = get_new_user_token()
    create_resp = sender_stand_request.post_new_client_kit(get_kit_body("Original kit"), token)
    kit_id = create_resp.json()["id"]
    update_resp = sender_stand_request.put_update_kit(kit_id, "Kit actualizado", token)
    assert update_resp.status_code == 200
    assert update_resp.json()["name"] == "Kit actualizado"


# ✅ DELETE
def test_delete_kit():
    token = get_new_user_token()
    create_resp = sender_stand_request.post_new_client_kit(get_kit_body("Kit temporal"), token)
    kit_id = create_resp.json()["id"]
    delete_resp = sender_stand_request.delete_kit(kit_id, token)
    assert delete_resp.status_code in [200, 204]
