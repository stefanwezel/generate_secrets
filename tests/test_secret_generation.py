import pytest
import jwt
import secrets


def generate_token(app_id, app_secret_key):
    token = jwt.encode({"app_id": app_id}, app_secret_key, algorithm="HS256")
    return token


def generate_secret_key():
    return secrets.token_urlsafe(64)


def decode_token(token, app_secret_key):
    try:
        decoded_token = jwt.decode(token, app_secret_key, algorithms=["HS256"])
        return decoded_token["app_id"]
    except jwt.InvalidTokenError:
        return None


def test_generate_token():
    app_id = "test_app"
    app_secret_key = "secret_key"
    token = generate_token(app_id, app_secret_key)
    assert token is not None
    assert isinstance(token, str)


def test_generate_secret_key():
    secret_key = generate_secret_key()
    assert secret_key is not None
    assert isinstance(secret_key, str)


def test_decode_token():
    app_id = "test_app"
    app_secret_key = "secret_key"
    token = generate_token(app_id, app_secret_key)
    decoded_app_id = decode_token(token, app_secret_key)
    assert decoded_app_id == app_id

    invalid_token = "invalid_token"
    decoded_app_id = decode_token(invalid_token, app_secret_key)
    assert decoded_app_id is None
