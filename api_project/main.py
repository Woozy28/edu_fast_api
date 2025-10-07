# main.py
import uvicorn
from fastapi import FastAPI


app = FastAPI()

# Гет к корневому каталогу.
@app.get("/")  
def read_root():
    return {"message": "Hello, World!"}

@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}

                  

# запускаем сервак увикорн 
if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8066, reload=True)