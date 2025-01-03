from enum import StrEnum, auto


__all__ = ["ApiConf", "DbConf"]


class ApiConf(StrEnum):
    ALLOWED_HOSTS = auto()
    DEBUG = auto()
    HOST = auto()
    PORT = auto()
    SECRET_KEY = auto()


class DbConf(StrEnum):
    DB_HOST = auto()
    DB_NAME = auto()
    DB_PASSWORD = auto()
    DB_PORT = auto()
    DB_USER = auto()
