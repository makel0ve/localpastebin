import io

from aiobotocore.session import get_session

from vkcloud.vkcloud_config import vkcloud_settings


async def upload_string_async(string_data, now):
    session = get_session()

    async with session.create_client(
        service_name=vkcloud_settings.SERVICE_NAME,
        endpoint_url=vkcloud_settings.ENDPOINT_URL,
        aws_access_key_id=vkcloud_settings.ACCESS_KEY_ID,
        aws_secret_access_key=vkcloud_settings.SECRET_KEY,
        region_name=vkcloud_settings.REGION
    ) as s3_client:
        test_bucket_name = vkcloud_settings.BUCKET_NAME  

        data = io.BytesIO(string_data.encode('utf-8'))

        await s3_client.put_object(Bucket=test_bucket_name, Key=f'{now}.txt', Body=data)

    return f"{vkcloud_settings.FILE_URL}{now}.txt"