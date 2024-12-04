# generate_secrets
Scripts for generating passwords, secrets, and signed API tokens. I use it for building `Flask` apps and APIs.

# Usage
To generate a secret key (i.e. for use in a `Flask` app), run `python generate.py secret_key --nbytes 64`. To generate an API token, run `python generate.py token --app_id sweeper --app_secret_key your_secret_app_key`

# Installation
Besides having Python installed (ideally version `3.9` or higher) there are not many prerequisites. You can install them using the `requirements.txt` by running `pip install -r requirements.txt` in your shell.
