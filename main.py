from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def base():
    return "Hello FastAPI"

@app.get('/student/{student_id}')
def base(student_id):
    return f"Student id is {student_id} & it's type is : {type(student_id)}"

@app.get('/add')
def base(x:int, y:int):
    return f"x = {x} and y = {y} and x + y = {x+y}"

@app.get('/multiply')
def base(x:int=4, y:int=6):
    return f"x = {x} and y = {y} and x * y = {x*y}"

