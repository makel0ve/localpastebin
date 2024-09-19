# import os

# from dotenv import load_dotenv


# load_dotenv()


# HASH_ALPHABET = os.environ.get("HASH_ALPHABET")


from pydantic_settings import BaseSettings, SettingsConfigDict


class HashSettings(BaseSettings):
    HASH_ALPHABET: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


hash_settings = HashSettings()
