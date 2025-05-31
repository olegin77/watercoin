import datetime

class AIRebalanceStrategy:
    def __init__(self, price_fetcher):
        self.price_fetcher = price_fetcher

    def decide(self, price_history):
        if len(price_history) < 2:
            return "HOLD"

        price_then = price_history[0][1]
        price_now = price_history[-1][1]

        if price_then == 0:
            return "HOLD"

        delta = (price_now - price_then) / price_then * 100

        if delta > 5:
            return "WATER"
        elif delta < -5:
            return "USDT"
        else:
            return "HOLD"
