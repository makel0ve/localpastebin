# import os

# from dotenv import load_dotenv


# load_dotenv()


# ACCESS_KEY_ID = os.environ.get("ACCESS_KEY_ID")
# SECRET_KEY = os.environ.get("SECRET_KEY")
# REGION = os.environ.get("REGION")
# ENDPOINT_URL = os.environ.get("ENDPOINT_URL")
# SERVICE_NAME = os.environ.get("SERVICE_NAME")
# BUCKET_NAME = os.environ.get("BUCKET_NAME")
# FILE_URL = os.environ.get("FILE_URL")

from pydantic_settings import BaseSettings, SettingsConfigDict


class VKCloudSettings(BaseSettings):
    ACCESS_KEY_ID: str
    SECRET_KEY: str
    REGION: str
    ENDPOINT_URL: str
    SERVICE_NAME: str
    BUCKET_NAME: str
    FILE_URL: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


vkcloud_settings = VKCloudSettings()