from pydantic.v1 import BaseSettings, root_validator
from secrets import token_bytes
from base64 import b64encode


class Settings(BaseSettings):
    DB_HOST:str
    DB_PORT:int
    DB_USER:str
    DB_PASS:str
    DB_NAME:str

    @root_validator
    def get_database_url(cls, values):
        values["DATABASE_URL"] =  f"postgresql+asyncpg://{values['DB_USER']}:{values['DB_PASS']}@{values['DB_HOST']}:{values['DB_PORT']}/{values['DB_NAME']}"
        return values
    
    KEY: str
    ALGORITHM: str

    class Config:
        env_file = ".env"

settings = Settings()
