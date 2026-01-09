import psycopg
import json
import time

CONN_STR = CONN_STR = (
    "postgresql://raveena:fDBHbWcrm69j1BsY8vRIvg@"
    "seg2102-test-19993.j77.aws-ap-southeast-1.cockroachlabs.cloud:26257/"
    "seg2102-test-19993.defaultdb"
    "?sslmode=verify-full"
    "&sslrootcert=/Users/ravvi0li/.postgresql/root.crt"
)

def load(file):
    with open(file) as f:
        data = json.load(f)

    conn = psycopg.connect(CONN_STR)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id SERIAL PRIMARY KEY,
            payload JSONB
        )
    """)
    conn.commit()

    start = time.time()

    BATCH_SIZE = 1000
    batch = []

    for row in data:
        batch.append((json.dumps(row),))
        if len(batch) == BATCH_SIZE:
            cur.executemany(
                "INSERT INTO records (payload) VALUES (%s)",
                batch
            )
            batch.clear()

    if batch:
        cur.executemany(
            "INSERT INTO records (payload) VALUES (%s)",
            batch
        )

    conn.commit()
    elapsed = time.time() - start

    cur.close()
    conn.close()

    return elapsed

for size in [100_000, 500_000, 1_000_000]:
   t = load(f"data_{size}.json")
   print(f"CockroachDB insert {size}: {t:.2f}s")
