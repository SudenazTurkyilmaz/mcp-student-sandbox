import os


AWS_SECRET_KEY_ENV_VAR = "AWS_SECRET_KEY"


def get_aws_secret_key():
    secret_key = os.getenv(AWS_SECRET_KEY_ENV_VAR)
    if not secret_key:
        raise ValueError(
            f"Missing required environment variable: {AWS_SECRET_KEY_ENV_VAR}"
        )
    return secret_key


def mask_secret(secret_key):
    return "*" * max(len(secret_key) - 4, 0) + secret_key[-4:]


def connect():
    secret_key = get_aws_secret_key()
    print(f"Connecting with key: {mask_secret(secret_key)}")
