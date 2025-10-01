from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
async def root():
    return FileResponse(r"F:\Phyton\fast_api\1.html")

