from fastapi import FastAPI
from backend.services.price_fetcher import MockPriceFetcher
from backend.ai_engine.strategy import AIRebalanceStrategy

app = FastAPI()

@app.get("/rebalance-decision")
def get_rebalance_decision():
    fetcher = MockPriceFetcher()
    history = fetcher.get_price_history()
    strategy = AIRebalanceStrategy(fetcher)
    decision = strategy.decide(history)
    return {"decision": decision, "history": history[-3:]}
