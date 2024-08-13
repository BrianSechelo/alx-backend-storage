#!/usr/bin/env python3
"""
mod doc
"""
from pymongo import MongoClient
def log_stats():
    """ func docs"""
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}

    for method in methods:
        method_counts[method] = collection.count_documents({"method": method})

    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")

    status_checks = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_checks} status check")

if __name__ == "__main__":
    log_stats()
