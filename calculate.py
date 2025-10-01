 # calculate.py
from fastapi import FastAPI, Body
from fastapi.responses import FileResponse
 
my_api = FastAPI()
 
@my_api.get("/")
def root():
    return FileResponse(r"F:\Phyton\api_edu\calc.html")
 
@my_api.post("/calculate")
def calculate(first_num = Body(embed=True), second_num = Body(embed=True)):
    return {"message": f"{int(first_num) + int(second_num)} "}
