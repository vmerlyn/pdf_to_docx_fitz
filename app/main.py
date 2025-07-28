from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.routes.convert import router as convert_router

import shutil
from app.config import UPLOAD_DIR
import shutil

# Clean uploads folder at startup
for item in UPLOAD_DIR.iterdir():
    if item.is_file():
        item.unlink()
    elif item.is_dir():
        shutil.rmtree(item)

# Clean uploads/ folder at startup
for item in UPLOAD_DIR.iterdir():
    if item.is_file():
        item.unlink()
    elif item.is_dir():
        shutil.rmtree(item)


app = FastAPI()
app.include_router(convert_router)


@app.get("/", response_class=HTMLResponse)
async def homepage():
    return """
    <html>
    <head><title>PDF to DOCX</title></head>
    <body>
        <h1>Upload PDF</h1>
        <form method="post" enctype="multipart/form-data" action="/convert">
            <input type="file" name="file">
            <input type="submit" value="Convert">
        </form>
    </body>
    </html>
    """
