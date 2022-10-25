from datetime import datetime
from typing import Dict
from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn
from ast import Num

app = FastAPI()

accounts = []

class Account(BaseModel):
    id: int
    nome: str
    documento: str
    dataNascimento: str
    email: str
    telefone: str


@app.get("/")
def root() -> str:
    return {"New" : "Life Bank"}


@app.get("/health/")
def alive() -> Dict[str, datetime]:
    return {"timestamp": datetime.now()}
    

@app.post("/accounts", response_model=bool, tags=["accounts"])
def create_account(account: Account):

    accounts.append(account)

    return True


@app.get("/accounts", response_model=list, tags=["accounts"])
def get_accounts():

    return accounts 


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)


