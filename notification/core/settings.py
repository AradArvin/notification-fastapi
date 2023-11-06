from fastapi_mail import ConnectionConfig
from decouple import config

FASTAPI_MAIL_CONF = ConnectionConfig(
    MAIL_USERNAME = config("EMAIL_USERNAME"),
    MAIL_PASSWORD = config("EMAIL_PASSWORD"),
    MAIL_FROM = config("EMAIL_FROM"),
    MAIL_PORT = config("EMAIL_PORT"),
    MAIL_SERVER = config("EMAIL_SERVER"),
    MAIL_FROM_NAME=config("EMAIL_FROM_NAME"),
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)


REDIS_HOST_ADDRESS = "redis://127.0.0.1:6379/1"

DATA_ADDRESS = "http://127.0.0.1:8000/data"