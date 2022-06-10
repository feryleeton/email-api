from starlette.config import Config

config = Config(".env")

DB_ENDPOINT_WRITER = config('DB_ENDPOINT_WRITER', cast=str, default='')
DB_ENDPOINT_READER = config('DB_ENDPOINT_READER', cast=str, default='')

DB_NAME = config('DB_NAME', cast=str, default='')
DB_USER = config('DB_USER', cast=str, default='')
DB_PORT = config('DB_PORT', cast=str, default='')
DB_PASSWORD = config('DB_PASSWORD', cast=str, default='')

