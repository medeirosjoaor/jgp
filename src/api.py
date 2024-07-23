import json

import pandas as pd
from fastapi import FastAPI

app = FastAPI()


def parse_csv(df: pd.DataFrame):
    res = df.to_json(orient="records")
    parsed = json.loads(res)
    return parsed


@app.get("/items")
def get_items():
    df = pd.read_csv("data.csv")

    df.drop(
        columns=["All items, less food and energy", "Gasoline (all types)"],
        inplace=True,
    )

    df.rename(columns={"Date": "date", "All items": "value"}, inplace=True)

    return parse_csv(df)


@app.get("/items-less-food-and-energy")
def get_items_less_food_and_energy():
    df = pd.read_csv("data.csv")

    df.drop(
        columns=["All items", "Gasoline (all types)"],
        inplace=True,
    )

    df.rename(
        columns={"Date": "date", "All items, less food and energy": "value"},
        inplace=True,
    )

    return parse_csv(df)


@app.get("/gasoline")
def get_gasoline():
    df = pd.read_csv("data.csv")

    df.drop(
        columns=["All items", "All items, less food and energy"],
        inplace=True,
    )

    df.rename(columns={"Date": "date", "Gasoline (all types)": "value"}, inplace=True)

    return parse_csv(df)
