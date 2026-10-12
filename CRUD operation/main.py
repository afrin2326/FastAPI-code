from fastapi import FastAPI,Path,HTTPException
import json

app = FastAPI()

#Load patiennts data
def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)

    return data

@app.get("/")
def hello():
    return {'message ':'Patients Management System API'}
    

@app.get("/about")
def about():
    return{'message':'A Fully Functional API to Manage Patients Records'}

@app.get("/view")
def  view():
    data=load_data()
    return data


