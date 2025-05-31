from fastapi import FastAPI
import redis
from datetime import datetime
import random

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
app = FastAPI()

@app.get("/ai")
def ai_rebalance():
    for key in r.scan_iter("stake:*"):
        uid = key.split(":")[1]
        stake = int(r.get(key) or 0)
        change = round(stake * (random.uniform(-0.03, 0.05)), 2)
        r.incrbyfloat(f"income:{uid}", change)
    return {"status": "updated"}
