import jwt
import secrets
import argparse


def generate_token(app_id, app_secret_key):
    token = jwt.encode({"app_id": app_id}, app_secret_key, algorithm="HS256")
    return token


def generate_secret_key(nbytes):
    return secrets.token_urlsafe(nbytes)


def main():
    parser = argparse.ArgumentParser(description="Generate JWT token or secret key")
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    generate_token_parser = subparsers.add_parser("token")
    generate_token_parser.add_argument(
        "--app_id", type=str, required=True, help="The application ID"
    )
    generate_token_parser.add_argument(
        "--app_secret_key", type=str, required=True, help="The application secret key"
    )

    generate_secret_key_parser = subparsers.add_parser("secret_key")
    generate_secret_key_parser.add_argument(
        "--nbytes",
        type=int,
        default=64,
        help="Number of characters the secret will have",
    )

    args = parser.parse_args()

    if args.subcommand == "token":
        token = generate_token(args.app_id, args.app_secret_key)
        print(token)
    elif args.subcommand == "secret_key":
        secret_key = generate_secret_key(args.nbytes)
        print(secret_key)
    else:
        print("Invalid subcommand. Choose 'token' or 'secret_key'")


if __name__ == "__main__":
    main()
