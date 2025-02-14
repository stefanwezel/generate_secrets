import jwt
import secrets
import argparse
from cryptography.fernet import Fernet


def generate_token(app_id, app_url_safe_token):
    """ Encode the payload as JSON Web Token. """
    token = jwt.encode({"app_id": app_id}, app_url_safe_token, algorithm="HS256")
    return token


def generate_url_safe_token(nbytes):
    """ Return a random URL-safe text string, containing nbytes random bytes. """
    return secrets.token_urlsafe(nbytes)


def generate_fernet_key():
    """ Generates A URL-safe base64-encoded 32-byte key. """
    return Fernet.generate_key()


def main():
    parser = argparse.ArgumentParser(description="Generate JWT token or secret key")
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    generate_token_parser = subparsers.add_parser("token")
    generate_token_parser.add_argument(
        "--app_id", type=str, required=True, help="The application ID"
    )
    generate_token_parser.add_argument(
        "--app_url_safe_token",
        type=str,
        required=True,
        help="The application secret key",
    )

    generate_url_safe_token_parser = subparsers.add_parser("url_safe_token")
    generate_url_safe_token_parser.add_argument(
        "--nbytes",
        type=int,
        default=64,
        help="Number of characters the secret will have",
    )

    generate_url_safe_token_parser = subparsers.add_parser("fernet_key")

    args = parser.parse_args()

    if args.subcommand == "token":
        token = generate_token(args.app_id, args.app_url_safe_token)
        print(token)
    elif args.subcommand == "url_safe_token":
        url_safe_token = generate_url_safe_token(args.nbytes)
        print(url_safe_token)
    elif args.subcommand == "fernet_key":
        fernet_key = generate_fernet_key()
        print(fernet_key)
    else:
        print(
            "Invalid subcommand. Check `python generate.py -h` for valid subcommands."
        )


if __name__ == "__main__":
    main()
