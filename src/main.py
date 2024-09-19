from datetime import datetime

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from hash.hash import create_custom_hash
from vkcloud.vkcloud import upload_string_async
from database.db_helper import add_data


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
tempaltes = Jinja2Templates(directory="templates")


@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
    return tempaltes.TemplateResponse(request, "main.html")


@app.post('/share_url')
async def share_url(request: Request):
    now = datetime.utcnow()
    data = await request.json()
    textarea = data.get("text")
    endlife = datetime.strptime(data.get("endlife"), "%Y-%m-%dT%H:%M:%S.%fZ")

    file_url = await upload_string_async(textarea, now)

    hashid = await create_custom_hash(file_url)

    await add_data(url=file_url, hashid=hashid, start_life=now, end_life=endlife)

    return {"name": hashid}


if __name__ == "__main__":
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)