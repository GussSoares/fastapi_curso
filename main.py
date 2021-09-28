import yfinance as yf
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from sqlmodel import create_engine, Session, SQLModel

from utils import functions
from models import Finance

app = FastAPI()

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)


@app.get("/finance")
def get(tickers: str, start: str, end: str):
    a = yf.download(" ".join(tickers.split(" ")), start=start, end=end)

    pos_data = functions.postprocess(a, tickers.split(" "))

    data = Finance(tickers=tickers, start=start, end=end)

    with Session(engine) as session:
        session.add(data)
        session.commit()

    return jsonable_encoder(pos_data)
