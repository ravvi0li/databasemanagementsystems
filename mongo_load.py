from pymongo import MongoClient
import json
import time

client = MongoClient("mongodb://localhost:27017/")
db = client["benchmark"]
collection = db["records"]

def load(file):
    with open(file) as f:
        data = json.load(f)
    start = time.time()
    collection.insert_many(data)
    return time.time() - start

for size in [100_000, 500_000, 1_000_000]:
    t = load(f"data_{size}.json")
    print(f"MongoDB insert {size}: {t:.2f}s")
