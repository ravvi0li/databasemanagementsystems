import random
import string
import json
import time

def random_payload():
    return {
        "action": random.choice(["read", "write", "update"]),
        "value": random.randint(1, 1000),
        "status": random.choice(["ok", "fail"])
    }

def generate_records(n):
    data = []
    for i in range(n):
        data.append({
            "id": i,
            "user_id": random.randint(1, 10000),
            "timestamp": time.time(),
            "payload": json.dumps(random_payload())
        })
    return data

if __name__ == "__main__":
    sizes = [100_000, 500_000, 1_000_000]
    for size in sizes:
        records = generate_records(size)
        with open(f"data_{size}.json", "w") as f:
            json.dump(records, f)
