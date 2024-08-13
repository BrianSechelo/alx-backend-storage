#!/usr/bin/env python3
from pymongo import MongoClient

def log_stats():
    client = MongoClient()  # Default connection to localhost:27017
    db = client.logs        # Access the logs database
    collection = db.nginx   # Access the nginx collection

    # Get the total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Initialize a dictionary for the methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}

    # Count the occurrences of each method
    for method in methods:
        method_counts[method] = collection.count_documents({"method": method})

    # Display the methods and their counts
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")

    # Count the number of logs with method=GET and path=/status
    status_checks = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_checks} status check")

    # Get the top 10 most frequent IPs
    top_ips = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    # Display the top 10 IPs
    print("IPs:")
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    log_stats()
