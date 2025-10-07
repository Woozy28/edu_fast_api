# main.py
import uvicorn
from fastapi import FastAPI
import logger
import config
import models

app = FastAPI()

user = models.User(name="John Doe", id=1)


# Гет к корневому каталогу.
@app.get("/")  
def read_root():
    return {"message": "Hello, World!"}

@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}

@app.get("/users", response_model= models.User)
def read_user_info():
    return user

@app.post("/user")
def new_user(user: models.User):
    if user.age >=18:
        user.is_adult = True
    return user
    

@app.get("/db")
def get_db_info():
    logger.info(f"Connecting to database: {config.db.database_url}")
    return {"database_url": config.db.database_url}                  


from config import load_config

config = load_config()

if config.debug:
    app.debug = True
else:
    app.debug = False


# запускаем сервак увикорн 
if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)    