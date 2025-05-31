import datetime
import random

class MockPriceFetcher:
    def get_price_history(self):
        now = datetime.datetime.utcnow()
        return [(now - datetime.timedelta(hours=i), 1.0 + random.uniform(-0.07, 0.07)) for i in reversed(range(24))]
