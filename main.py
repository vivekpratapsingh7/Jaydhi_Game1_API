from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

# Load dataset
df = pd.read_csv("ml101_cleaned_chatbot_dataset.csv")
df["Item"] = df["Item"].str.lower()

# FastAPI app
app = FastAPI()

# Request schema
class ItemRequest(BaseModel):
    item: str

# Route
@app.post("/chat")
def get_label(request: ItemRequest):
    item = request.item.strip().lower()
    match = df[df["Item"] == item]

    if not match.empty:
        return {"label": match["Label"].values[0]}
    else:
        raise HTTPException(status_code=404, detail="Unknown item")
