from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app=FastAPI()

class Detail(BaseModel):
    id:int
    name:str
    address:str
    age:int
    gender:str

Details:List[Detail]=[]  


@app.get("/")
def read_root():
    return{'massage':'welcome to our website'}
@app.get('/detail')
def data():
    return Details

@app.post("/detail")
def add_data(detail:Detail):
    Details.append(detail)
    return detail

@app.put("/detail/{detail_id}")
def updata_data(detail_id:int ,updata_detail:Detail):
    for index, detail in enumerate(Details):
        if detail.id==detail_id:
            return updata_data
        
    return{"error":"data not fount"}      

details = []  # example global list to store data

@app.delete("/detail/{detail_id}")
def delete_data(detail_id: int):
    for index, detail in enumerate(details):
        if detail.id == detail_id:
            del details[index]
            return {"message": "Data deleted successfully"}
    return {"message": "Data not found"}
