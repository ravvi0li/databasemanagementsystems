# DBMS Performance Benchmarking

This repository contains Python scripts used to benchmark write performance between MongoDB (NoSQL) and CockroachDB (NewSQL).

## Environment
- Python 3.11
- macOS (Apple M1)
- MongoDB (local)
- CockroachDB (cloud)

## Files
- `generate_data.py` – Generates synthetic datasets
- `mongo_load.py` – Bulk insert benchmarking for MongoDB
- `crdb_load.py` – Insert benchmarking for CockroachDB
- `read_test.py` – Read performance test (optional)
- `concurrency_test.py` – Concurrent workload test (optional)

## How to Run
```bash
python generate_data.py
python mongo_load.py
python crdb_load.py
