import pytest
import jwt
import secrets
from cryptography.fernet import Fernet
from ..generate import generate_token, generate_url_safe_token, generate_fernet_key


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


def test_generate_url_safe_token():
    secret_key = generate_url_safe_token(32)
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


def test_fernet_encryption():
    key = generate_fernet_key()
    f = Fernet(key)
    secret = b"my test secret"
    token = f.encrypt(secret)
    decrypted = f.decrypt(token)
    assert decrypted == secret
