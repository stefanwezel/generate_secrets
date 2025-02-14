# generate_secrets
Scripts for generating passwords, secrets, and signed API tokens. I use it for building `Flask` apps and APIs.

# Usage
To generate a secret key (i.e. for use in a `Flask` app), run `python generate.py url_safe_token --nbytes 64`. To generate an API token, run `python generate.py token --app_id sweeper --app_url_safe_token your_secret_app_key`. To generate a Fernet key, use `python generate.py fernet_key`. Run `python generate.py -h` to see all subcommands.

# Installation
Besides having Python installed (ideally version `3.9` or higher) there are not many prerequisites. You can install them using the `requirements.txt` by running `pip install -r requirements.txt` in your shell. Run `pytest` to ensure everything works.
